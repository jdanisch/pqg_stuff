# -*- coding: utf-8 -*-
"""
Shows use of PlotWidget to display panning data

"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

app = QtGui.QApplication([])
win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: PanningPlot')
win.setWindowIcon(QtGui.QIcon("icon-mongol.jpg"))

plt = win.addPlot()
#plt.setAutoVisibleOnly(y=True)
curve = plt.plot()

data = []
count = 0
def update():
    global data, curve, count
    data.append(np.random.normal(size=10) + np.sin(count * 0.1) * 5)
    if len(data) > 100:
        data.pop(0)
    curve.setData(np.hstack(data))
    count += 1

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

win.show()

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app.instance().exec_()
