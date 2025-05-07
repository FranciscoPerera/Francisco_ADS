import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="WxPython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Olá, mundo!")
        sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)

        button = wx.Button(panel, label="Clique aqui")
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)
        self.Show()

    def on_button_click(self, event):
        self.label.SetLabel("Você clicou!")

app = wx.App(False)
frame = MyFrame()
app.MainLoop()
