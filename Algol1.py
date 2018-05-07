
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:41:58 2017
@author: user
"""


import sys
import math as ma
from PyQt5 import QtGui, QtCore, QtWidgets
g=9.8
RAD = ma.pi/180
PI = ma.pi

class Animation(QtWidgets.QMainWindow) :
    def __init__(self) :
        QtWidgets.QMainWindow.__init__(self)
        self.resize(1000, 800)
        self.setWindowTitle('Circ')
        
        self.parama1 = QtWidgets.QLineEdit("1",self)
        self.parama1.move(70,70)
        
        self.labela1 = QtWidgets.QLabel("a:",self)
        self.labela1.move(20,70)
        
        self.parama2 = QtWidgets.QLineEdit("0",self)
        self.parama2.move(70,110)
      
        self.labela2 = QtWidgets.QLabel("e:",self)
        self.labela2.move(20,110)
        
        self.paraml = QtWidgets.QLineEdit("10",self)
        self.paraml.move(70,150)
      
        self.labell = QtWidgets.QLabel("P:",self)
        self.labell.move(20,150)
        
        self.paraml1 = QtWidgets.QLineEdit("5",self)
        self.paraml1.move(70,190)
        
        self.labell1 = QtWidgets.QLabel("M1/M2:",self)
        self.labell1.move(20,190)
        
        self.paramk = QtWidgets.QLineEdit("2",self)
        self.paramk.move(70,230)
        
        self.labelk = QtWidgets.QLabel("R1:",self)
        self.labelk.move(20,230)
        
        self.paramm = QtWidgets.QLineEdit("1",self)
        self.paramm.move(70,270)
        
        self.labelm = QtWidgets.QLabel("R2:",self)
        self.labelm.move(20,270)
        
        self.paramv1 = QtWidgets.QLineEdit("5000",self)
        self.paramv1.move(70,310)
       
        self.labelv1 = QtWidgets.QLabel("T1:",self)
        self.labelv1.move(20,310)
        
        self.paramv2 = QtWidgets.QLineEdit("15000",self)
        self.paramv2.move(70,350)
        
        self.labelv2 = QtWidgets.QLabel("T2:",self)
        self.labelv2.move(20,350)
        
        self.buttonStart = QtWidgets.QPushButton("Start",self)
        self.buttonStart.move(30,390)
        self.buttonStart.clicked.connect(self.onStart)

        self.buttonStop = QtWidgets.QPushButton("Stop",self)
        self.buttonStop.move(30,430)
        self.buttonStop.clicked.connect(self.onStop)       

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.onTimer) 
        
        self.x1=0.0
        self.y1=0.0
        self.t=0.0
        
        
    def paintEvent(self,ev) :
       
        qp=QtGui.QPainter()
        qp.begin(self)
        
        self.x1=200*ma.cos(self.t)-150
        self.y1=200*ma.sin(self.t)
        
        
        qp.drawEllipse(395,200,70,70)
        qp.drawEllipse(595+self.x1,225+self.y1,20,20)
        
        qp.end()
        
        
    def onTimer(self) :
        
        self.t+=0.1
        self.update()
        
    def onStart(self) :
        
       self.t=0.0
       self.timer.start()
       
        
    def onStop(self) :
        self.timer.stop()

class Chlenkita():
        
        
        a = [[0] * 100 for i in range(2)]
        t=0.0
        sigma=1
        R1=70
        R2=20
        T1=5000
        T2=1500
        
        I1=4*PI*R1*R1*sigma*T1*T1*T1*T1
        I2=4*PI*R2*R2*sigma*T2*T2*T2*T2
        
        I0=I1+I2
        for j in range(100):
            
            a[0][j] = t
            t+=0.1
            
            x1=200*ma.cos(t)-150+595-R2
            y1=200*ma.sin(t)
            x0=395+R1
            y0=200+R1
            s=ma.fabs(x1-x0)
            if s<=R1:
                S1=R1*R1*ma.acos(s/R1)
                S2=s*ma.sqrt(R1*R1-s*s)
                if y1>y0 and x1>x0:
                    S0=S1-S2
                if y1>y0 and x1<x0:
                    S0=S1+S2
                if y1<y0 and x1<x0:
                    S0=S1+S2
                if y1<y0 and x1>x0:
                    S0=S1-S2
            else:
                    I=I0
                
                
            I=ma.sin(t)
            a[1][j] = s
                

        for row in a:
            print(' '.join([str(elem) for elem in row]))
            
app = QtWidgets.QApplication(sys.argv)

widget = Animation()
widget.show()
sys.exit(app.exec_())  