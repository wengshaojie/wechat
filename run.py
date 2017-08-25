#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys,os
import thread, subprocess 
from PyQt4 import QtCore, QtGui, Qt
from login import Ui_Login
import itchat,time
from itchat import tools
from main import Ui_Main



class opertor_Login(QtCore.QThread):
    message_signal = QtCore.pyqtSignal(list)
    processes_signal = QtCore.pyqtSignal(list, int) 
    def __init__(self, parent=None):
        super(opertor_Login, self).__init__(parent)
    def setMessageSignal(self,Signal_):
        self.message_signal.connect(Signal_)
    def setProcessesSignal(self,Signal_):
        self.processes_signal.connect(Signal_)        
    def start_processes(self):
        self.start()
    def run(self):
        itchat.auto_login(self.processes_signal.emit,self.message_signal.emit)
class UIcontrol():
    def __init__(self, parent=None):
        self.ui_login = Ui_Login()
        self.ui_main = Ui_Main()
    def ProcessesSignal(self,list, number):
        if number==1:
            self.ui_login.updateImageUi(list[0],list[1],list[2])
            self.ui_login.show()
        elif number==2:
            self.ui_login.updateLabelUi(list[0])
        elif number==3:

            self.ui_main.initUserData(list)
            self.ui_login.hide()
            self.ui_main.show()
    def MessageSignal(self,list):
        self.ui_main.receiveMsg(list)  
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    weixinapp = UIcontrol()
    opertor_login_thread = opertor_Login()
    opertor_login_thread.setProcessesSignal(weixinapp.ProcessesSignal)
    opertor_login_thread.setMessageSignal(weixinapp.MessageSignal)
    opertor_login_thread.start_processes()
    sys.exit(app.exec_())
    