
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:41:58 2017
@author: user
"""


import sys
import math as ma
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
import random
 

from PyQt5 import QtGui, QtCore, QtWidgets
g=9.8
RAD = ma.pi/180
PI = ma.pi
sigma=5.67*10**(-8)
G=6.67*10**(-11)
Ms=2*10**30
ae=150*10**9
class Animation(QtWidgets.QMainWindow) :
    def __init__(self) :
        QtWidgets.QMainWindow.__init__(self)
        self.resize(1500, 800)
        self.setWindowTitle('Algol')
        
        self.parama = QtWidgets.QLineEdit("10",self)
        self.parama.move(100,70)
        
        self.labela = QtWidgets.QLabel("a:",self)
        self.labela.move(20,70)
        
        
        self.paramm1 = QtWidgets.QLineEdit("10",self)
        self.paramm1.move(100,150)
      
        self.labelm1 = QtWidgets.QLabel("m1,M солнца:",self)
        self.labelm1.move(20,150)
        
        self.paramm2 = QtWidgets.QLineEdit("5",self)
        self.paramm2.move(100,190)
        
        self.labelm2 = QtWidgets.QLabel("m2,M солнца:",self)
        self.labelm2.move(20,190)
        
        self.paramr1 = QtWidgets.QLineEdit("70",self)
        self.paramr1.move(100,230)
        
        self.labelr1 = QtWidgets.QLabel("R1,тыс.км:",self)
        self.labelr1.move(20,230)
        
        self.paramr2= QtWidgets.QLineEdit("20",self)
        self.paramr2.move(100,270)
        
        self.labelr2 = QtWidgets.QLabel("R2,тыс.км:",self)
        self.labelr2.move(20,270)
        
        self.paramt1 = QtWidgets.QLineEdit("5000",self)
        self.paramt1.move(100,310)
       
        self.labelt1 = QtWidgets.QLabel("T1:",self)
        self.labelt1.move(20,310)
        
        self.paramt2 = QtWidgets.QLineEdit("3000",self)
        self.paramt2.move(100,350)
        
        self.labelt2 = QtWidgets.QLabel("T2:",self)
        self.labelt2.move(20,350)
        
        self.buttonStart = QtWidgets.QPushButton("Start",self)
        self.buttonStart.move(30,390)
        self.buttonStart.clicked.connect(self.onStart)

        self.buttonStop = QtWidgets.QPushButton("Stop",self)
        self.buttonStop.move(30,430)
        self.buttonStop.clicked.connect(self.onStop)       

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.onTimer) 
        
        a_str = self.parama.text() 

        self.a=float(str(a_str))
        
        m1_str = self.paramm1.text() 


        self.m1=float(str(m1_str))
        
        m2_str = self.paramm2.text() 

        self.m2=float(str(m2_str)) 
        
        R1_str = self.paramr1.text() 

        self.R1=float(str(R1_str)) 
        
        R2_str = self.paramr2.text() 
        
        self.R2=float(str(R2_str)) 
        
        T1_str = self.paramt1.text() 

        self.T1=float(str(T1_str)) 
        
        T2_str = self.paramt2.text() 

        self.T2=float(str(T2_str)) 

        
        
        self.P=ma.sqrt(2*PI*(self.a*ae)**3/G/((self.m1+self.m2)*Ms))
        self.P1=int(self.P/3600/24*100)/100
        self.P2=str(self.P1)
        self.labelP = QtWidgets.QLabel("P="+self.P2+"сут.",self)
        self.labelP.move(20,500)
        
        self.x1=0.0
        self.y1=0.0
        self.t=0.0
        #self.initUI()
        self.N=0
        
    def paintEvent(self,ev) :
       
        qp=QtGui.QPainter()
        qp.begin(self)
        
        self.x1=self.a*20*ma.cos(self.t)+self.x0
        self.y1=self.a*20*ma.sin(self.t)+self.y0


    
        qp.drawEllipse(self.x0,self.y0,self.R1,self.R1)
        qp.drawEllipse(self.x1,self.y1,self.R2,self.R2)
        
        
        qp.end()
        
        
    def onStart(self) :
        self.N=1
        self.t=0.0
        self.j=0
        self.timer.start()
        self.initUI()
        self.b = [[0] * 10000 for i in range(2)]
        self.I1=PI*self.R1*self.R1*sigma*self.T1*self.T1*self.T1*self.T1
        self.I2=PI*self.R2*self.R2*sigma*self.T2*self.T2*self.T2*self.T2
        
        self.S1=PI*self.R1*self.R1
        self.S2=PI*self.R2*self.R2

        self.I0=self.I1+self.I2

        self.x0=500
        self.y0=200
        self.j=0
        
        a_str = self.parama.text() 

        self.a=float(str(a_str))
        
        m1_str = self.paramm1.text() 


        self.m1=float(str(m1_str))
        
        m2_str = self.paramm2.text() 

        self.m2=float(str(m2_str)) 
        
        R1_str = self.paramr1.text() 

        self.R1=float(str(R1_str)) 
        
        R2_str = self.paramr2.text() 
        
        self.R2=float(str(R2_str)) 
        
        T1_str = self.paramt1.text() 

        self.T1=float(str(T1_str)) 
        
        T2_str = self.paramt2.text() 

        self.T2=float(str(T2_str)) 
        
        self.my_file = open('Algol.txt', 'w')
        self.update()
        
    def onTimer(self) :
        self.N+=1
        self.t+=0.1
        self.j+=1
        self.b[0][self.j] = self.t

            
        self.x1=200*ma.cos(self.t)+self.x0
        self.y1=200*ma.sin(self.t)+self.y0

                
                
        if self.x1>(self.R1+self.R2+self.x0) or self.x1<(-self.R1-self.R2+self.x0):
                        self.dI1=self.I1
                        self.dI2=self.I2
               
        if self.y1>=self.y0 and self.x1>(-self.R1+self.R2+self.x0) and self.x1<(self.R1-self.R2+self.x0):
                        self.dI1=self.I1
                        self.dI2=0
               
    
        if self.y1<self.y0 and self.x1>(-self.R1+self.R2+self.x0) and self.x1<(self.R1-self.R2+self.x0):
                        self.dI2=self.I2
                        self.dI1=(1-self.S2/self.S1)*self.I1

               
        I=self.dI1+self.dI2

                
        self.b[1][self.j] = I
                

                
        Is=str(self.b[1][self.j])
        ts=str(self.t)
        x11=str(self.x1)
        y11=str(self.y1)
            
        self.my_file.write(ts+'          '+Is+'          '+x11+'          '+y11+'\n')
        self.update()
        
    def onStop(self) :
        self.timer.stop()
        for i in range(self.N):
            self.c[i]=self.b[0][i]
            self.d[i]=self.b[1][i]
            
        self.my_file.close()
        self.update()
        self.initUI()
    def initUI(self):

        m = PlotCanvas(self, width=5, height=4)
        m.move(850,50)
 
        self.show()
    
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=120):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        
        
        data = [random.random() for i in range(10)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('Кривая блеска')
        self.draw()

app = QtWidgets.QApplication(sys.argv)

widget = Animation()
widget.show()
sys.exit(app.exec_())  