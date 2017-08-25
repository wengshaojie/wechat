# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sun Aug 13 17:40:27 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, Qt ,QtGui
from PyQt4.QtGui import *

from PyQt4.Qt import *

from PyQt4.QtCore import *
import sys,os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(QtGui.QWidget):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
    def __init__(self, parent=None):
        super(Ui_Login, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.resize(280, 400)
        self.setStyleSheet('background-color:#f5f5f5;')
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 68, 280, 190))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setAlignment(Qt.AlignCenter)

        self.label4 = QtGui.QLabel(self)
        self.label4.setGeometry(QtCore.QRect(260, 8,14,14))
        self.label4.setObjectName(_fromUtf8("label"))
        self.label4.setStyleSheet("QLabel{background-image:url(img/close.png);}")
        self.label4.mousePressEvent=sys.exit

        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(0, 300, 280, 41))
        font = QtGui.QFont()
        self.label_2.setAlignment(Qt.AlignCenter)
        font.setPointSize(10)
        self.label_2.setStyleSheet('color:#999999;font-weight:500') 
        self.label_2.setFont(font)

        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setStyleSheet('color:#444444;font-weight:500') 
        self.label_3.setFont(font)
        self.label_3.setText(_translate("Dialog", u"微信(增强版)", None))
        self.label_3.setObjectName(_fromUtf8("label_2"))
        self.updateLabelUi("请使用微信扫一扫以登陆")

        QtCore.QMetaObject.connectSlotsByName(self)
    def updateImageUi(self,path,widht,height):
        #self.label.setPixmap(QPixmap(os.path.join('dist','QR.jpg')))
        image=QImage()
        image.load(path)
        self.label.setPixmap(QPixmap.fromImage(image).scaled(widht,height))
  


    def updateLabelUi(self, msg):
        #Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.label_2.setText(_translate("Dialog",msg , None))

if __name__=='__main__':
    app = QApplication(sys.argv)
    pchat = Ui_Login()
    pchat.show()
    sys.exit(app.exec_())