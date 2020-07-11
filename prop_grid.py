#-----------------------------------------------------------------------------#
# NOTE: Lifted from top StackOverflow answer question 28509629
#-----------------------------------------------------------------------------#
import wx.grid
import wx

class prop_grid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_KEY_DOWN, self.on_key)
        self.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.on_label_right_click)
        self.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click)
        self.selected_rows = []
        self.selected_cols = []
        self.history = []

    def get_col_headers(self):
        return [self.GetColLabelValue(col) for col in range(self.GetNumberCols())]

    def get_table(self):
        for row in range(self.GetNumberRows()):
            result = {}
            for col, header in enumerate(self.get_col_headers()):
                result[header] = self.GetCellValue(row, col)
            yield result


    def on_cell_right_click(self, event):
        menus = [(wx.NewId(), "Copy", self.copy)]
        popup_menu = wx.Menu()
        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])

        self.PopupMenu(popup_menu, event.GetPosition())
        popup_menu.Destroy()
        return

    def on_label_right_click(self, event):
        menus = [(wx.NewId(), "Copy", self.copy)]

        # Select if right clicked row or column is not in selection
        if event.GetRow() > -1:
            if not self.IsInSelection(row=event.GetRow(), col=1):
                self.SelectRow(event.GetRow())
            self.selected_rows = self.GetSelectedRows()
        elif event.GetCol() > -1:
            if not self.IsInSelection(row=1, col=event.GetCol()):
                self.SelectCol(event.GetCol())
            self.selected_cols = self.GetSelectedCols()
        else:
            return

        popup_menu = wx.Menu()
        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])

        self.PopupMenu(popup_menu, event.GetPosition())
        popup_menu.Destroy()
        return

    def on_key(self, event):
        """
        Handles all key events.
        """
        # Ctrl+C or Ctrl+Insert
        if event.ControlDown() and event.GetKeyCode() in [67, 322]:
            self.copy(event)

        # Ctrl+A
        elif event.ControlDown() and event.GetKeyCode() == 65:
            self.SelectAll()

        else:
            event.Skip()

    def get_selection(self):
        """
        Returns selected range's start_row, start_col, end_row, end_col
        If there is no selection, returns selected cell's start_row=end_row, start_col=end_col
        """
        if not len(self.GetSelectionBlockTopLeft()):
            selected_columns = self.GetSelectedCols()
            selected_rows = self.GetSelectedRows()
            if selected_columns:
                start_col = selected_columns[0]
                end_col = selected_columns[-1]
                start_row = 0
                end_row = self.GetNumberRows() - 1
            elif selected_rows:
                start_row = selected_rows[0]
                end_row = selected_rows[-1]
                start_col = 0
                end_col = self.GetNumberCols() - 1
            else:
                start_row = end_row = self.GetGridCursorRow()
                start_col = end_col = self.GetGridCursorCol()
        elif len(self.GetSelectionBlockTopLeft()) > 1:
            wx.MessageBox("Multiple selections are not supported", "Warning")
            return []
        else:
            start_row, start_col = self.GetSelectionBlockTopLeft()[0]
            end_row, end_col = self.GetSelectionBlockBottomRight()[0]

        return [start_row, start_col, end_row, end_col]

    def get_selected_cells(self):
        # returns a list of selected cells
        selection = self.get_selection()
        if not selection:
            return

        start_row, start_col, end_row, end_col = selection
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                yield [row, col]

    def copy(self, event):
        """
        Copies range of selected cells to clipboard.
        """

        selection = self.get_selection()
        if not selection:
            return []
        start_row, start_col, end_row, end_col = selection

        data = u''

        rows = range(start_row, end_row + 1)
        for row in rows:
            columns = range(start_col, end_col + 1)
            for idx, column in enumerate(columns, 1):
                if idx == len(columns):
                    # if we are at the last cell of the row, add new line instead
                    data += self.GetCellValue(row, column) + "\n"
                else:
                    data += self.GetCellValue(row, column) + "\t"

        text_data_object = wx.TextDataObject()
        text_data_object.SetText(data)

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_data_object)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Can't open the clipboard", "Warning")

    def lock_cells(self):
        """Makes all cells read only."""
        for row in range(self.GetNumberRows()):
            for col in range(self.GetNumberCols()):
                self.SetReadOnly(row, col)