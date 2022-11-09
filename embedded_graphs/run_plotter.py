"""
Simple GUI that loads data into a two-column spreadsheet and allows
the user the plot it.
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication,
    QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QVBoxLayout, 
    QWidget, QPushButton)
from PyQt5.QtGui import  QIcon, QPixmap

from layout_colorwidget import Color 

from mpl_plot import MplCanvas

import numpy as np

class RunPlotter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        openAct = QAction('&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file')
        openAct.triggered.connect(self.load_file)

        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        aboutAct = QAction('&About', self)
        aboutAct.setShortcut('Ctrl+A')
        aboutAct.setStatusTip('About!')
        aboutAct.triggered.connect(self.about_message)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addAction(exitAct)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAct)

        ## Create the spreadsheet
        self.table = QTableWidget(100, 2)

        ## Create the "plot" widget
        self.plot = MplCanvas()

        # Provide a default graph
        x = np.linspace(0, 10, 100)
        y = np.cos(x)
        self.plot.plot(x, y)
        self.plot.show()
        self.plot.setFixedSize(400,400)

        ## Create a button to plot and clear.
        self.button_plot = QPushButton("Plot")
        self.button_clear = QPushButton("Clear")
        self.button_plot.clicked.connect(self.update_plot)
        self.button_clear.clicked.connect(self.clear_plot)

        #--------------------------#
        #  Spread   | pretty       |
        #  Sheet    |    picture   |
        #           |--------------|
        #           | plot | clear |
        # -------------------------#

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_plot)
        button_layout.addWidget(self.button_clear)

        right_side_layout = QVBoxLayout()
        right_side_layout.addWidget(self.plot)
        right_side_layout.addLayout(button_layout)

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(right_side_layout)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def about_message(self):
        box = QMessageBox(self)
        message = "This is a text.\n\n"
        message+= "Nothing to see here.\n\n"
        message+= "© 2021 the powers that be."
        box.setText(message)
        box.show()

    def load_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')[0]
        # Do something with the file!  Like load it and set the table.
        self.statusBar().showMessage("You chose {}".format(file_name))
        
        # Load the data with numpy, assuming CSV
        x, y = np.loadtxt(file_name, delimiter=',', unpack=True)
        self._set_column(0, x)
        self._set_column(1, y)

    def update_plot(self):
        """Update the plot with whatever data lives in the table.

        Note, check out 
          https://www.pythonguis.com/tutorials/plotting-matplotlib/
        for more on updating Matplotlib plots.

        Here, we use the "clear" then "draw" approach.
        """

        # Extract data from table
        x = self._extract_column(0)
        y = self._extract_column(1)
        #x = np.linspace(0, 10, 100)
        #y = np.sin(x)

        # Update the plot
        self.plot.axes.cla()
        self.plot.axes.plot(x, y, 'r')
        self.plot.draw()

    def clear_plot(self):
        self.plot.axes.clear()
        self.plot.draw()

    def _extract_column(self, j):
        """Extract values from column j as np array.
        
        Note, the underscore prefix suggests that this is a method to be 
        used only inside this class, i.e., it isn't part of the interface
        for users.
        """
        n = self.table.rowCount()
        vals = []
        for i in range(n):
            # quit if we've hit an empty cell.  assume
            # no data after this cell.
            if self.table.item(i, j).text() == "":
                break
            vals.append(float(self.table.item(i, j).text()))
        return np.array(vals) 

    def _set_column(self, j, vals):
        """Set column j to vals."""
        n = len(vals)
        self.table.setRowCount(n)
        for i in range(n):
            self.table.setItem(i, j, QTableWidgetItem(str(vals[i])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RunPlotter()
    main.show()
    sys.exit(app.exec_())