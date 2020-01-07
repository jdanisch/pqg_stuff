# -*- coding: utf-8 -*-

import pyqtgraph as pg
import numpy as np
import sys

app = pg.QtGui.QApplication([])
win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')
win.resize(1000,600)

plot = win.addPlot()#title="Plotting with symbols")
plot.addLegend()
plot.plot([0, 1, 2, 3, 4], pen=(0,0,200), symbolBrush=(0,0,200),
          symbolPen='w', symbol='o', symbolSize=14, name="symbol='o'")

win.show()
sys.exit(app.exec_())
##pg.QtGui.QApplication.instance().exec_()
