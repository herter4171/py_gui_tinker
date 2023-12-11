import wx

from ecr_fetcher import EcrFetcher


class tag_choice(wx.ListBox):

    @property
    def tag_name(self):
        return self._tag_name

    @property
    def _img_spec(self):
        return '{}:{}'.format(self._repo_name, self._tag_name)

    def __init__(self, parent, ecr_fetcher: EcrFetcher):
        super().__init__(parent=parent,
                         pos=wx.Point(300, 30),
                         size=wx.Size(250, 250))

        wx.StaticText(parent=parent, pos=wx.Point(300, 10), label="Tag:")

        self.Bind(wx.EVT_LISTBOX, self.on_choice)

        self._parent = parent
        self._repo_name = None
        self._tag_name = None

        wx.StaticText(parent=parent, pos=wx.Point(5, 290), label="Full Image Spec:")
        self._img_spec_tb = wx.TextCtrl(parent, pos=wx.Point(5, 310), size=wx.Size(545, 25), value="Image spec...", style=wx.TE_READONLY | wx.TE_LEFT)

    def set_repo_uri(self, repo_name: str):
        self._repo_name = repo_name
    def on_choice(self, event):
        # Get table data
        self._tag_name = self.GetString(self.GetSelection())
        self._img_spec_tb.SetValue(self._img_spec)