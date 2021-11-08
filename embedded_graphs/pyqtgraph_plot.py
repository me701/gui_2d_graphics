import sys

from PyQt5.QtWidgets import QApplication

from PyQt5 import QtWidgets 
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot 



class PyQtGraphCanvas(PlotWidget):

    def __init__(self):
        super().__init__()

if __name__ == '__main__':

    import numpy as np
    x = np.linspace(0, 10, 100)
    y = np.cos(x)

    app = QApplication(sys.argv)
    widget = PyQtGraphCanvas()
    widget.plot(x, y)
    widget.show()
    sys.exit(app.exec_())

