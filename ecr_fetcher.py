import boto3
import wx
from botocore.exceptions import ClientError

class EcrFetcher(object):

    @property
    def repo_names(self):
        try:
            resp = self._ecr_client.describe_repositories()['repositories']
        except ClientError as ex:
            self._pop_up_about_credentials_error(ex)
            raise ex

        all_repo_names = [repo['repositoryName'] for repo in resp]
        all_repo_names.sort()

        if not self._repo_uri_pfx and resp:
            self._repo_uri_pfx = resp[0]['repositoryUri'].split('/')[0]

        return self._prune_auth_repos(all_repo_names)

    @property
    def uri_pfx(self):
        return self._repo_uri_pfx

    @property
    def _ecr_client(self):
        return boto3.client('ecr')

    def __init__(self):
        self._panel = None
        self._known_auth_repos = set()
        self._repo_uri_pfx = None
        pass

    def set_panel(self, panel):
        self._panel = panel

    def get_tags_for_repository_name(self, repo_name: str) -> list:
        tag_key = 'imageTag'
        repo_tags = []

        resp = self._ecr_client.list_images(repositoryName=repo_name)

        for curr_img in resp['imageIds']:
            if tag_key in curr_img:
                repo_tags.append(curr_img[tag_key])

        repo_tags.sort()

        return repo_tags

    def _prune_auth_repos(self, all_repo_names):
        ecr_client = self._ecr_client

        for curr_name in all_repo_names:
            if curr_name in self._known_auth_repos:
                continue

            if self._check_repo_access(curr_name, ecr_client):
                self._known_auth_repos.add(curr_name)

        for_disp_repos = list(self._known_auth_repos)
        for_disp_repos.sort()

        return for_disp_repos

    def _check_repo_access(self, repo_name: str, ecr_client):
        authorized = False

        try:
            ecr_client.list_images(repositoryName=repo_name)
            authorized = True
        except ClientError:
            pass
        finally:
            return authorized

    def _pop_up_about_credentials_error(self, ex: ClientError):
        msg = "ERROR: Your AWS credentials didn't work or haven't been set.\n\
               Have you installed the AWS CLI and ran \"aws configure\"\n \
               to populate your credentials?"

        pop_up_window = wx.MessageBox(msg, "Credentials Error", wx.OK | wx.ALIGN_LEFT)
        pop_up_window.Show()