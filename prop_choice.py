import wx

from db_wrapper import db_wrapper
from prop_grid import prop_grid

class prop_choice(wx.Choice):

    @property
    def grid(self):
        return self._grid

    def __init__(self, parent, db_wrap):
        super().__init__(parent=parent,
                         pos=wx.Point(5, 80),
                         size=wx.Size(250, 20))

        assert (isinstance(db_wrap, db_wrapper))

        wx.StaticText(parent=parent, pos=wx.Point(5, 60), label="Property:")

        self.Bind(wx.EVT_CHOICE, self.on_choice)

        self._db = db_wrap
        self._parent = parent
        self._grid = None

    def on_choice(self, event):
        # Get table data
        tab_name = self.GetString(self.GetSelection())
        tab_data = self._db.get_table_data_raw(tab_name)

        # Get dimensions
        num_cols = len(tab_data[0])
        num_rows = len(tab_data)

        # Clear old grid
        if self._grid:
            self._grid.Destroy()

        # Make a new grid
        self._grid = prop_grid(self._parent)
        self._grid.CreateGrid(num_rows, num_cols)

        # Populate the grid
        for curr_row in range(num_rows):
            for curr_col in range(num_cols):
                cell_val = str(tab_data[curr_row][curr_col])
                self._grid.SetCellValue(curr_row, curr_col, cell_val)

        self._grid.AutoSizeColumns()
        #self._grid.AlwaysShowScrollbars()

        # Set to read-only
        self._grid.lock_cells()