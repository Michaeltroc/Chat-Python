# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ChatForm(object):
    def setupUi(self, chatForm):
        if not chatForm.objectName():
            chatForm.setObjectName(u"chatForm")
        chatForm.resize(877, 538)
        self.frame = QFrame(chatForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 877, 91))
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(170, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 30, 241, 31))
        self.label.setStyleSheet(u"color: white;")
        self.logoutButton = QPushButton(self.frame)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(760, 30, 81, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.logoutButton.setFont(font)
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutButton.setAutoFillBackground(False)
        self.logoutButton.setStyleSheet(u"background-color: rgb(231, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.logoutButton.setIconSize(QSize(60, 60))
        self.logoutButton.setFlat(True)
        self.chatTextEdit = QTextEdit(chatForm)
        self.chatTextEdit.setObjectName(u"chatTextEdit")
        self.chatTextEdit.setGeometry(QRect(0, 90, 877, 381))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.chatTextEdit.setFont(font1)
        self.chatTextEdit.setAutoFillBackground(True)
        self.chatTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black")
        self.chatTextEdit.setReadOnly(True)
        self.frame_2 = QFrame(chatForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 470, 877, 71))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.messageLineEdit = QLineEdit(self.frame_2)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(20, 10, 741, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.messageLineEdit.setFont(font2)
        self.messageLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sendButton = QPushButton(self.frame_2)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(780, 10, 81, 51))
        self.sendButton.setFont(font)
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setAutoFillBackground(False)
        self.sendButton.setStyleSheet(u"background-color: rgb(231, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.sendButton.setIconSize(QSize(60, 60))
        self.sendButton.setFlat(True)

        self.retranslateUi(chatForm)

        QMetaObject.connectSlotsByName(chatForm)
    # setupUi

    def retranslateUi(self, chatForm):
        chatForm.setWindowTitle(QCoreApplication.translate("chatForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CHAT ROOM</span></p></body></html>", None))
        self.logoutButton.setText(QCoreApplication.translate("chatForm", u"SALIR", None))
        self.messageLineEdit.setText("")
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("chatForm", u"Escribe un mensaje....", None))
        self.sendButton.setText(QCoreApplication.translate("chatForm", u"ENVIAR", None))
    # retranslateUi

