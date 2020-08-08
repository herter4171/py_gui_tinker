import wx

from prop_choice import prop_choice
from prop_grid import prop_grid

class units_dialog(wx.Frame):

    def __init__(self, prop_chc):
        super().__init__(None, title="Unit Specification")
        assert (isinstance(prop_chc, prop_choice))

        self._prop_chc = prop_chc
        self._panel = wx.Panel(self)

        self._fields, self._units = self.__get_unit_spec()
        self._unit_map = {}
        vert_interval = 40

        for i in range(len(self._fields)):
            txt_pos = wx.Point(5, 5 + i*vert_interval)
            fld_pos = wx.Point(150, 5 + i*vert_interval)

            wx.StaticText(parent=self._panel, pos=txt_pos, label=self._fields[i])
            txt_box = wx.TextCtrl(parent=self._panel, pos=fld_pos, value=self._units[i])
            self._unit_map[self._fields[i]] = txt_box

        self.Show()
        self.Bind(wx.EVT_CLOSE, self.on_close)
        print("DONE")

    def __get_unit_spec(self):
        grid = self._prop_chc.grid
        assert(isinstance(grid, prop_grid))

        fields = []
        units = []

        for curr_col in range(grid.GetNumberCols()):
            heading = grid.GetCellValue(0, curr_col)
            split_args = heading.split('(')

            fields.append(split_args[0].strip())
            units.append(split_args[1].replace(')', ''))

        return fields, units

    def on_close(self, event):
        print("CLOSED")
        self.Destroy()