import wx

from db_wrapper import db_wrapper
from prop_grid import prop_grid

class prop_choice(wx.Choice):

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
        print("MADE FOLLOWING CHOICE")
        tab_name = self.GetString(self.GetSelection())

        # Clear old grid
        if self._grid:
            self._grid.Destroy()

        # Make a new grid
        self._grid = prop_grid(self._parent)
        self._grid.CreateGrid(7, 7)

        # Populate the grid
        for count in range(3):
            for count2 in range(3):
                self._grid.SetCellValue(count, count2, tab_name)

        self._grid.AutoSizeColumns()

        # Set to read-only
        self._grid.lock_cells()
        