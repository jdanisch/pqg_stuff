import sys

from PyQt5 import QtCore, QtWidgets

from pyqtgraph import (
    mkBrush,
    mkPen,
    GraphicsObject,
    QtGui,
    PlotWidget,
)


class SquareItem(GraphicsObject):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'FF0', 'AA0', '0AA']
    def __init__(self):
        super().__init__()
        self.mColor = SquareItem.colors[0]

    def paint(self, p, *args):
        p.setBrush(mkBrush(self.mColor))
        p.setPen(mkPen(None))
        p.drawRect(self.boundingRect())

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 1, 1)

    def update_draw(self, x):
        self.mColor = SquareItem.colors[x]
        self.update()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Micromouse maze simulator')
        self.resize(600, 600)

        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        self.graphics = PlotWidget()
        self.graphics.setAspectLocked()
        self.item = SquareItem()
        self.graphics.addItem(self.item)

        self.graphics.setRange(rect=QtCore.QRectF(-10, -10, 20, 20))

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(10)
        self.slider.setRange(0, 10)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider.valueChanged.connect(self.item.update_draw)
        self.slider.setValue(1)

        layout.addWidget(self.graphics)
        layout.addWidget(self.slider)

        self.setCentralWidget(frame)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
