import pyqtgraph as pg
##from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import QtCore, QtGui
import numpy as np
from time import sleep

win = pg.GraphicsWindow()
win.setWindowTitle('Sliding Window Test')
win.setWindowIcon(QtGui.QIcon("icon-mongol.jpg"))

p1 = win.addPlot()
p1.setLabels(left='Large Range')

## create third ViewBox.
## this time we need to create a new axis as well.
p3 = pg.ViewBox()
ax3 = pg.AxisItem('right')
p1.layout.addItem(ax3, 2, 3)
p1.scene().addItem(p3)
ax3.linkToView(p3)
p3.setXLink(p1)
ax3.setZValue(-10000)
ax3.setLabel('Small Range', color='#ff0000')

win.nextRow()
p5 = win.addPlot()
p5.setLabels(left='Large Range')

## create third ViewBox.
## this time we need to create a new axis as well.
p7 = pg.ViewBox()
ax7 = pg.AxisItem('right')
p5.layout.addItem(ax7, 2, 3)
p5.scene().addItem(p7)
ax7.linkToView(p7)
p7.setXLink(p5)
ax7.setZValue(-10000)
ax7.setLabel('Small Range', color='#ff0000')

## Handle view resizing
def updateViews():
    ## view has resized; update auxiliary views to match
    global p1, p3, p5, p7
    p3.setGeometry(p1.vb.sceneBoundingRect())

    p7.setGeometry(p5.vb.sceneBoundingRect())

    ## need to re-update linked axes since this was called
    ## incorrectly while views had different shapes.
    ## (probably this should be handled in ViewBox.resizeEvent)
    p3.linkedViewChanged(p1.vb, p3.XAxis)

    p7.linkedViewChanged(p5.vb, p7.XAxis)

updateViews()
p1.vb.sigResized.connect(updateViews)
p5.vb.sigResized.connect(updateViews)


data1 = []
data3 = []

curve1 = p1.plot()
curve3 = pg.PlotCurveItem(pen='r')
p3.addItem(curve3)

curve5 = p5.plot()
curve7 = pg.PlotCurveItem(pen='r')
p7.addItem(curve7)

data1 = [1000.0*r - 400 for r in np.random.random(size=600)]
data3 = [1.5*r for r in np.random.random(size=600)]

p1.setRange(yRange=(-400, 600))
p3.setRange(yRange=(0, 1.5))

p5.setRange(yRange=(-400, 600))
p7.setRange(yRange=(0, 1.5))

timer = pg.QtCore.QTimer()
r = 0
def update():
    global timer
    global r
    if r > 50:
        curve1.setData(data1[r-50:r])
        curve3.setData(data3[r-50:r])
        curve1.setPos(r - 50, 0)
        curve3.setPos(r - 50, 0)
    else:
        curve1.setData(data1[:r])
        curve3.setData(data3[:r])

    curve5.setData(data1[:r])
    curve7.setData(data3[:r])

    r +=1
    if r >= 600:
        timer.stop()

timer.timeout.connect(update)
timer.start(100)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
