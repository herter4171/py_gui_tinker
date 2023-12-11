import wx

class help_button(wx.Button):

    __msg_lines = ['Usage\n',
                   '0. Install the AWS CLI and run "aws configure" to set your credentials',
                   '1. Select a repository',
                   '2. Select a tag',
                   '3. Copy the full image spec']

    def __init__(self, parent, is_error=False):
        super().__init__(parent=parent,
                         pos=wx.Point(5, 395),
                         label='Help')

        self.Bind(wx.EVT_BUTTON, self.on_click)
        self._parent = parent

    def on_click(self, event):
        msg = '\n'.join(help_button.__msg_lines)
        wx.MessageBox(msg, "Help", wx.OK | wx.ICON_INFORMATION | wx.ALIGN_LEFT)