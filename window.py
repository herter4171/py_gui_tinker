from botocore.exceptions import ClientError
import wx

from ecr_fetcher import EcrFetcher
from repo_choice import repo_choice
from tag_choice import tag_choice
from help_button import help_button

class window(wx.Frame):
    def __init__(self, parent, title, ecr_fetcher: EcrFetcher):
        super(window, self).__init__(parent, title=title, size=(555, 450))


        panel = wx.Panel(self)

        try:
            ecr_fetcher.set_panel(panel)
            box = wx.BoxSizer(wx.VERTICAL)

            self.m_choice = repo_choice(panel, ecr_fetcher)
            self.p_choice = tag_choice(panel, ecr_fetcher)
            self.m_choice.set_tag_choice(self.p_choice)

            self._help_btn = help_button(panel)
        except ClientError as ex:
            pass
        finally:
           self.Centre()
           self.Show()
