# -*- coding: utf-8 -*-

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np
import sys


app = QtWidgets.QApplication(sys.argv)

win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')

# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 100
# Remove chunks after we have 10
maxChunks = 10
startTime = pg.ptime.time()
p5 = win.addPlot(colspan=2)
p5.setLabel('bottom', 'Time', 's')
p5.setXRange(-10, 0)
curves = []
data5 = np.empty((chunkSize+1,2))
ptr5 = 0

p5.showAxis('right')  # set attributes of chart
p5.hideAxis('left')
p5.showGrid(x=True,y=True,alpha=1.0)
#p5.addLine(y=10)
def update3():
    global p5, data5, ptr5, curves
    now = pg.ptime.time()
    for c in curves:
        c.setPos(-(now-startTime), 0)
    
    i = ptr5 % chunkSize
    if i == 0:
        curve = p5.plot()
        curves.append(curve)
        last = data5[-1]
        data5 = np.empty((chunkSize+1,2))        
        data5[0] = last
        while len(curves) > maxChunks:
            c = curves.pop(0)
            p5.removeItem(c)
    else:
        curve = curves[-1]
    data5[i+1,0] = now - startTime
    data5[i+1,1] = np.random.normal()
    curve.setData(x=data5[:i+2, 0], y=data5[:i+2, 1])
    ptr5 += 1



timer = QtCore.QTimer()
timer.timeout.connect(update3)
timer.start(50)

win.show()
sys.exit(app.exec_())
