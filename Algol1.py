
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
        self.k=1
        
        
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
        
    def onStart(self) :
        
       self.t=0.0
       self.timer.start()
       
        
    def onStop(self) :
        self.timer.stop()
         
    

class Chlenkita():
        
        
        a = [[0] * 1000 for i in range(2)]
        t=0.0
        sigma=1
        R1=70
        R2=20
        T1=3000
        T2=5000
        
        I1=PI*R1*R1*sigma*T1*T1*T1*T1
        I2=PI*R2*R2*sigma*T2*T2*T2*T2
        
        S1=PI*R1*R1
        S2=PI*R2*R2
        
        T14=T1*T1*T1*T1
        T24=T2*T2*T2*T2
        I0=I1+I2
        
        x0=395
        #y0=200+R1
        y0=0
        print(x0)
        print(y0)
        
        my_file = open('snake.txt', 'w')
        
        for j in range(1000):
            
            a[0][j] = t
            t+=0.01
            
            x1=200*ma.cos(t)+x0
            y1=200*ma.sin(t)+y0
            
            x2=(4*x1**3-4*x1*x1*x0-ma.sqrt(((4*x1**3+4*x1*x1*x0-4*x1*y0*y0+8*x1*y0*y1+4*x1*x0*x0-4*x1*y1*1+4*x1*R2*R2-4*x1*R1*R1-4*y0*y0*x0+8*y0*x0*y1-4*x0**3-4*x0*y1*y1-4*x0*R2*R2+4*x0*R1*R1)**2-4*(4*x1*x1-8*x1*x0+4*y0*y0-8*y0*y1+4*x0*x0+4*y1*y1)*(x1**4+2*x1*x1*y0*y0-4*x1*x1*y0*y1-2*x1*x1*x0*x0+2*x1*x1*y1*y1-2*x1*x1*R2*R2+2*x1*x1*R1*R1+y0**4-4*y0**3*y1+y0*y0*x0*x0+6*y0*y0*y1*y1-2*y0*y0*R2*R2-2*y0*y0*R2*R2-2*y0*y0*R1*R1-4*y0*x0*x0*y1-4*y0*y1**3+4*y0*y1*R2*R2+4*y0*y1*R1*R1+x0**4+2*x0*x0*y1*y1+2*x0*x0*R2*R2-2*x0*x0*R1*R1+y1**4-2*y1*y1*R2*R2-2*y1*y1*R1*R1+R2**4-2*R2*R2*R1*R1+R1**4)))+4*x1*y0-8*x1*y0*y1-4*x1*x0*x0+4*x1*y1*y1-4*x1*R2*R2+4*x1*R1*R1+4*y0*y0*x0-8*y0*x0*y1+4*x0**3+4*x0*y1*y1+4*x0*R2*R2-4*x0*R1*R1)/(2*(4*x1*x1-8*x1*x0+4*y0*y0-8*y0*y1+4*x0*x0+4*y1*y1))

            l1=ma.fabs(x2-x0)
            l2=ma.fabs(x2-x1)
            if l1<=R1 and l2<=R2:
                S11=R1*R1*ma.fabs(ma.acos(l1/R1))
                S12=l1*ma.sqrt(R1*R1-l1*l1)
                S21=R2*R2*ma.fabs(ma.acos(l2/R2))
                S22=l2*ma.sqrt(R2*R2-l2*l2)
                S01=S11-S12
                S02=S21-S22
                
                if x1>(R1+R2+x0) or x1<(-R1-R2+x0):
                        dI1=I1
                        dI2=I2
                if y1>=y0 and x1>(R1+x0) and x1<(R1+R2+x0):
                        dI1=I1
                        dI2=(1-(S01+S02)/S2)*I2
                if y1>=y0 and x1>(R1-R2+x0) and x1<(R1+x0):
                        dI1=I1
                        dI2=ma.fabs(S01-S02)/S2*I2
                if y1>=y0 and x1>(-R1+R2+x0) and x1<(R1-R2+x0):
                        dI1=I1
                        dI2=0
                if y1>=y0 and x1>(-R1+x0) and x1<(-R1+R2+x0):
                        dI1=I1
                        dI2=ma.fabs(S01-S02)/S2*I2
                if y1>=y0 and x1>(-R1-R2+x0) and x1<(-R1+x0):
                        dI1=I1
                        dI2=(1-(S01+S02)/S2)*I2
    
                if y1<y0 and x1>(R1+x0) and x1<(R1+R2+x0):
                        dI2=I2
                        dI1=(1-(S01+S02)/S1)*I1
                if y1<y0 and x1>(R1-R2+x0) and x1<(R1+x0):
                        dI2=I2
                        dI1=(1-ma.fabs(S01-S02))/S1*I1
                if y1<y0 and x1>(-R1+R2+x0) and x1<(R1-R2+x0):
                        dI2=I2
                        dI1=(1-S2/S1)*I1
                if y1<y0 and x1>(-R1+x0) and x1<(-R1+R2+x0):
                        dI2=I2
                        dI1=(1-ma.fabs(S01-S02))/S1*I1
                if y1<y0 and x1>(-R1-R2+x0) and x1<(-R1+x0):
                        dI2=I2
                        dI1=(1-(S01+S02)/S1)*I1
                I=dI1+dI2
                print('I1')
                print(dI1/I1)
                print('I2')
                print(dI2/I2)

                
                a[1][j] = I
                
            else:
                I=I0

                a[1][j] = I
                
            Is=str(a[1][j])
            ts=str(t)
            x11=str(x1)
            y11=str(y1)
            x22=str(x2)
            my_file.write(ts+'          '+Is+'          '+x11+'          '+y11+'          '+x22+'\n')

       # for row in a:
          # print(' '.join([str(elem) for elem in row]))
           
        my_file.close()
        
app = QtWidgets.QApplication(sys.argv)

widget = Animation()
widget.show()
sys.exit(app.exec_())  