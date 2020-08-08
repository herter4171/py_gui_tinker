import wx
from prop_grid import prop_grid

class prop_frame(wx.Frame):
    def __init__(self, parent, ID, title, pos=wx.DefaultPosition, size=wx.Size(800, 400), style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        agrid = prop_grid(self)
        agrid.CreateGrid(7, 3)
        for count in range(3):
            for count2 in range(3):
                agrid.SetCellValue(count, count2, str(count + count2))

        agrid.lock_cells()