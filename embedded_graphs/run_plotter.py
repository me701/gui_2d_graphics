"""
Simple GUI that loads data into a two-column spreadsheet and allows
the user the plot it.
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication,
    QMessageBox, QFileDialog, QTableWidget, QHBoxLayout, QVBoxLayout, 
    QWidget, QPushButton)
from PyQt5.QtGui import  QIcon, QPixmap

from layout_colorwidget import Color 

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
        self.plot = Color("red")
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
        file_name = QFileDialog.getOpenFileName(self, 'Open file')
        # Do something with the file!  Like load it and set the table.
        self.statusBar().showMessage("You chose {}".format(file_name))

    def update_plot(self):
        pass 

    def clear_plot(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RunPlotter()
    main.show()
    sys.exit(app.exec_())