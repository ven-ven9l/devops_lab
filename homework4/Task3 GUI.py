import sys
import psutil
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QMainWindow, QSizePolicy, QMessageBox, QWidget, QPushButton)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import threading
import json
import logging
logging.basicConfig(level=logging.DEBUG)

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, mas=[]):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.axes.set_title('CPU util graph')
        self.plot(mas)

    def plot(self, v_util):
        data = v_util
        self.axes.plot(data, 'r-')
        self.draw()


class Dialog(QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        self.layout = QFormLayout()
        self.formGroupBox = QGroupBox()
        self.w = [str(psutil.cpu_times().user / 1024)[0:5]]
        self.cpu = QLabel("0")
        self.layout.addRow(QLabel("CPU:"), self.cpu)
        self.mem = QLabel("0:")
        self.layout.addRow(QLabel("Memory:"), self.mem)
        self.net = QLabel("Network:")
        self.layout.addRow(QLabel("Network:"), self.net)
        self.io = QLabel("IO")
        self.layout.addRow(QLabel("IO:"), self.io)
        self.btn1 = QPushButton('Refresh', self)
        self.layout.addRow(self.btn1)
        self.btn1.clicked.connect(self.setStats)
        self.c = QComboBox()
        self.c.addItem("json")
        self.c.addItem("txt")
        self.layout.addRow(QLabel("Format: "), self.c)
        self.btn2 = QPushButton('Snapshot', self)
        self.layout.addRow(self.btn2)
        self.stat = QLabel("")
        self.layout.addRow(self.stat)
        self.btn2.clicked.connect(self.snapshot)
        self.formGroupBox.setLayout(self.layout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Sys stats")

        self.left = 10
        self.top = 10
        self.title = 'Task 3 - System stats'
        self.width = 540
        self.height = 695

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m = PlotCanvas(self, width=5, height=4, mas=self.w)
        self.m.move(20, 275)

        self.show()

    def setStats(self):
        v_cpu = str(psutil.cpu_times().user / 1024)[0:5]
        self.cpu.setText(v_cpu + " %")
        v_mem = str(psutil.virtual_memory().used / 1024 / 1024)[0:6]
        self.mem.setText(v_mem + " mb")
        v_net = str(psutil.net_io_counters().bytes_recv / 1024 / 1024)[0:8]
        self.net.setText(v_net + " mb")
        v_io = str(psutil.disk_usage('/').percent)
        self.io.setText(v_io + " %")
        self.w.append(v_cpu)
        #logging.debug(self.w)
        self.m.plot(self.w)

    def snapshot(self):
        f = str(self.c.currentText())
        if f == 'json':
            data = {
                'CPU': str(psutil.cpu_times().user / 1024)[0:5],
                'MEM': str(psutil.virtual_memory().used / 1024 / 1024)[0:6],
                'NET': str(psutil.net_io_counters().bytes_recv / 1024 / 1024)[0:8],
                'IO': str(psutil.disk_usage('/').percent)
            }
            file = open("snapshot.json", 'a')
            file.write(json.dumps([data], sort_keys=False, separators=(', ', ': ')) + "\n")
            file.close()
        if f == 'txt':
            data = ' CPU ' + str(psutil.cpu_times().user / 1024)[0:5] + \
                   ' MEM ' + str(psutil.virtual_memory().used / 1024 / 1024)[0:6] + \
                   ' NET ' + str(psutil.net_io_counters().bytes_recv / 1024 / 1024)[0:8] + \
                   ' IO ' + str(psutil.disk_usage('/').percent)
            file = open("snapshot.txt", 'a')
            file.write(data + "\n")
            file.close()

        self.stat.setText("OK " + str(data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()


    def work():
        z = threading.Timer(2, work).start()
        dialog.setStats()
    work()

    sys.exit(dialog.exec_())
