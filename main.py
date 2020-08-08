import wx

from db_wrapper import db_wrapper

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(300, 100))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        languages = ['C', 'C++', 'Python', 'Java', 'Perl']

        self.choice = wx.Choice(panel, choices=languages)
        box.Add(self.choice, 1, wx.EXPAND | wx.ALL, 5)

        box.AddStretchSpacer()

        panel.SetSizer(box)
        self.Centre()
        self.Show()

db_wrap = db_wrapper()
print("TABLE NAMES")
[print(x) for x in db_wrap.table_names]

print("\nMATERIAL_NAMES")
[print(x) for x in db_wrap.material_names]
#app = wx.App()
#Mywin(None, 'ComboBox and Choice demo')
#app.MainLoop()