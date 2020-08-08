import wx

from db_wrapper import db_wrapper
from prop_choice import prop_choice

class mat_choice(wx.Choice):

    def __init__(self, parent, db_wrap):
        super().__init__(parent=parent, choices=db_wrap.material_names)
        assert (isinstance(db_wrap, db_wrapper))

        self._db = db_wrap
        self.Bind(wx.EVT_CHOICE, self.on_choice)

        self._prop_chc = None

    def set_prop_choice(self, prop_chc):
        self._prop_chc = prop_chc

    def on_choice(self, event):
        assert(isinstance(self._prop_chc, prop_choice))
        mat_name = self.GetString(self.GetSelection())
        prop_tabs = list(self._db.get_mat_prop_table_names(mat_name))
        prop_tabs.sort()

        self._prop_chc.Clear()
        self._prop_chc.AppendItems(prop_tabs)
