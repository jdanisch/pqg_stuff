# -*- coding: utf-8 -*-

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np
import sys


app = QtWidgets.QApplication(sys.argv)

win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')

p1 = win.addPlot()
#p2 = win.addPlot()
data1 = np.random.normal(size=300)
curve1 = p1.plot(data1)
#curve2 = p2.plot(data1)
ptr1=0

def update1():
    global data1, ptr1
    data1[:-1] = data1[1:]
    data1[-1] = np.random.normal()
    ptr1 += 1
    curve1.setData(data1)
    curve1.setPos(ptr1,10)

    #curve2.setData(data1)
    #curve2.setPos(ptr1, 0)
    
timer = QtCore.QTimer()
timer.timeout.connect(update1)
timer.start(50)

win.show()
sys.exit(app.exec_())
