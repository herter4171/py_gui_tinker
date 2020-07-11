import wx
from prop_frame import prop_frame

class mats_app(wx.App):
    def OnInit(self):
        frame = prop_frame(None, -1, "A copy and paste grid")

        frame.Show(True)
        self.SetTopWindow(frame)
        return True