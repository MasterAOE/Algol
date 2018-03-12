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

class Lab119(QtWidgets.QMainWindow) :

    def __init__(self) :
        QtWidgets.QMainWindow.__init__(self)
        self.resize(1000, 550)
        self.setWindowTitle('Затменно-двойная система')
        
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
        self.buttonStart.move(20,390)
        self.buttonStart.clicked.connect(self.onStart)

        self.pbOK=QtWidgets.QPushButton(self);
        self.pbOK.setText('OK');
        self.pbOK.move(20,430);
        self.pbOK.clicked.connect(self.onOK)

        self.buttonStop = QtWidgets.QPushButton("Stop",self)
        self.buttonStop.move(20,470)
        self.buttonStop.clicked.connect(self.onStop)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.onTimer)

        
        self.t1=0
        
        a_str = self.parama1.text() 
        self.a=0;

        a=float(str(a_str)) 

        self.a=a;
        
        P_str = self.parama2.text() 
        self.P=0;

        P=float(str(P_str)) 

        self.P=P;
        
        self.a=0.0
        self.P=0.0
        
        self.t=0.0
        self.a1=0.0
        self.a2=0.0
        self.l=1
        self.l1=1
        self.k=0.0
        self.m=0.0
        self.v1=0.0
        self.v2=0.0
        self.A=0.0
        self.B=0.0
        self.w1=0.0
        self.w2=0.0
        self.f1=0.0
        self.f2=0.0
        self.s=0.0
        self.d=0.0
        self.x1=0.0
        self.x2=0.0
        self.x3=0.0
        self.x4=0.0
        self.x5=0.0
        self.x6=0.0
        self.x7=0.0
        self.x8=0.0
        self.x9=0.0
        self.x10=0.0
        self.x11=0.0


    def paintEvent(self,ev) :
        
       
        qp=QtGui.QPainter()
        qp.begin(self)

        h=0.01
        
    
        p01=QtCore.QPointF(400, 30)
        p1=QtCore.QPointF(400+ self.x1, 200)
        p02=QtCore.QPointF(600, 30)
        p2=QtCore.QPointF(600+ self.x2, 200)
        
        L1=30+170*(self.l1/self.l)
        
        pl1=QtCore.QPointF(400+ self.x3, L1)
        pl2=QtCore.QPointF(425+ self.x4, L1+20)
        pl3=QtCore.QPointF(450+ self.x5, L1-20)
        pl4=QtCore.QPointF(475+ self.x6, L1+20)
        pl5=QtCore.QPointF(500+ self.x7, L1-20)
        pl6=QtCore.QPointF(525+ self.x8, L1+20)
        pl7=QtCore.QPointF(550+ self.x9, L1-20)
        pl8=QtCore.QPointF(575+ self.x10, L1+20)
        pl9=QtCore.QPointF(600+ self.x11, L1)
    
        
        qp.drawEllipse(395+self.x1,200,10,10)
        qp.drawEllipse(595+self.x2,200,10,10)
        
        p3=QtCore.QPointF(300,30)
        p4=QtCore.QPointF(500,30)
        p5=QtCore.QPointF(500,30)
        p6=QtCore.QPointF(700,30)
        
        qp.drawLine(p01,p1)
        qp.drawLine(p02,p2)
        qp.drawLine(p3,p4)
        qp.drawLine(p5,p6)
        qp.drawLine(pl1,pl2)
        qp.drawLine(pl2,pl3)
        qp.drawLine(pl3,pl4)
        qp.drawLine(pl4,pl5)
        qp.drawLine(pl5,pl6)
        qp.drawLine(pl6,pl7)
        qp.drawLine(pl7,pl8)
        qp.drawLine(pl8,pl9)
        
        self.x=self.a*ma.cos(t1)
        self.y=self.b*ma.sin(t1)
        self.t=self.t1+h
        """
        p03=QtCore.QPointF(400, 530)
        p7=QtCore.QPointF(400+ self.x3, 700)
        p04=QtCore.QPointF(700, 530)
        p8=QtCore.QPointF(700+ self.x4, 700)
        
        qp.drawEllipse(395+self.x3,700,10,10)
        qp.drawEllipse(695+self.x4,700,10,10)
        
        p9=QtCore.QPointF(300,530)
        p10=QtCore.QPointF(500,530)
        p11=QtCore.QPointF(600,530)
        p12=QtCore.QPointF(800,530)
        
        qp.drawLine(p03,p7)
        qp.drawLine(p04,p8)
        qp.drawLine(p9,p10)
        qp.drawLine(p11,p12)
        """
        qp.end()


    def onTimer(self) :

        self.t+=0.01 

        
        self.update()
        
    def onOK(self) :
        
        a1_str = self.parama1.text() 
        self.a1=0;

        a1=float(str(a1_str)) 

        self.a1=a1;
        
        a2_str = self.parama2.text() 
        self.a2=0;

        a2=float(str(a2_str)) 

        self.a2=a2;
        
        self.a1=self.a1*RAD
        self.a2=self.a2*RAD
       
        self.x1=200*ma.sin(self.a1)
        self.x2=200*ma.sin(self.a2)
        
        #self.x3=200*ma.sin(self.a1)
        #self.x4=200*ma.sin(self.a2)
        
       
        self.update()

    def onStart(self) :
        
        a1_str = self.parama1.text() 
        self.a1=0;

        a1=float(str(a1_str)) 

        self.a1=a1;
        
        a2_str = self.parama2.text() 
        self.a2=0;

        a2=float(str(a2_str)) 

        self.a2=a2;
       
        l_str = self.paraml.text() 
        self.l=0;

        l=float(str(l_str)) 

        self.l=l;

        l1_str = self.paraml1.text() 
        self.l1=0;

        l1=float(str(l1_str)) 

        self.l1=l1;
        
        k_str = self.paramk.text() 
        self.k=0;

        k=float(str(k_str)) 

        self.k=k;
        
        m_str = self.paramm.text() 
        self.m=0;

        m=float(str(m_str)) 

        self.m=m;
        
        v1_str = self.paramv1.text() 
        self.v1=0;

        v1=float(str(v1_str)) 

        self.v1=v1;
        
        v2_str = self.paramv2.text() 
        self.v2=0;

        v2=float(str(v2_str)) 

        self.v2=v2;
      
        self.a1=self.a1*RAD
        self.a2=self.a2*RAD
        self.v1=self.v1*RAD
        self.v2=self.v2*RAD
        self.w1=(g/self.l)**(1/2)
        self.w2=((g/self.l)+(2*self.k*(self.l1)**2/(self.m*(self.l)**2)))**(1/2)
        self.A=(1/2)*((self.a1+self.a2)**2+(self.v1+self.v2)**2/self.w1**2)**(1/2)
        self.B=(1/2)*((self.a1-self.a2)**2+(self.v1-self.v2)**2/self.w2**2)**(1/2)
        
        
        if (v1==v2==0 or v1+v2==0):
            self.f1=PI/2
            self.f2=PI/2
        else:
            self.f1=ma.atan(self.a1+self.a2)*self.w1/(self.v1+self.v2)
            self.f2=ma.atan(self.a1-self.a2)*self.w2/(self.v1-self.v2)
            
        self.x1=self.a1
        self.x2=self.a2
        
        self.s=g/self.l
        self.d=self.k*(self.l1)**2/self.m/(self.l)**2

        self.t=0.0
        self.timer.start()

    def onStop(self) :
        self.timer.stop()

app = QtWidgets.QApplication(sys.argv)
widget = Lab119()
widget.show()
sys.exit(app.exec_())