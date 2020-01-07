import pyqtgraph as pg
import numpy as np
x = np.arange(100)
y = np.random.normal(size=(3, 100))
plotWidget = pg.plot(title="Three plot curves")
for i in range(3):
    ## setting pen=(i,3) automaticaly creates three different-colored pens
    plotWidget.plot(x, y[i], pen=(i,3))  
    
## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
