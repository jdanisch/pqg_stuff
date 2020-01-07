import sys
##from PyQt5.QtWidgets import QApplication, QWidget
##from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
##    w.resize(250, 150)
##    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.setWindowIcon(QtGui.QIcon('icon-mongol.jpg'))
    
    w.setGeometry(100, 100, 300, 200)
    w.show()

    sys.exit(app.exec_())

window()
