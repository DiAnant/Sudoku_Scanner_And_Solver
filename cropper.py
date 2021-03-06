""" 
CURRENTLY NOT USING THIS CROPPER.PY FILE BUT CAN BE USED IN FUTURE.
"""

import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QApplication, QRubberBand


class QExampleLabel (QLabel):
    def __init__(self, parentQWidget=None):
        super(QExampleLabel, self).__init__(parentQWidget)
        self.initUI()

    def initUI(self):
        self.setPixmap(QtGui.QPixmap('image.jpg'))

    def mousePressEvent(self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QRubberBand(
            QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(
            QtCore.QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent(self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QtCore.QRect(
            self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent(self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        cropQPixmap = self.pixmap().copy(currentQRect)
        cropQPixmap.save('output.png')


if __name__ == '__main__':
    myQApplication = QApplication(sys.argv)
    myQExampleLabel = QExampleLabel()
    myQExampleLabel.show()
    sys.exit(myQApplication.exec_())
