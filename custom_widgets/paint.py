# based on MF listing 123

import sys

from PyQt5.QtWidgets import (QApplication, QLabel)
from PyQt5.QtGui import (QPixmap, QPainter)
from PyQt5.QtCore import Qt 


class Canvas(QLabel):

    def __init__(self, img=None, parent=None):
        super().__init__(parent)
        self.initialize_pixmap(img)
        self.pen_color = Qt.red 
        self._x = [] 
        self._y = []

    def initialize_pixmap(self, img):
        self.img = img
        if self.img == None:
            pixmap = QPixmap(600, 300)
            pixmap.fill(Qt.white)
        else:
            pixmap = QPixmap(self.img)
        self.setPixmap(pixmap)

    def points(self):
        return self._x, self._y

    def mouseMoveEvent(self, e):
        if len(self._x) == 0:
            self._x.append(e.x())
            self._y.append(e.y())
            return
        painter = QPainter(self.pixmap())
        p = painter.pen() 
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self._x[-1], self._y[-1], e.x(), e.y())
        painter.end()
        self.update()
        self._x.append(e.x())
        self._y.append(e.y())

    def mouseReleaseEvent(self, e):
        self.pen_lifted = True

    def clear(self):
        self._x = [] 
        self._y = []
        self.initialize_pixmap(self.img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Canvas()
    widget.show()
    app.exec_()
