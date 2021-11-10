# based on MF listing 118

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtGui import (QPixmap, QPainter)
from PyQt5.QtCore import Qt 


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        painter.drawLine(10, 10, 300, 200)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
