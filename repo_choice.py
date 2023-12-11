import wx

from ecr_fetcher import EcrFetcher
from tag_choice import tag_choice

class repo_choice(wx.ListBox):

    def __init__(self, parent, ecr_fetcher: EcrFetcher):
        super().__init__(parent=parent,
                         choices=ecr_fetcher.repo_names,
                         pos=wx.Point(5, 30),
                         size=wx.Size(250, 250))

        wx.StaticText(parent=parent, pos=wx.Point(5, 10), label="Repository:")


        self._ecr_fetcher = ecr_fetcher
        self.Bind(wx.EVT_LISTBOX, self.on_choice)

        self._prop_chc = None

    def set_tag_choice(self, prop_chc):
        self._prop_chc = prop_chc
        self.SetSelection(0)
        self.on_choice(None)

    def on_choice(self, event):
        assert (isinstance(self._prop_chc, tag_choice))
        repo_name = self.GetString(self.GetSelection())
        repo_tags = self._ecr_fetcher.get_tags_for_repository_name(repo_name)

        self._prop_chc.Clear()
        self._prop_chc.AppendItems(repo_tags)
        tag_latest = 'latest'

        repo_uri = '{}/{}'.format(self._ecr_fetcher.uri_pfx, repo_name)
        self._prop_chc.set_repo_uri(repo_uri)

        if tag_latest in repo_tags:
            self._prop_chc.SetSelection(repo_tags.index(tag_latest))
            self._prop_chc.on_choice(None)