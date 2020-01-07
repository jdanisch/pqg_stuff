# -*- coding: utf-8 -*-

import pyqtgraph as pg
import numpy as np
import sys

#app = pg.QtGui.QApplication([])

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
pg.plot(x, y, pen=None, symbol='o')


##sys.exit(app.exec_())
pg.QtGui.QApplication.instance().exec_()
