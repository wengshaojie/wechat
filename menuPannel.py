import sys,os
from PyQt4.QtGui import QApplication,QListWidget,QListWidgetItem,QLabel,QPixmap
from PyQt4.QtCore import QSize
class MenuButton(QListWidgetItem):
    def __init__(self,parent = None,imagepath='',mouse_press=None):
            super(MenuButton,self).__init__(parent)
            self.setSizeHint(QSize(60, 60))
            self.button_label = QLabel()
            self.button_label.setPixmap(QPixmap(imagepath).scaled(24,24))
            self.button_label.setStyleSheet("padding:17px 17px;")
            self.button_label.mousePressEvent=mouse_press
class MenuPannel(QListWidget):
    def __init__(self,parent = None):
        super(MenuPannel,self).__init__(parent)
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(60, 60))
        self.setStyleSheet("border:0px;background-color:#27282b;")
        self.setMaximumWidth(60)
        self.setMinimumWidth(60)
        self.addItem(item_widget)
        self.self_head_image = QLabel()
        self.self_head_image.setStyleSheet("padding:10px;")
        self.setItemWidget(item_widget, self.self_head_image)
    def changeSelectImage(self,index):
        if index==1:
            self.item(1).button_label.setPixmap(QPixmap(os.path.join('img','message.png')).scaled(24,24))
            self.item(2).button_label.setPixmap(QPixmap(os.path.join('img','note_.png')).scaled(24,24))
            self.item(3).button_label.setPixmap(QPixmap(os.path.join('img','config_.png')).scaled(24,24))
        elif index==2:
            self.item(1).button_label.setPixmap(QPixmap(os.path.join('img','message_.png')).scaled(24,24))
            self.item(2).button_label.setPixmap(QPixmap(os.path.join('img','note.png')).scaled(24,24))
            self.item(3).button_label.setPixmap(QPixmap(os.path.join('img','config_.png')).scaled(24,24))
        elif index==3:
            self.item(1).button_label.setPixmap(QPixmap(os.path.join('img','message_.png')).scaled(24,24))
            self.item(2).button_label.setPixmap(QPixmap(os.path.join('img','note_.png')).scaled(24,24))
            self.item(3).button_label.setPixmap(QPixmap(os.path.join('img','config.png')).scaled(24,24))
    def setSelfHeadImg(self,username):
        self.self_head_image.setPixmap(QPixmap(os.path.join('dist',username)).scaled(40,40))
    def addButton(self,imagepath,mouse_press):
        item_widget = MenuButton(self,imagepath,mouse_press)
        self.addItem(item_widget)
        self.setItemWidget(item_widget, item_widget.button_label)
if __name__ == "__main__":
        def test(event):
            print event
        app = QApplication(sys.argv)
        menu_pannel = MenuPannel()
        
        menu_pannel.addButton(os.path.join('img','message.png'),test)
        menu_pannel.addButton(os.path.join('img','note_.png'),test)
        menu_pannel.addButton(os.path.join('img','config_.png'),test)
        menu_pannel.show()
        sys.exit(app.exec_())