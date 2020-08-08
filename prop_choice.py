import wx

class prop_choice(wx.Choice):

    def __init__(self, parent):
        super().__init__(parent=parent)

        self.Bind(wx.EVT_CHOICE, self.on_choice)

    def on_choice(self, event):
        print("MADE FOLLOWING CHOICE")
        print(self.GetString(self.GetSelection()))