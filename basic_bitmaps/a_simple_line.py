# based on MF listing 118

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtGui import (QPixmap, QPainter, QFont)
from PyQt5.QtCore import Qt 


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # QLabel is chosen as the central widget because
        # it contains the pixmap attribute.
        self.setWindowTitle("The Ring to Rule Them All.")
        self.label = QLabel()
        canvas = QPixmap(500, 100)

        canvas.load("./map.png")
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        # draw the path
        painter.setPen(Qt.red)
        p = painter.pen()
        painter.drawLine(300, 300, 950, 600)
        # make the title
        painter.setPen(Qt.blue)
        font = QFont()
        font.setFamily("Times")
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)
        painter.drawText(100, 100, "The Path")
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
