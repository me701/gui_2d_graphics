# Based on Martin Fitzpatrick, Listing 194

# Basic Matplotlib-based plotting widget

import sys

from PyQt5.QtWidgets import QApplication


import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure 

matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvasQTAgg) :

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
  
    def plot(self, x, y) :
        self.axes.clear()
        self.axes.plot(x, y)


if __name__ == '__main__':

    import numpy as np
    x = np.linspace(0, 10, 100)
    y = np.cos(x)

    app = QApplication(sys.argv)
    widget = MplCanvas()
    widget.plot(x, y)
    widget.show()
    sys.exit(app.exec_())

