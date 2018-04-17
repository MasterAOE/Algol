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
        self.resize(700, 8000)
        self.setWindowTitle('Circ')
        
        self.buttonStart = QtWidgets.QPushButton("Start",self)
        self.buttonStart.move(30,160)
        self.buttonStart.clicked.connect(self.onStart)

        self.buttonStop = QtWidgets.QPushButton("Stop",self)
        self.buttonStop.move(30,190)
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
        
        
        
        qp.drawEllipse(395,200,70,70)
        qp.drawEllipse(595+self.x1,225+self.y1,20,20)
        
        qp.end()

        
    def onTimer(self) :
        
        self.t+=0.1
       
        self.update()
        
    def onStart(self) :
        
       11 
        
    def onStop(self) :
        self.timer.stop()
        
app = QtWidgets.QApplication(sys.argv)
widget = Animation()
widget.show()
sys.exit(app.exec_())  

        
        
 
    
    
    
    
    
