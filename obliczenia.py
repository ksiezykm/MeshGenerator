# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:53:40 2015

@author: ksiezykm
"""
import numpy as np
#class Konwerter:
   # def __init__():
        #self.wejscie = wejscie
        #self.wyjscie = wyjscie
def obliczenia_funkcja(x,y):
    y[0]=100*y[0]
    y[3]=100*y[3]
    #print 'udalo sie'
    #print y
    #return y

def wypelnij_x(x):
    x[0]=1
    x[1]=51
    x[2]=102
    x[3]=153
    x[4]=204
    x[5]=256
    
def wypelnij_y(x,y):
    y[0]=x[0]**2
    y[1]=x[1]**2
    y[2]=x[2]**2
    y[3]=x[3]**2
    y[4]=x[4]**2
    y[5]=x[5]**2

def zakres_wykresu(liczba_wezlow,wspolrzedne_wezlow,zakres):

    zakres_n=1    
    
    for i in range(1,liczba_wezlow):
        if wspolrzedne_wezlow[i] < zakres:
            zakres_n=i+1
       
    return zakres_n
    

    #print zakres1_n,wspolrzedne_wezlow[zakres1_n],zakres2_n,wspolrzedne_wezlow[zakres2_n]
    
    
def wielomian_szostego_stopnia(x,y,y_plus,wezel,liczba_wezlow,wspolrzedne_wezlow,x_min,x_max,Re,Podzial,odwroc,wezly_rownomiernie,Przesuniecie):
    
    pomocnicza_zmienne = np.arange(0.0,1000,1.0)
    pomocnicza_stale = np.arange(0.0,1000,1.0)
    pomocnicza = np.arange(0.0,1000,1.0)
    liczba_wezlow_plus_1=liczba_wezlow-wezly_rownomiernie+1 
    liczba_wezlow_zmienne=liczba_wezlow-wezly_rownomiernie
    zmienne=abs(Podzial-x_min)
    stale=abs(x_max-Podzial)
    
   # if odwroc == 1:
        #zmienne=abs(x_max-Podzial)
        #stale=abs(Podzial-x_min)
    
    krok_staly=0.0
    
    if wezly_rownomiernie > 1:
        krok_staly=stale/float(wezly_rownomiernie)
    
    A1 = np.arange(0.0,7,1.0)
    A2 = np.arange(0.0,7,1.0)
    A3 = np.arange(0.0,7,1.0)
    A4 = np.arange(0.0,7,1.0)
    A5 = np.arange(0.0,7,1.0)
    A6 = np.arange(0.0,7,1.0)
    A7 = np.arange(0.0,7,1.0)
    A = np.arange(0.0,7,1.0)
    wektor_wynikow = np.arange(0.0,7,1.0)
    #print x
    #for i in range(0,6):
        #print i,x[i]
    
    for i in range(0,7):
        A1[i]=pow(x[0],(6-i))
        
    #print A1
    
    for i in range(0,7):
        A2[i]=pow(x[1],(6-i))
        
    #print A2
    
    for i in range(0,7):
        A3[i]=pow(x[2],(6-i))
        
    #print A3
    
    for i in range(0,7):
        A4[i]=pow(x[3],(6-i))
        
    #print A4
    
    for i in range(0,7):
        A5[i]=pow(x[4],(6-i))
        
    #print A5
    
    for i in range(0,7):
        A6[i]=pow(x[5],(6-i))
        
    #print A6
    
    for i in range(0,7):
        A7[i]=((1.0/(7-i)) * pow(x[5],(7-i))) - ((1.0/(7-i)) * pow(x[0],(7-i)))
        
   # print A7
    
    A = np.array([A1,A2,A3,A4,A5,A6,A7])
    
    #print A
    
    wektor_wynikow = np.array([y[0],y[1],y[2],y[3],y[4],y[5],zmienne])
    
   # print wektor_wynikow
        
    abcdefg = np.linalg.solve(A,wektor_wynikow)
    
    
    
   # print abcdefg
   
      
    #wspolrzedne_wezlow = np.arange(0.0,1000,1.0)
    #wezel = np.arange(0.0,liczba_wezlow_plus_1,1.0)
    #y_plus = np.arange(0.0,liczba_wezlow_plus_1,1.0)
    
   
        
    pomocnicza_zmienne[0]=x_min
    
    for i in range(1,liczba_wezlow_zmienne):
        pomocnicza_zmienne[i] = pomocnicza_zmienne[i-1] + ( (abcdefg[0]*pow((i-1),6)) + (abcdefg[1]*pow((i-1),5)) + (abcdefg[2]*pow((i-1),4)) + (abcdefg[3]*pow((i-1),3)) + (abcdefg[4]*pow((i-1),2)) + (abcdefg[5]*pow((i-1),1)) + (abcdefg[6]*pow((i-1),0)) )
    
   
    pomocnicza_stale[0]=pomocnicza_zmienne[liczba_wezlow_zmienne-1]+krok_staly
        
    for i in range(1,wezly_rownomiernie):
        pomocnicza_stale[i] = pomocnicza_stale[i-1] + krok_staly
            
            
    for i in range(0,liczba_wezlow_zmienne):
        wspolrzedne_wezlow[i]=pomocnicza_zmienne[i]
            
    for i in range(0,wezly_rownomiernie):
        wspolrzedne_wezlow[i+liczba_wezlow_zmienne]=pomocnicza_stale[i]
            
   
        
    
        
           
    for i in range(0,liczba_wezlow):
        wspolrzedne_wezlow[i]=wspolrzedne_wezlow[i]/wspolrzedne_wezlow[liczba_wezlow-1]
        
    for i in range(0,liczba_wezlow):
        wspolrzedne_wezlow[i]=wspolrzedne_wezlow[i]*x_max
        
    for i in range(0,liczba_wezlow):
        wspolrzedne_wezlow[i]=wspolrzedne_wezlow[i]-Przesuniecie
    
    if odwroc == 1:
        
        for i in range(0,liczba_wezlow):
            pomocnicza[i]=wspolrzedne_wezlow[liczba_wezlow-i-1]
            
        for i in range(0,liczba_wezlow):
            wspolrzedne_wezlow[i]=x_max
            
        for i in range(0,liczba_wezlow):
            wspolrzedne_wezlow[i]=x_max-pomocnicza[i]
    
   # print liczba_wezlow_plus_1
        
   # y_plus = np.arange(0.0,liczba_wezlow_plus_1,1.0)
    #wezel = np.arange(0.0,liczba_wezlow_plus_1,1.0)
    
    for i in range(1,liczba_wezlow):
         y_plus[i]=(wspolrzedne_wezlow[i]-wspolrzedne_wezlow[i-1])

    #for i in range(0,liczba_wezlow):
        #print i, wspolrzedne_wezlow[i], y_plus[i]
    
    y_plus[0]=y_plus[1]
    
    
    del A,A1,A2,A3,A4,A5,A6,A7,wektor_wynikow,pomocnicza,pomocnicza_stale,pomocnicza_zmienne,abcdefg















