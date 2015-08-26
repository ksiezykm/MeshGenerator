import wx
import numpy as np
import matplotlib
matplotlib.use('GTKAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import pylab
from obliczenia import *
# begin wxGlade: extracode
# end wxGlade
liczba=4
pozycja=0
liczba_wezlow=320

zakres1=2.1
zakres2=2.2
zakres1_n=89
zakres2_n=223
liczba_wezlow_w_zakresie=1
x1=1
x2=50
x3=100
x4=160
x5=280
x6=320

y1=7.8/100
y2=1.0/100
y3=0.6/100
y4=0.65/100
y5=3.2/100
y6=7.1/100

wezel = np.arange(1000)
y_plus= np.arange(0.0,1000,1.0)
wspolrzedne_wezlow = np.arange(0.0,1000,1.0)


x=[x1,x2,x3,x4,x5,x6]
y=[y1,y2,y3,y4,y5,y6]
#wypelnij_x(x)
#wypelnij_y(x,y)
class MyFrame2(wx.Frame):
    def __init__(self, *args, **kwds):
        self.figure = matplotlib.figure.Figure()        
        
        # begin wxGlade: MyFrame2.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_3 = wx.Panel(self, -1)
        self.name_y1 = wx.StaticText(self.panel_3, -1, "y1", style=wx.ALIGN_CENTRE)
        self.text_ctrl_y1 = wx.TextCtrl(self.panel_3, -1, str(y[0]))
        self.name_y2 = wx.StaticText(self.panel_3, -1, "y2", style=wx.ALIGN_CENTRE)
        self.text_ctrl_y2 = wx.TextCtrl(self.panel_3, -1, str(y[1]))
        self.name_y3 = wx.StaticText(self.panel_3, -1, "y3", style=wx.ALIGN_CENTRE)
        self.text_ctrl_y3 = wx.TextCtrl(self.panel_3, -1, str(y[2]))
        self.name_y4 = wx.StaticText(self.panel_3, -1, "y4", style=wx.ALIGN_CENTRE)
        self.text_ctrl_y4 = wx.TextCtrl(self.panel_3, -1, str(y[3]))
        self.name_y5 = wx.StaticText(self.panel_3, -1, "y5", style=wx.ALIGN_CENTRE)
        self.text_ctrl_y5 = wx.TextCtrl(self.panel_3, -1, str(y[4]))
        self.name_y6 = wx.StaticText(self.panel_3, -1, "y6", style=wx.ALIGN_CENTRE)
        self.text_ctrl_y6 = wx.TextCtrl(self.panel_3, -1, str(y[5]))
        self.zakres_wyswietlania1 = wx.StaticText(self.panel_3, -1, "zakres")
        self.text_ctrl_zakres1 = wx.TextCtrl(self.panel_3, -1, str(zakres1))
        self.zakres_wyswietlania2 = wx.StaticText(self.panel_3, -1, "0")
        self.text_ctrl_zakres2 = wx.TextCtrl(self.panel_3, -1, str(zakres2))
        self.window_2 = FigureCanvas(self, -1, self.figure)
        self.panel_5 = wx.Panel(self, -1)
        self.name_wezly = wx.StaticText(self.panel_5, -1, "ilosc wezlow")
        self.spin_ctrl_ilosc_wezlow = wx.SpinCtrl(self.panel_5, -1, str(liczba_wezlow), min=0, max=10000)
        self.name_x_min = wx.StaticText(self.panel_5, -1, "x min")
        self.text_ctrl_x_min = wx.TextCtrl(self.panel_5, -1, "")
        self.name_x_max = wx.StaticText(self.panel_5, -1, "x max")
        self.text_ctrl_x_max = wx.TextCtrl(self.panel_5, -1, "")
        self.panel_6 = wx.Panel(self, -1)
        self.spin_ctrl_x1 = wx.SpinCtrl(self.panel_6, -1, str(x[0]), min=1, max=liczba_wezlow)
        self.spin_ctrl_x2 = wx.SpinCtrl(self.panel_6, -1, str(x[1]), min=1, max=liczba_wezlow)
        self.spin_ctrl_x3 = wx.SpinCtrl(self.panel_6, -1, str(x[2]), min=1, max=liczba_wezlow)
        self.spin_ctrl_x4 = wx.SpinCtrl(self.panel_6, -1, str(x[3]), min=1, max=liczba_wezlow)
        self.spin_ctrl_x5 = wx.SpinCtrl(self.panel_6, -1, str(x[4]), min=1, max=liczba_wezlow)
        self.spin_ctrl_x6 = wx.SpinCtrl(self.panel_6, -1, str(x[5]), min=1, max=liczba_wezlow)
        self.name_x2 = wx.StaticText(self.panel_6, -1, "x2", style=wx.ALIGN_CENTRE)
        self.name_x3 = wx.StaticText(self.panel_6, -1, "x3", style=wx.ALIGN_CENTRE)
        self.name_x4 = wx.StaticText(self.panel_6, -1, "x4", style=wx.ALIGN_CENTRE)
        self.name_x5 = wx.StaticText(self.panel_6, -1, "x5", style=wx.ALIGN_CENTRE)
        self.name_x6 = wx.StaticText(self.panel_6, -1, "x6", style=wx.ALIGN_CENTRE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.evt_y1, self.text_ctrl_y1)
        self.Bind(wx.EVT_TEXT, self.evt_y2, self.text_ctrl_y2)
        self.Bind(wx.EVT_TEXT, self.evt_y3, self.text_ctrl_y3)
        self.Bind(wx.EVT_TEXT, self.evt_y4, self.text_ctrl_y4)
        self.Bind(wx.EVT_TEXT, self.evt_y5, self.text_ctrl_y5)
        self.Bind(wx.EVT_TEXT, self.evt_y6, self.text_ctrl_y6)
        self.Bind(wx.EVT_TEXT, self.evt_zakres1, self.text_ctrl_zakres1)
        self.Bind(wx.EVT_TEXT, self.evt_zakres2, self.text_ctrl_zakres2)
        self.Bind(wx.EVT_SPINCTRL, self.evt_ilosc_wezlow, self.spin_ctrl_ilosc_wezlow)
        self.Bind(wx.EVT_TEXT, self.evt_x_min, self.text_ctrl_x_min)
        self.Bind(wx.EVT_TEXT, self.evt_x_max, self.text_ctrl_x_max)
        self.Bind(wx.EVT_SPINCTRL, self.evt_x1, self.spin_ctrl_x1)
        self.Bind(wx.EVT_SPINCTRL, self.evt_x2, self.spin_ctrl_x2)
        self.Bind(wx.EVT_SPINCTRL, self.evt_x3, self.spin_ctrl_x3)
        self.Bind(wx.EVT_SPINCTRL, self.evt_x4, self.spin_ctrl_x4)
        self.Bind(wx.EVT_SPINCTRL, self.evt_x5, self.spin_ctrl_x5)
        self.Bind(wx.EVT_SPINCTRL, self.evt_x6, self.spin_ctrl_x6)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame2.__set_properties
        self.SetTitle("frame_3")
        self.SetSize((970, 600))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame2.__do_layout
        grid_sizer_9 = wx.FlexGridSizer(2, 2, 0, 0)
        grid_sizer_11 = wx.FlexGridSizer(2, 6, 0, 0)
        grid_sizer_12 = wx.GridSizer(3, 2, 0, 0)
        grid_sizer_10 = wx.FlexGridSizer(8, 2, 0, 0)
        grid_sizer_10.Add(self.name_y1, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_y1, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.name_y2, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_y2, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.name_y3, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_y3, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.name_y4, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_y4, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.name_y5, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_y5, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.name_y6, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_y6, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.zakres_wyswietlania1, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_zakres1, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.zakres_wyswietlania2, 0, wx.ALL, 5)
        grid_sizer_10.Add(self.text_ctrl_zakres2, 0, wx.ALL, 5)
        self.panel_3.SetSizer(grid_sizer_10)
        grid_sizer_9.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_9.Add(self.window_2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_12.Add(self.name_wezly, 0, wx.ALL, 5)
        grid_sizer_12.Add(self.spin_ctrl_ilosc_wezlow, 0, wx.ALL, 5)
        grid_sizer_12.Add(self.name_x_min, 0, wx.ALL, 5)
        grid_sizer_12.Add(self.text_ctrl_x_min, 0, wx.ALL, 5)
        grid_sizer_12.Add(self.name_x_max, 0, wx.ALL, 5)
        grid_sizer_12.Add(self.text_ctrl_x_max, 0, wx.ALL, 5)
        self.panel_5.SetSizer(grid_sizer_12)
        grid_sizer_9.Add(self.panel_5, 1, wx.EXPAND, 0)
        grid_sizer_11.Add(self.spin_ctrl_x1, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.spin_ctrl_x2, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.spin_ctrl_x3, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.spin_ctrl_x4, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.spin_ctrl_x5, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.spin_ctrl_x6, 0, wx.ALL, 5)
        name_x1 = wx.StaticText(self.panel_6, -1, "x1", style=wx.ALIGN_CENTRE)
        grid_sizer_11.Add(name_x1, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.name_x2, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.name_x3, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.name_x4, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.name_x5, 0, wx.ALL, 5)
        grid_sizer_11.Add(self.name_x6, 0, wx.ALL, 5)
        self.panel_6.SetSizer(grid_sizer_11)
        grid_sizer_9.Add(self.panel_6, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_9)
        self.Layout()
        # end wxGlade

    def wykres(self,x,y,liczba_wezlow,zakres1,zakres2):
        
        zakres1=float(self.text_ctrl_zakres1.GetValue())
        zakres2=float(self.text_ctrl_zakres2.GetValue())
               
        wielomian_szostego_stopnia(x,y,y_plus,wezel,liczba_wezlow,wspolrzedne_wezlow)
        
        zakres1_n = zakres_wykresu(liczba_wezlow,wspolrzedne_wezlow,zakres1)
        zakres2_n = zakres_wykresu(liczba_wezlow,wspolrzedne_wezlow,zakres2) 
        
        liczba_wezlow_w_zakresie=zakres2_n-zakres1_n
        self.zakres_wyswietlania2.SetLabel(str(liczba_wezlow_w_zakresie))
        
       
        self.figure = matplotlib.figure.Figure()
        self.y_plus_n = self.figure.add_subplot(2,2,1)
        self.y_plus_x = self.figure.add_subplot(2,2,2)
        self.y_plus_x2 = self.figure.add_subplot(2,1,2)
        
        
        #print wspolrzedne_wezlow[liczba_wezlow-1]
        #print zakres1_n,zakres2_n
        
        self.y_plus_n.plot(wezel[0:liczba_wezlow],y_plus[0:liczba_wezlow])
        
        self.y_plus_x.plot(wspolrzedne_wezlow[0:liczba_wezlow],y_plus[0:liczba_wezlow]) 
        
        self.y_plus_x2.plot(wspolrzedne_wezlow[zakres1_n:zakres2_n],y_plus[zakres1_n:zakres2_n],marker='o', color='r') 
        
        self.window_2 = FigureCanvas(self, -1, self.figure)
         
        self.__set_properties()
        self.__do_layout()

    def evt_x1(self, event):  # wxGlade: MyFrame2.<event_handler>
        x[0]=int(self.spin_ctrl_x1.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        
        event.Skip()

    def evt_x2(self, event):  # wxGlade: MyFrame2.<event_handler>
        x[1]=int(self.spin_ctrl_x2.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_x3(self, event):  # wxGlade: MyFrame2.<event_handler>
        x[2]=int(self.spin_ctrl_x3.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_x4(self, event):  # wxGlade: MyFrame2.<event_handler>
        x[3]=int(self.spin_ctrl_x4.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_x5(self, event):  # wxGlade: MyFrame2.<event_handler>
        x[4]=int(self.spin_ctrl_x5.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_x6(self, event):  # wxGlade: MyFrame2.<event_handler>
        x[5]=int(self.spin_ctrl_x6.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_y1(self, event):  # wxGlade: MyFrame2.<event_handler>
        y[0]=float(self.text_ctrl_y1.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_y2(self, event):  # wxGlade: MyFrame2.<event_handler>
        y[1]=float(self.text_ctrl_y2.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_y3(self, event):  # wxGlade: MyFrame2.<event_handler>
        y[2]=float(self.text_ctrl_y3.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_y4(self, event):  # wxGlade: MyFrame2.<event_handler>
        y[3]=float(self.text_ctrl_y4.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_y5(self, event):  # wxGlade: MyFrame2.<event_handler>
        y[4]=float(self.text_ctrl_y5.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_y6(self, event):  # wxGlade: MyFrame2.<event_handler>
        y[5]=float(self.text_ctrl_y6.GetValue())
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_ilosc_wezlow(self, event):  # wxGlade: MyFrame2.<event_handler>
        liczba_wezlow=int(self.spin_ctrl_ilosc_wezlow.GetValue())
        self.spin_ctrl_x6.SetRange(1,liczba_wezlow)
        self.spin_ctrl_x5.SetRange(1,liczba_wezlow)
        self.spin_ctrl_x4.SetRange(1,liczba_wezlow)
        self.spin_ctrl_x3.SetRange(1,liczba_wezlow)
        self.spin_ctrl_x2.SetRange(1,liczba_wezlow)
        self.spin_ctrl_x1.SetRange(1,liczba_wezlow)
        self.spin_ctrl_zakres1.SetRange(1,liczba_wezlow)
        self.spin_ctrl_zakres2.SetRange(1,liczba_wezlow)
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_x_min(self, event):  # wxGlade: MyFrame2.<event_handler>
        print "Event handler `evt_x_min' not implemented"
        event.Skip()

    def evt_x_max(self, event):  # wxGlade: MyFrame2.<event_handler>
        print "Event handler `evt_x_max' not implemented"
        event.Skip()
        
    def evt_zakres1(self, event):  # wxGlade: MyFrame2.<event_handler>
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()

    def evt_zakres2(self, event):  # wxGlade: MyFrame2.<event_handler>
        self.wykres(x,y,liczba_wezlow,zakres1,zakres2)
        event.Skip()


# end of class MyFrame2
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame2(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()