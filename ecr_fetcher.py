import boto3


class EcrFetcher(object):

    @property
    def repo_names(self):
        resp = self._ecr_client.describe_repositories()['repositories']

        repo_names = [repo['repositoryName'] for repo in resp]
        repo_names.sort()

        if not self._repo_uri_pfx and resp:
            self._repo_uri_pfx = resp[0]['repositoryUri'].split('/')[0]

        return repo_names

    @property
    def uri_pfx(self):
        return self._repo_uri_pfx

    @property
    def _ecr_client(self):
        return boto3.client('ecr')

    def __init__(self):
        self._repo_uri_pfx = None
        pass

    def get_tags_for_repository_name(self, repo_name: str) -> list:
        tag_key = 'imageTag'
        repo_tags = []

        resp = self._ecr_client.list_images(repositoryName=repo_name)

        for curr_img in resp['imageIds']:
            if tag_key in curr_img:
                repo_tags.append(curr_img[tag_key])

        repo_tags.sort()

        return repo_tags