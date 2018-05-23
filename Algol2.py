
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:41:58 2017
@author: user
"""


import sys
import math as ma
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
g=9.8
RAD = ma.pi/180
PI = ma.pi
sigma=1


class Animation(QtWidgets.QMainWindow) :
    def __init__(self) :
        QtWidgets.QMainWindow.__init__(self)
        self.resize(1000, 800)
        self.setWindowTitle('Circ')
        
        self.parama = QtWidgets.QLineEdit("50",self)
        self.parama.move(70,70)
        
        self.labela = QtWidgets.QLabel("a:",self)
        self.labela.move(20,70)
        
        
        self.paramp = QtWidgets.QLineEdit("10",self)
        self.paramp.move(70,150)
      
        self.labelp = QtWidgets.QLabel("P:",self)
        self.labelp.move(20,150)
        
        self.paramm = QtWidgets.QLineEdit("5",self)
        self.paramm.move(70,190)
        
        self.labelm = QtWidgets.QLabel("M1/M2:",self)
        self.labelm.move(20,190)
        
        self.paramr1 = QtWidgets.QLineEdit("70",self)
        self.paramr1.move(70,230)
        
        self.labelr1 = QtWidgets.QLabel("R1:",self)
        self.labelr1.move(20,230)
        
        self.paramr2= QtWidgets.QLineEdit("20",self)
        self.paramr2.move(70,270)
        
        self.labelr2 = QtWidgets.QLabel("R2:",self)
        self.labelr2.move(20,270)
        
        self.paramt1 = QtWidgets.QLineEdit("5000",self)
        self.paramt1.move(70,310)
       
        self.labelt1 = QtWidgets.QLabel("T1:",self)
        self.labelt1.move(20,310)
        
        self.paramt2 = QtWidgets.QLineEdit("15000",self)
        self.paramt2.move(70,350)
        
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

        a=float(str(a_str))
        
        P_str = self.paramp.text() 


        P=float(str(P_str))
        
        M_str = self.paramm.text() 

        M=float(str(M_str)) 
        
        R1_str = self.paramr1.text() 

        R1=float(str(R1_str)) 
        
        R2_str = self.paramr2.text() 
        
        R2=float(str(R2_str)) 
        
        T1_str = self.paramt1.text() 

        T1=float(str(T1_str)) 
        
        T2_str = self.paramt2.text() 

        T2=float(str(T2_str)) 
        
        
        self.x1=0.0
        self.y1=0.0
        self.t=0.0
        
        
    def paintEvent(self,ev) :
       
        qp=QtGui.QPainter()
        qp.begin(self)
        
        self.x1=200*ma.cos(self.t)+395
        self.y1=200*ma.sin(self.t)
       # print (self.x1,self.y1, self.t)

    
        qp.drawEllipse(395,200,70,70)
        qp.drawEllipse(self.x1,225+self.y1,20,20)
        
        qp.end()
        
        
    def onTimer(self) :
        
        self.t+=0.1
        self.update()
        self.j+=1
        self.b[0][self.j] = self.t

            
        self.x1=200*ma.cos(self.t)+self.x0
        self.y1=200*ma.sin(self.t)+self.y0

                
                
        if self.x1>(self.R1+self.R2+self.x0) or self.x1<(-self.R1-self.R2+self.x0):
                        dI1=self.I1
                        dI2=self.I2
               
        if self.y1>=self.y0 and self.x1>(-self.R1+self.R2+self.x0) and self.x1<(self.R1-self.R2+self.x0):
                        dI1=self.I1
                        dI2=0
               
    
        if self.y1<self.y0 and self.x1>(-self.R1+self.R2+self.x0) and self.x1<(self.R1-self.R2+self.x0):
                        dI2=self.I2
                        dI1=(1-self.S2/self.S1)*self.I1

               
        I=dI1+dI2

                
        self.b[1][self.j] = I
                

                
        Is=str(self.b[1][self.j])
        ts=str(self.t)
        x11=str(self.x1)
        y11=str(self.y1)
            
        self.my_file.write(ts+'          '+Is+'          '+x11+'          '+y11+'\n')
    def onStart(self) :
        
        self.t=0.0
        self.timer.start()
        self.b = [[0] * 1000 for i in range(2)]
        self.I1=PI*self.R1*self.R1*sigma*self.T1*self.T1*self.T1*self.T1
        self.I2=PI*self.R2*self.R2*sigma*self.T2*self.T2*self.T2*self.T2
        
        self.S1=PI*self.R1*self.R1
        self.S2=PI*self.R2*self.R2

        self.I0=self.I1+self.I2

        self.x0=395
        self.y0=0
        self.j=0
        self.my_file = open('Algol.txt', 'w')

    def onStop(self) :
        self.timer.stop()
        self.my_file.close()
    


app = QtWidgets.QApplication(sys.argv)

widget = Animation()
widget.show()
sys.exit(app.exec_())  