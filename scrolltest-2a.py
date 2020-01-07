# -*- coding: utf-8 -*-

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np
import sys


app = QtWidgets.QApplication(sys.argv)

win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')
win.setWindowIcon(QtGui.QIcon('icon-mongol.jpg'))
# 2) Allow data to accumulate. In these examples, the array doubles in length
#    whenever it is full. 
p3 = win.addPlot()
#p4 = win.addPlot()
# Use automatic downsampling and clipping to reduce the drawing load
#p3.setDownsampling(mode='peak')
#p4.setDownsampling(mode='peak')
#p3.setClipToView(True)
#p4.setClipToView(True)
p3.setRange(xRange=[-100, 0])
p3.setLimits(xMax=0)
curve3 = p3.plot()
#curve4 = p4.plot()

data3 = np.empty(100)
ptr3 = 0

def update2():
    global data3, ptr3
    data3[ptr3] = np.random.normal()
    ptr3 += 1
    if ptr3 >= data3.shape[0]:
        tmp = data3
        data3 = np.empty(data3.shape[0] * 2)
        data3[:tmp.shape[0]] = tmp
        print(data3.shape,tmp.shape)
    curve3.setData(data3[:ptr3])
    curve3.setPos(-ptr3, 0)
    #curve4.setData(data3[:ptr3])


timer = QtCore.QTimer()
timer.timeout.connect(update2)
timer.start(50)
print(data3.shape)

win.show()
sys.exit(app.exec_())
