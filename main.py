import wx


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


app = wx.App()
Mywin(None, 'ComboBox and Choice demo')
app.MainLoop()