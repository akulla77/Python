# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QWidget)







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
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 160, 391, 211))

        self.listUser = QListWidget(self.centralwidget)
        self.listUser.setObjectName(u"listUser")
        self.listUser.setGeometry(QRect(10, 40, 171, 101))
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 35, 10))
        self.username = QLabel(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(50, 20, 35, 10))
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

