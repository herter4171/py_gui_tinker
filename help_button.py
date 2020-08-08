import wx

class help_button(wx.Button):

    def __init__(self, parent):
        super().__init__(parent=parent,
                         pos=wx.Point(5, 120),
                         label='Help')

        self.Bind(wx.EVT_BUTTON, self.on_click)
        self._parent = parent

    def on_click(self, event):
        msg = "Usage\n\n1. Select a material\n2. Select a property\n3. Copy from grid"
        wx.MessageBox(msg, "Help", wx.OK | wx.ICON_INFORMATION)