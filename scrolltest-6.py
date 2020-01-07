import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class GUI(QWidget, Ui_DynoTest1):
    def __init__(self, parent=None):
        [...]
        self.torque = []
        self.horse_power = []
        self.time = []
        self.counter = 0
        [...]
        self.p1 = self.plot.plotItem
        self.p1.setLabels(left='Torque', bottom='Time')
        # self.p1.setLabel('bottom', 'Time', units="samples")
        [...]

    def onDataChanged(self, Force, RPM, Max_RPM, Torque, Max_Torque,
                      HorsePower, Max_HorsePower, Run_Time):
        [...]
        if self.counter < 50:
            self.torque.append(Torque)
            self.horse_power.append(HorsePower)
            self.time.append(Run_Time)
        else:
            self.torque = self.torque[1:] + [Torque]
            self.horse_power = self.horse_power[1:] + [HorsePower]
            self.time = self.time[1:] + [Run_Time]
        self.HorsePowerCurve.setData(self.time, self.horse_power)
        self.TorqueCurve.setData(np.array(self.time), self.torque)
        self.updateViews()
