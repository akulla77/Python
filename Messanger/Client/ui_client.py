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
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QWidget)
import requests
import json
from datetime import datetime, time

from requests.models import HTTPBasicAuth
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 253, 181, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 260, 31, 21))
        self.pushButton.clicked.connect(self.SendMessage)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 40, 221, 201))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 10, 113, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.GetMessages)
        self.timer.start(5000)
        self.after =0
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Messenger", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi


    def print_message(self,mes):
            t= mes['time']
            dt = datetime.fromtimestamp(t).strftime('%H:%M:%S')
            self.textBrowser.append(dt +' '+ mes['name'])
            self.textBrowser.append(mes['text'])
            self.textBrowser.append('')
            





    @Slot()
    def SendMessage(self):

        name= self.lineEdit.text()
        text = self.textEdit.toPlainText()

        resp = requests.post('http://localhost:3333/send', json = {'name': name,'text': text} )
        if resp.status_code != 200:
            print('Check inputs data') 
            return
        
        self.textEdit.setText('')

    @Slot()
    def GetMessages(self):
        try:
            resp = requests.get('http://localhost:3333/messages', json ={'after':self.after})
            t= resp.json()
            print(t)
            # messages = resp.json()['messages']
            # for message in messages:
            #     self.print_message(message)
            #     self.after = message['time']
        except Exception  as e:
            print(str(e))
            return

