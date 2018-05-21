# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:04:17 2018

@author: olegi
"""
import math as ma

l1=ma.fabs(x2-x0)
l2=ma.fabs(x2-x1)
if l1<=R1 and l2<=R2:
    S11=R1*R1*ma.fabs(ma.acos(l1/R1))
    S12=l1*ma.sqrt(R1*R1-l1*l1)
    S21=R2*R2*ma.fabs(ma.acos(l2/R2))
    S22=l2*ma.sqrt(R2*R2-l2*l2)
    S01=S11-S12
    S02=S21-S22
        if ma.fabs(x1)>(R1+R2+x0):
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