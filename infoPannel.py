#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class InfoPannel(QSplitter):
    def closesys(self, event):
        sys.exit()
    def  __init__(self,parent = None):
        super(InfoPannel,self).__init__(parent)
        self.setOrientation(Qt.Vertical)
        self.setMinimumHeight(665)
        self.setMinimumWidth(530)
        self.titlepannel=QWidget()
        self.titlepannel.setMaximumHeight(40)
        self.titlepannel.setMinimumHeight(40)
        self.titlepannel.setParent(self)
        self.titlepannel.setStyleSheet("margin:0px;font-size:12px;border:0px;padding:0px;background-color:#f5f5f5;")
        close_label = QLabel()
        close_label.setGeometry(QRect(510, 8, 14, 14))
        close_label.setStyleSheet("QLabel{background-image:url(img/close.png);}")
        close_label.mousePressEvent=self.closesys
        close_label.setParent(self.titlepannel)
        self.user_info=QWidget()
        self.user_info.setParent(self)
        user_info_layout=QGridLayout()
        self.user_info.setLayout(user_info_layout)
        self.name_label=QLabel()
        self.sex_label=QLabel()
        self.city_label=QLabel()
        self.head_image_label=QLabel()

        operator_layout=QGridLayout()
        self.operator=QWidget()
        self.operator.setParent(self)

        self.autorepy = QCheckBox(u'自动回复')
        self.tochar_button = QPushButton(u'发送消息')
        self.tochar_button.setStyleSheet("QPushButton{padding:10px;border:1px solid #cccccc;color:cccccc}"
             "QPushButton:hover{padding:10px;background-color:#129611;color:while}"
             "QPushButton:pressed{padding:10px;background-color:#129611;color:while}")

        operator_layout.addWidget(self.tochar_button,0,0,1,1,Qt.AlignCenter)
        operator_layout.addWidget(self.autorepy,1,0,1,1,Qt.AlignCenter)
        self.operator.setLayout(operator_layout)
        user_info_layout.addWidget(self.name_label,0,0,1,1,Qt.AlignRight)
        user_info_layout.addWidget(self.sex_label,0,1,1,1,Qt.AlignLeft)
        user_info_layout.addWidget(self.city_label,1,0,1,1,Qt.AlignRight)
        user_info_layout.addWidget(self.head_image_label,0,2,2,1,Qt.AlignCenter)  
        user_info_layout.addWidget(self.operator,2,0,1,3,Qt.AlignCenter)
        self.sex_label.setStyleSheet("margin:0px;border:0px;padding:0px;")
        self.name_label.setStyleSheet("border:0px;padding:0px;font-size:16px;font-weight:700;color:#333333;")
        self.city_label.setStyleSheet("border:0px;padding:0px;font-size:12px;font-weight:500;color:#aaaaaa;")
        self.head_image_label.setStyleSheet("margin:0px;border:0px;padding:0px;")
        user_info_layout.setRowStretch(0, 1)
        user_info_layout.setRowStretch(1, 1)
        user_info_layout.setRowStretch(2, 20)
        user_info_layout.setColumnStretch(0, 6)
        user_info_layout.setColumnStretch(1, 1)
        user_info_layout.setColumnStretch(2, 12)
    def setAutorepyChangeEvent(self,AutorepyChangeEvent):
        self.autorepy.stateChanged.connect(AutorepyChangeEvent)
    def setToCharButtonClickedEvent(self,ToCharButtonClickedEvent):
            self.tochar_button.clicked.connect(ToCharButtonClickedEvent)
    def showUserInfo(self,item):
        self.head_image_label.setPixmap(QPixmap(os.path.join('dist',item.getHead())).scaled(60,60))
        self.name_label.setText(item.getName())
        self.setSexLabel(item.getSex())
        self.city_label.setText(item.getCity())
        self.show()
    def setSexLabel(self,sex):
        if sex== 1:
            self.sex_label.setPixmap(QPixmap(os.path.join('img','men.png')).scaled(12,12))
        else:
            self.sex_label.setPixmap(QPixmap(os.path.join('img','fem.png')).scaled(12,12))
        #self.setCurUserTitle('')
if __name__=='__main__':
        def test(event):
            print event
        app = QApplication(sys.argv)
        menu_pannel = InfoPannel()
        menu_pannel.name_label.setText('wenhxiao')
        menu_pannel.setSexLabel(1)
        menu_pannel.city_label.setText('asfdasdfsadf')

        menu_pannel.show()
        sys.exit(app.exec_())