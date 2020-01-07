import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap('icon-mongol.jpg'))
    
    l1.setText('Yo Man')
    w.setWindowTitle('kukujiao')
    w.setWindowIcon(QtGui.QIcon("icon-mongol.jpg"))

    w.setGeometry(100, 100, 300, 200)
    l1.move(100, 20)
    l2.move(100, 50)

    w.show()
    sys.exit(app.exec_())

window()
