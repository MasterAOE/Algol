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
n = 10000
a = [[0] * n for i in range(2)]
for i in range(2):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

class Animation(QtWidgets.QMainWindow) :
    def __init__(self) :
        QtWidgets.QMainWindow.__init__(self)
        self.resize(7000, 8000)
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
        
        self.t+=1
       
        self.update()
        
    def onStart(self) :
        
       self.t=0.0
       self.timer.start()
        
    def onStop(self) :
        self.timer.stop()
        
app = QtWidgets.QApplication(sys.argv)
widget = Animation()
widget.show()
sys.exit(app.exec_())  

        
        
 
    
    
    
    
    
