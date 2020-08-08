import wx

class prop_choice(wx.Choice):

    def __init__(self, parent):
        super().__init__(parent=parent,
                         pos=wx.Point(5, 80),
                         size=wx.Size(250, 20))
        text = wx.StaticText(parent=parent, pos=wx.Point(5, 60), label="Property:")
        self.Bind(wx.EVT_CHOICE, self.on_choice)

    def on_choice(self, event):
        print("MADE FOLLOWING CHOICE")
        print(self.GetString(self.GetSelection()))