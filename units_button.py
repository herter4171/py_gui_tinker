import wx

from prop_choice import prop_choice
from units_dialog import units_dialog

class units_button(wx.Button):

    def __init__(self, parent, prop_chc):
        super().__init__(parent=parent,
                         pos=wx.Point(5, 200),
                         label='Set Units')

        assert (isinstance(prop_chc, prop_choice))

        self.Bind(wx.EVT_BUTTON, self.on_click)
        self._prop_chc = prop_chc

    def on_click(self, event):
        if not self._prop_chc.grid:
            msg = "You have to select a material property before changing units."
            wx.MessageBox(msg, "Help", wx.ICON_WARNING | wx.ICON_INFORMATION)
        else:
            ud = units_dialog(self._prop_chc)