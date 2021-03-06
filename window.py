import wx

from db_wrapper import db_wrapper
from mat_choice import mat_choice
from prop_choice import prop_choice
from help_button import help_button
from csv_button import csv_button
from units_button import units_button

class window(wx.Frame):
    def __init__(self, parent, title, db_wrap):
        super(window, self).__init__(parent, title=title, size=(1024, 768))
        assert(isinstance(db_wrap, db_wrapper))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        self.m_choice = mat_choice(panel, db_wrap)
        self.p_choice = prop_choice(panel, db_wrap)
        self.m_choice.set_prop_choice(self.p_choice)

        self._hb = help_button(panel)
        self._csvb = csv_button(panel, self.p_choice)
        #self._ub = units_button(panel, self.p_choice)

        #box.Add(self.m_choice, 0, 4)
        #box.Add(self.p_choice, 0, 4)

        #panel.SetSizer(box)
        self.Centre()
        self.Show()