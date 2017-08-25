#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from infoPannel import InfoPannel
from messagePannel import MessagePannel
class OperationPannel(QSplitter):
    def __init__(self, parent=None):
        super(OperationPannel, self).__init__(parent)
        self.info_pannel=InfoPannel()
        self.message_pannel=MessagePannel()
        self.info_pannel.setParent(self)
        self.message_pannel.setParent(self)

    def showInitMessagePannel(self):
        self.info_pannel.hide()
        self.message_pannel.showNoneBackground()
    def showMessageInOut(self):
        self.info_pannel.hide()
        self.message_pannel.showMessageInOut()
    def showUserInfo(self,item):
        self.message_pannel.hide()
        self.info_pannel.showUserInfo(item)