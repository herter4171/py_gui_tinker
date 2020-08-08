import wx
import csv

from prop_choice import prop_choice

class csv_button(wx.Button):

    def __init__(self, parent, prop_chc):
        super().__init__(parent=parent,
                         pos=wx.Point(180, 120),
                         label='Save CSV')

        assert(isinstance(prop_chc, prop_choice))

        self.Bind(wx.EVT_BUTTON, self.on_click)
        self._prop_chc = prop_chc

    def on_click(self, event):
        # Warn user if they didn't select a mat prop first
        if not self._prop_chc.grid:
            msg = "You have to select a material property before saving."
            wx.MessageBox(msg, "Help", wx.ICON_WARNING | wx.ICON_INFORMATION)
        else:
            with wx.FileDialog(self, "Save CSV", wildcard="*.csv",
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

                if fileDialog.ShowModal() != wx.ID_CANCEL:
                    self.__write_grid_csv(fileDialog.GetPath())
                pass

    def __write_grid_csv(self, save_path):
        from prop_grid import prop_grid
        grid = self._prop_chc.grid
        assert(isinstance(grid, prop_grid))

        csv_file = open(save_path, 'w', newline='')
        csv_writer = csv.writer(csv_file)

        for curr_row in range(grid.GetNumberRows()):
            row_vals = []

            for curr_col in range(grid.GetNumberCols()):
                cell_val = grid.GetCellValue(curr_row, curr_col)
                row_vals.append(cell_val)

            csv_writer.writerow(row_vals)



