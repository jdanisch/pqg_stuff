import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import collections
import numpy as np

class CandlestickItem(pg.GraphicsObject):
    data = []
    def __init__(self):
        pg.GraphicsObject.__init__(self)
        self.picture = QtGui.QPicture()
     
    def setData(self, toclh):
        # toclh is a tuple of (time, open, close, min, max)
        self.data.append(toclh)

        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))

        w = 1./3.

        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
        self.update() 


    def paint(self, p, *args):

        p.drawPicture(0, 0, self.picture)
   
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)

        return QtCore.QRectF(self.picture.boundingRect())

data = [  ## fields are (time, open, close, min, max).

    (1., 10, 13, 5, 15),
    (2., 13, 17, 9, 20),
    (3., 17, 14, 11, 23),
    (4., 14, 15, 5, 19),
    (5., 15, 9, 8, 22),
    (6., 9, 15, 8, 16),
    (7., 10, 13, 5, 15),
    (8., 13, 17, 9, 20),
    (9., 17, 14, 11, 23),
    (10., 14, 15, 5, 19),
    (11., 15, 9, 8, 22),
    (12., 9, 15, 8, 16),
]


class DynamicPlotter():
    def __init__(self, sampleinterval, timewindow, size=(600,350)):
        # Data stuff
        self.tick_idx = 0
        self._bufsize = int(timewindow/sampleinterval)
        self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.x = np.linspace(0.0, timewindow, self._bufsize)
        self.y = np.zeros(self._bufsize, dtype=np.float)
        # Candlestick data
        self.candlestick_item = CandlestickItem()
        # PyQtGraph stuff
        self.app = QtGui.QApplication([])
        self.plt = pg.plot(title='Plot Viewer')
        self.plt.resize(*size)
        self.plt.showGrid(x=True, y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')
        self.plt.setXRange(0.,timewindow)
        self.plt.setYRange(0.,30)
        self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
        self.plt.addItem(self.candlestick_item)


        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(1000)


    def updateplot(self):
        if(self.tick_idx < len(data)):
            self.candlestick_item.setData(data[self.tick_idx])
            self.databuffer.appendleft( 1.0 )
            self.y[:] = self.databuffer
            self.curve.setData(self.x, self.y)
            self.tick_idx += 1
        self.app.processEvents()


    def run(self):
        self.app.exec_()


if __name__ == '__main__':
    m = DynamicPlotter(sampleinterval=1., timewindow=7.)
    m.run() 
