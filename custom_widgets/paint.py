# based on MF listing 118

import sys

from PyQt5.QtWidgets import (QApplication, QLabel)
from PyQt5.QtGui import (QPixmap, QPainter)
from PyQt5.QtCore import Qt 


class Canvas(QLabel):

    def __init__(self):
        super().__init__()
        self.label = QLabel()
        pixmap = QPixmap(600, 300)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        
        self.last_x, self.last_y = None, None
        self.pen_color = Qt.red 

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x, self.last_y = e.x(), e.y()
            return 
        painter = QPainter(self.pixmap())
        p = painter.pen() 
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x, self.last_y = e.x(), e.y()

    def mouseReleaseEvent(self, e):
        self.last_x, self.last_y = None, None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Canvas()
    widget.show()
    app.exec_()
