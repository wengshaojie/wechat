#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from menuPannel import MenuPannel
from userPannel import UserPannel
from operationPannel import OperationPannel
import itchat,robot
msgBox={}
class Ui_Main(QSplitter):
    """聊天界面，QSplitter用于让界面可以鼠标拖动调节"""
    curUser = {'id':None,'name':None,'head':'self'}

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def __init__(self):
        super(Ui_Main, self).__init__(Qt.Horizontal)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setMinimumSize(850,665) # 窗口最小大小
        self.setStyleSheet("background-color:#f5f5f5;")

        self.menu_pannel = MenuPannel(self)
        self.menu_pannel.addButton(os.path.join('img','message.png'),self.showChatPannel)
        self.menu_pannel.addButton(os.path.join('img','note_.png'),self.showUserPannel)
        self.menu_pannel.addButton(os.path.join('img','config_.png'),self.showGroupPannel)

        self.user_pannel = UserPannel(self)
        self.user_pannel.setUserListItemClickedEvent(self.getFriendInfo)
        self.user_pannel.setChatListItemClickedEvent(self.setChatUser)



        self.operation_pannel = OperationPannel(self)
        self.operation_pannel.showInitMessagePannel()
        self.operation_pannel.info_pannel.setToCharButtonClickedEvent(self.toChart)
        self.operation_pannel.message_pannel.setSendTextMsgEvent(self.sendTextMsg)
        self.operation_pannel.message_pannel.setSendImageMsgEvent(self.sendImgMsg)
        self.operation_pannel.info_pannel.setAutorepyChangeEvent(self.setAutorepy)
    def showChatPannel(self,event):
        self.user_pannel.showChatPannel()
        self.operation_pannel.showInitMessagePannel()
        self.menu_pannel.changeSelectImage(1)
        self.user_pannel.chat_ListWidget.setCurrentRow(-1)
    def showUserPannel(self,event):
        self.user_pannel.showUserPannel()
        self.operation_pannel.showInitMessagePannel()
        self.menu_pannel.changeSelectImage(2)

        self.user_pannel.user_ListWidget.setCurrentRow(-1)
    def showGroupPannel(self,event):
        #self.user_pannel.showUserPannel()
        #self.menu_pannel.changeSelectImage(2)
        print '还没有实现'
    def initUserData(self,list):
        self.userinfo=list[0]
        self.menu_pannel.setSelfHeadImg(self.userinfo['UserName'])

        self.user_pannel.initUserData(list)

 
    def setMsgHistory(self):
        self.operation_pannel.message_pannel.msgList.clear()
       
        if not msgBox.has_key(self.curUser['head']):
            msgBox[self.curUser['head']]=[]
        for boxmsg,ifself,boxuser,type in msgBox[self.curUser['head']]:
            if type=='Picture':
                    self.operation_pannel.message_pannel.msgList.addImageMsg(boxmsg,ifself,head = boxuser)
            else:
                    self.operation_pannel.message_pannel.msgList.addTextMsg(boxmsg,ifself,head = boxuser)

    def receiveMsg(self,list):
        for msg in list:
            note=''
            if msg['Type']=='Picture':
                fileDir = '%s%s'%(msg['Type'], int(time.time()))
                msg['Text'](fileDir)
                note=u'[图片]'
                if msg['FromUserName']==self.curUser['head']:
                    if '@@' in msg['FromUserName']:
                       msgBox[msg['FromUserName']].append((fileDir,True,msg['ActualUserName'],msg['Type']))
                       self.operation_pannel.message_pannel.msgList.addImageMsg(fileDir,True,msg['ActualUserName'])
                    else:
                       msgBox[msg['FromUserName']].append((fileDir,True,self.curUser['head'],msg['Type']))
                       self.operation_pannel.message_pannel.msgList.addImageMsg(fileDir,True,self.curUser['head'])
                    self.user_pannel.sendNewMessage(msg['FromUserName'],note)
                else:
                    if not msgBox.has_key(msg['FromUserName']):
                       msgBox[msg['FromUserName']]=[]
                    if '@@' in msg['FromUserName']:
                       msgBox[msg['FromUserName']].append((fileDir,True,msg['ActualUserName'],msg['Type']))
                    else:
                       msgBox[msg['FromUserName']].append((fileDir,True,msg['FromUserName'],msg['Type']))

                self.user_pannel.updateNewMessage(msg['FromUserName'],note)
            elif msg['Type']=='Init':
                if msg['StatusNotifyCode']==4:
                    chatusers=msg['StatusNotifyUserName'].split(',')
                    #for chatuser in chatusers:
                         #self.user_pannel.sendNewMessage(chatuser,'')
                    for index in range(0,len(chatusers))[::-1]:
                        self.user_pannel.sendNewMessage(chatusers[index],'')
                else:
                    print msg
            elif msg['Type']=='Text':
                note=msg['Text']
                if msg['FromUserName']==self.curUser['head']:
                    if '@@' in msg['FromUserName']:
                       msgBox[msg['FromUserName']].append((msg['Text'],True,msg['ActualUserName'],msg['Type']))
                       self.operation_pannel.message_pannel.msgList.addTextMsg(msg['Text'],True,msg['ActualUserName'])
                    else:
                       msgBox[msg['FromUserName']].append((msg['Text'],True,self.curUser['head'],msg['Type']))
                       self.operation_pannel.message_pannel.msgList.addTextMsg(msg['Text'],True,self.curUser['head'])
                    self.user_pannel.sendNewMessage(msg['FromUserName'],note)
                    if self.user_pannel.isAutoRepy(msg['FromUserName']):
                            result=robot.getResultFromRobot(msg['Text'],msg['FromUserName'])
                            self.sendTextMsg(result['text'])
                else:
                    if not msgBox.has_key(msg['FromUserName']):
                       msgBox[msg['FromUserName']]=[]
                    if '@@' in msg['FromUserName']:
                       msgBox[msg['FromUserName']].append((msg['Text'],True,msg['ActualUserName'],msg['Type']))
                    else:
                       msgBox[msg['FromUserName']].append((msg['Text'],True,msg['FromUserName'],msg['Type']))
                    self.user_pannel.updateNewMessage(msg['FromUserName'],note)
                    if self.user_pannel.isAutoRepy(msg['FromUserName']):
                            result=robot.getResultFromRobot(msg['Text'],msg['FromUserName'])
                            itchat.send_msg(result['text'], msg['FromUserName'])
                            if not msgBox.has_key(msg['FromUserName']):
                                msgBox[msg['FromUserName']]=[]
                            msgBox[msg['FromUserName']].append((result['text'],False,self.userinfo['UserName'],msg['Type']))
            else:
                print msg['Type']
                print msg
                continue
    def setAutorepy(self, value):
        if self.operation_pannel.info_pannel.autorepy.isChecked():
            self.selectItem.setAuto(True)
        else:
            self.selectItem.setAuto(False)
    def toChart(self,event):
        self.user_pannel.sendNewMessage(self.selectItem.getHead(),self.selectItem.getNote())
        self.menu_pannel.changeSelectImage(1)
        self.setChatUser(self.selectItem)
    @pyqtSlot(str)
    def sendTextMsg(self,txt):
        txt = unicode(txt)
        self.operation_pannel.message_pannel.msgList.addTextMsg(txt,False,self.userinfo['UserName'])
        itchat.send_msg(txt, self.curUser['head'])
        if not msgBox.has_key(self.curUser['head']):
            msgBox[self.curUser['head']]=[]
        msgBox[self.curUser['head']].append((txt,False,self.userinfo['UserName'],'text'))
        self.user_pannel.sendNewMessage(self.curUser['head'],txt)
    @pyqtSlot(str)
    def sendImgMsg(self,img):
        img = unicode(img)
        self.operation_pannel.message_pannel.msgList.addImageMsg(img,False,head = self.userinfo['UserName'])
        if not msgBox.has_key(self.curUser['head']):
            msgBox[self.curUser['head']]=[]
        msgBox[self.curUser['head']].append((img,False,self.userinfo['UserName'],'Picture'))
        itchat.send_image(img, self.curUser['head'])
    @pyqtSlot(QListWidgetItem)
    def setChatUser(self,item):
        (self.curUser['id'],self.curUser['name'],self.curUser['head']) = (item.getId(),item.getName(),item.getHead())
        #self.operation_pannel.message_pannel.nonbackground.hide()
        #self.operation_pannel.hide()
        #self.operation_pannel.message_pannel.show()
        self.user_pannel.showChatPannel()
        self.operation_pannel.showMessageInOut()
        #self.operation_pannel.message_pannel.msgList.setDisabled(False)
        self.operation_pannel.message_pannel.msg_pannel_title_label.setText(self.curUser['name'])
        self.setMsgHistory()
    def getFriendInfo(self,item):
        self.selectItem=item
        self.operation_pannel.showUserInfo(item)
if __name__=='__main__':
    app = QApplication(sys.argv)
    pchat = Ui_Main()
    pchat.show()
    sys.exit(app.exec_())