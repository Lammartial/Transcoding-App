# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'loginUI.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
import res

class LogIn_Form(object):
    def initUI(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 612)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 720, 520))

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 325, 470))
        self.label.setStyleSheet(u"border-image: url(:/images/Resized image/Lake_Purple_Nature_Sunset.jpg);\n"
                                 "border-top-left-radius: 50px;")

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 320, 470))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
                                   "border-bottom-right-radius: 50px;")

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 80, 80, 50))
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(27,18,18,200);")

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(395, 180, 250, 41))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(8)
        self.lineEdit.setFont(font1)
        self.lineEdit.setCursor(QCursor(Qt.SizeVerCursor))

        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                    "border:none;\n"
                                    "border-bottom: 2px solid rgba(8,80,120,200);\n"
                                    "color: rgba(0,0,0,240);\n"
                                    "padding-bottom:7px;")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(395, 250, 250, 41))
        self.lineEdit_2.setEchoMode(
            QtWidgets.QLineEdit.Password)  # show the dots
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(8,80,120,200);\n"
                                      "color: rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;")

        self.logInButton = QPushButton(self.widget)
        self.logInButton.setObjectName(u"pushButton")
        self.logInButton.setGeometry(QRect(395, 380, 250, 41))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.logInButton.setFont(font3)
        self.logInButton.setStyleSheet(u"QPushButton#pushButton{\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.505862, x2:1, y2:0.477, stop:0 rgba(221, 94, 137, 1), stop:1 rgba(247, 187, 151, 1));\n"
                                       "	color: rgba(255, 255, 255, 210);\n"
                                       "	border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#pushButton:hover{\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.505862, x2:1, y2:0.477, stop:0 rgba(222, 98, 98, 219), stop:1 rgba(255, 184, 140, 226));\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#pushButton:pressed{\n"
                                       "	padding-left: 5px;\n"
                                       "	padding-top: 5px;\n"
                                       "	background-color: rgba(248, 131, 121, 255);\n"
                                       "}")

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(395, 305, 111, 31))
        font5 = QFont()
        font5.setFamily(u"Montserrat")
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setWeight(50)
        self.checkBox.setFont(font5)
        self.checkBox.setStyleSheet(u"QCheckBox::indicator:unchecked{\n"
                                    " border: 1.5px solid rgb(128, 0, 128);\n"
                                    "}\n"
                                    u"QCheckBox::indicator:unchecked:hover{\n"
                                    " border: 1.5px solid rgb(242, 112, 156);\n"
                                    "}\n"
                                    u"QCheckBox::indicator:unchecked:pressed{\n"
                                    " background-color: rgb(255, 148, 114);\n"
                                    "}\n"
                                    "")

        # setting check box state to checked
        self.checkBox.setChecked(False)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 445, 161, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:rgba(27,18,18,200);")

        self.signUpButton = QPushButton(self.widget)
        self.signUpButton.setObjectName(u"signUpButton")
        self.signUpButton.setGeometry(QRect(567, 451, 51, 20))
        font6 = QFont()
        font6.setFamily(u"Montserrat")
        font6.setBold(True)
        font6.setWeight(75)
        self.signUpButton.setFont(font6)
        self.signUpButton.setAutoFillBackground(False)
        self.signUpButton.setStyleSheet(u"QPushButton#signUpButton {\n"
                                        "	color: rgba(128,0,128,1);\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border: None;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#signUpButton:hover {\n"
                                        "  color: rgb(240, 101, 131);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton#signUpButton:pressed{\n"
                                        "	color: rgba(248, 131, 121, 255);\n"
                                        "}\n"
                                        "\n"
                                        "")

        self.signUpButton.setCheckable(False)
        self.signUpButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(530, 310, 121, 21))
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2 {\n"
                                        "	color: rgba(128,0,128,1);\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border: None;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#pushButton_2:hover {\n"
                                        "  color: rgb(240, 101, 131);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#pushButton_2:pressed{\n"
                                        "	color: rgba(248, 131, 121, 255);\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))


        self.error = QLabel(self.widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(395, 335, 251, 21))
        font6 = QFont()
        font6.setFamily(u"Montserrat")
        font6.setBold(False)
        font6.setWeight(50)
        self.error.setFont(font6)
        self.error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.logInButton.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(
            QCoreApplication.translate("Form", u"Login", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Form", u"username/e-mail", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", u"password", None))
        self.logInButton.setText(
            QCoreApplication.translate("Form", u"Login", None))
        self.checkBox.setText(QCoreApplication.translate(
            "Form", u" Remember me", None))
        self.label_5.setText(QCoreApplication.translate(
            "Form", u" Don't have an account yet?", None))
        self.signUpButton.setText(
            QCoreApplication.translate("Form", u"Sign up", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "Form", u"Forgot Password?", None))
    # retranslateUi
