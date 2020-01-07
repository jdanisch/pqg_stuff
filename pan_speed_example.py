from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import random
import sys

class PanSpeedExample (pg.GraphicsWindow):

    timer = QtCore.QTimer()
    
    def __init__(self):
        super(PanSpeedExample, self).__init__()
        
        #counter for keeping track of the update loop
        self.counter = 0
        
        #arrays for the plot data
        self.datax = []
        self.datay = []
        
        #creates the central plot and a curve for that plot
        self.plot1 = self.addPlot()
        self.plot1.setXRange(0, 300)
        self.plot1.enableAutoRange()
        self.plot1.setAutoPan(True)
        self.curve = self.plot1.plot(pen='r')
        
        #when the timer triggers, runs the update method
        self.timer.timeout.connect(self.update)
        
    def update(self):
        #append new data to the arrays
        self.datax.append(self.counter)
        self.datay.append(random.randint(1, 10))
        #update the curve with the new data
        self.curve.setData(self.datax, self.datay)
        #increment the counter variable to control the loop
        self.counter += 1
        if self.counter == 5000:
            self.stop_timer()
        
    def start_timer(self):
        self.timer.start(0)
        
    def stop_timer(self):
        self.timer.stop()
    
if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        win = QtGui.QMainWindow()
        ex = PanSpeedExample()
        win.setCentralWidget(ex)
        win.show()
        ex.start_timer()
        QtGui.QApplication.instance().exec_()

        
