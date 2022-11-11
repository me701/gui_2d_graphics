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
from PyQt5.QtCore import Qt 

#sys.path.append("../embedded_graphs")
#from layout_colorwidget import Color 
#from mpl_plot import MplCanvas

from paint import Canvas

import numpy as np

class RunPlotter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        openAct = QAction('&Save', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Save file')
        openAct.triggered.connect(self.save_file)

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
        self.table = QTableWidget(10, 2)

        ## Create the "canvas" widget
        self.imgfile = "data.png"
        self.canvas = Canvas(self.imgfile, parent=self)

        ## Create a button to plot and clear.
        self.button_transfer = QPushButton("Transfer Data")
        self.button_clear = QPushButton("Clear Data")
        self.button_transfer.clicked.connect(self.transfer_data)
        self.button_clear.clicked.connect(self.clear_data)

        #--------------------------#
        #  Spread   | pretty       |
        #  Sheet    |    picture   |
        #           |--------------|
        #           | plot | clear |
        # -------------------------#

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_transfer)
        button_layout.addWidget(self.button_clear)

        right_side_layout = QVBoxLayout()
        right_side_layout.setAlignment(Qt.AlignTop)
       
        right_side_layout.addWidget(self.canvas)
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
        message+= "© 2022 the powers that be."
        box.setText(message)
        box.show()

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, 'Open file')[0]
        # Do something with the file!  Like load it and set the table.
        self.statusBar().showMessage("You chose {}".format(file_name))
        
        # Load the data with numpy, assuming CSV
        x = self._extract_column(0)
        y = self._extract_column(1)
        data = np.array([x, y]).T
        np.savetxt(file_name, data, delimiter=',')

    def transfer_data(self):
        """Take canvased data and move to the table."""
        x, y = self.canvas.points()
        self.table.setRowCount(len(x))
        self._set_column(0, x)
        self._set_column(1, y)

    def clear_data(self):
        """Clear the table and the lines."""
        self.table.clearContents()
        self.canvas.clear()
       
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