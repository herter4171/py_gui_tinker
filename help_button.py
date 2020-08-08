import wx

class help_button(wx.Button):

    __msg_lines = ['Usage\n',
                   '1. Select a material from the menu in the upper-left',
                   '2. Choose a property for the selected material',
                   '3. Copy from the grid or save a CSV']

    def __init__(self, parent):
        super().__init__(parent=parent,
                         pos=wx.Point(5, 120),
                         label='Help')

        self.Bind(wx.EVT_BUTTON, self.on_click)
        self._parent = parent

    def on_click(self, event):
        msg = '\n'.join(help_button.__msg_lines)
        wx.MessageBox(msg, "Help", wx.OK | wx.ICON_INFORMATION)