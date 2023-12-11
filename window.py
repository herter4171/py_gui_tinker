import wx

from ecr_fetcher import EcrFetcher
from repo_choice import repo_choice
from tag_choice import tag_choice

class window(wx.Frame):
    def __init__(self, parent, title, ecr_fetcher: EcrFetcher):
        super(window, self).__init__(parent, title=title, size=(555, 450))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        self.m_choice = repo_choice(panel, ecr_fetcher)
        self.p_choice = tag_choice(panel, ecr_fetcher)
        self.m_choice.set_tag_choice(self.p_choice)


        self.Centre()
        self.Show()
