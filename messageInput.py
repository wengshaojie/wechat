#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from userPannel import GroupUserList
from menuPannel import MenuPannel

from flowlayout import FlowLayout
import itchat
DEFAULT_HEAD = 'self'


class TextEdit(QTextEdit,QObject):
    '''支持ctrl+return信号发射的QTextEdit'''
    entered = pyqtSignal()
    def __init__(self, parent = None):
        super(TextEdit, self).__init__(parent)
    
    def keyPressEvent(self,e):
        # print e.key() == Qt.Key_Return,e.key() == Qt.Key_Enter, e.modifiers() == Qt.ControlModifier
        if (e.key() == Qt.Key_Return) and (e.modifiers() == Qt.ControlModifier):
            self.entered.emit()# ctrl+return 输入
            self.clear()
        super(TextEdit,self).keyPressEvent(e)


'''
"QPushButton{background-color:black;color: white;border-radius: 10px;border: 2px groove gray;border-style: outset;}"
"QPushButton:hover{background-color:white; color: black;}"
"QPushButton:pressed{background-color:rgb(85, 170, 255);border-style: inset;}"
'''
class MsgInput(QWidget,QObject):
    '''自定义的内容输入控件，支持图像和文字的输入，文字输入按回车确认。'''
    textEntered = pyqtSignal(str)
    imgEntered = pyqtSignal(str)

    btnSize = 35
    teditHeight = 200
    def __init__(self,parent = None):
        super(MsgInput, self).__init__(parent)
        self.setContentsMargins(3,3,3,3)

        self.textEdit = TextEdit()
        self.textEdit.setMaximumHeight(self.teditHeight)
        self.setMaximumHeight(self.teditHeight+self.btnSize)
        self.textEdit.setFont(QFont("Times",15,QFont.Normal))
        self.textEdit.entered.connect(self.sendText)

        sendImg = QPushButton()
        sendImg.setStyleSheet("margin:0px;padding:1px;border:0px;background-image:url(img/file.png);")
        sendImg.setFixedSize(22,22)
        sendImg.clicked.connect(self.sendImage)

        sendEmoji = QPushButton()
        sendEmoji.setFixedSize(22,22)
        sendEmoji.setStyleSheet("margin:0px;padding:1px;border:0px;background-image:url(img/emoji.png);")
        sendEmoji.clicked.connect(self.toInsertEmoji)

        sendTxt = QPushButton(u'发送')
        sendTxt.setStyleSheet("QPushButton{border:1px solid #cccccc;color:cccccc}"
             "QPushButton:hover{background-color:#129611;color:while}"
             "QPushButton:pressed{background-color:#129611;;color:while}")
        sendTxt.setFixedHeight(self.btnSize)
        sendTxt.clicked.connect(self.sendText)

        hl = FlowLayout()
        hl.addWidget(sendTxt)

        hl.setMargin(2)

        h2 = FlowLayout()
        h2.addWidget(sendImg)
        h2.addWidget(sendEmoji)
        h2.setMargin(2)

        vl = QVBoxLayout()
        vl.addLayout(h2)
        vl.addWidget(self.textEdit)
        vl.addLayout(hl)

        vl.setMargin(0)
        self.setLayout(vl)
    def toInsertEmoji(self,event):
        editUser = QAction(QIcon('img/biaoqing.png'),u'',self)#第一个参数也可以给一个QIcon图标
        #editUser.triggered.connect(self.editInfo)

        delUser = QAction(QIcon('img/biaoqing.png'),u'',self)
        #delUser.triggered.connect(self._listWidgetItem.delSelfFromList)#选中就会触发

        menu = QTableWidget()
        

        menu.exec_(QCursor.pos())
    def sendImage(self):#选择图像发送
        dialog = QFileDialog(self,u'请选择图像文件...')
        dialog.setDirectory(os.getcwd() + '/ref') #设置默认路径
        dialog.setNameFilter(u"图片文件(*.png *.jpg *.bmp *.ico);;")#中间一定要用两个分号才行！
        if dialog.exec_():
            selectFileName = unicode(dialog.selectedFiles()[0])
            self.imgEntered.emit(selectFileName)
        else:#放弃选择
            pass
    def sendText(self):
        txt = self.textEdit.toPlainText()
        if len(txt)>0:
            self.textEntered.emit(txt)
            self.textEdit.clear()
def closesys(self):
    sys.exit()

if __name__=='__main__':
    app = QApplication(sys.argv)
    pchat = PyqtChatApp()
    pchat.show()
    sys.exit(app.exec_())