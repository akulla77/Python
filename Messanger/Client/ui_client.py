# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,QComboBox, QWidget,QListWidget, QLabel)

import requests
import json
from datetime import datetime, time

from requests.models import HTTPBasicAuth
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(422, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 390, 391, 71))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 480, 371, 21))
        self.pushButton.clicked.connect(self.SendMessage)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 160, 391, 211))

        self.listUsers = QListWidget(self.centralwidget)
        self.listUsers.setObjectName(u"listWidget")
        self.listUsers.setGeometry(QRect(10, 40, 171, 101))
        self.usersTimer = QtCore.QTimer()
        self.usersTimer.timeout.connect(self.FillUser)
        self.usersTimer.start(1000)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 35, 10))
        self.username = QLabel(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(50, 20, 35, 10))


        self.RefreshTimer = QtCore.QTimer()
        self.RefreshTimer.timeout.connect(self.RefreshLabels) 
        self.RefreshTimer.start(500)

        self.listContacts = QListWidget(self.centralwidget)
        self.listContacts.setObjectName(u"listContacts")
        self.listContacts.setGeometry(QRect(230, 40, 171, 101))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 20, 35, 10))
        self.contactname = QLabel(self.centralwidget)
        self.contactname.setObjectName(u"contactname")
        self.contactname.setGeometry(QRect(310, 20, 35, 10))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 35, 10))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 370, 71, 16))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
       
        self.contactTimer = QtCore.QTimer() 
        self.contactTimer.timeout.connect(self.FillContacts)
        self.contactTimer.start(1000)

      
        self.listContacts.clicked.connect(self.OnClickContact)
        self.listUsers.clicked.connect(self.OnClickUser)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.GetMessages)
        self.timer.start(5000)
        self.after =0
        self.User = ''
        self.Contact =''
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Messenger", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.username.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contact:", None))
        self.contactname.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Text message:", None))
    # retranslateUi


    def print_message(self,mes):
            t=  mes['time']
            dt = datetime.fromisoformat(t).strftime( "%m/%d/%Y, %H:%M:%S")
            self.textBrowser.append(dt +' '+ mes['src']+ '->'+mes['dest'])
            self.textBrowser.append(mes['text'])
            self.textBrowser.append('')
            


    @Slot()
    def RefreshLabels(self):
        
        self.username.setText(self.User)
        



    @Slot()
    def FillUser(self):
        resp = requests.get('http://localhost:3333/users')
        users = resp.json()
        if self.listUsers.count() != len(users):
            self.listUsers.clear()
            self.listUsers.addItems(users)
        
    
    def RefreshUser(self):
         requests.post('http://localhost:3333/userRefresh', json = {'user': self.User})


    @Slot()
    def OnClickUser(self, index):

        self.RefreshUser()

        self.User = self.listUsers.currentItem().text()
        self.username = self.User
        requests.post('http://localhost:3333/user', json = {'user': self.User})
        self.listUsers.clear()
        self.listContacts.clear()
        self.after = 0
        self.textBrowser.clear()
        self.Contact =''

    @Slot()
    def OnClickContact(self):
        self.Contact = self.listContacts.currentItem().text()
        self.contactname = self.Contact
        self.after = 0
        self.textBrowser.clear()



    @Slot()
    def FillContacts(self):
        resp = requests.get('http://localhost:3333/contacts', json = {'user': self.User})
        users = resp.json()
        if self.listContacts.count() != len(users):
            self.listContacts.clear()
            self.listContacts.addItems(users)
            


    @Slot()
    def SendMessage(self):

        src= self.User
        dest = self.Contact
        time =  str(datetime.now())
        text = self.textEdit.toPlainText()

        resp = requests.post('http://localhost:3333/send', json = {'src': src,'dest': dest, 'text': text, 'time': time} )
        if resp.status_code != 200:
            print('Check inputs data') 
            return
        
        self.textEdit.setText('')

    @Slot()
    def GetMessages(self):
        try:
            resp = requests.get('http://localhost:3333/messages', json ={'after':self.after, 'src': self.User, 'dest': self.Contact})
            # t= resp.json()
            # print(t)
            messages = resp.json()
            for message in messages:
                self.print_message(message)
                self.after = message['time']
        except Exception  as e:
            print(str(e))
            return

