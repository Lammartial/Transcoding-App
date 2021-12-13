from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
import registration


class Reg_Form(object):
    def initUI(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(782, 612)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 720, 520))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 320, 470))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
                                   "border-bottom-right-radius: 50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(465, 80, 110, 50))
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(27,18,18,200);")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(395, 150, 250, 41))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(8,80,120,200);\n"
                                      "color: rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(395, 380, 250, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
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
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 445, 161, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgba(27,18,18,200);")

        self.signInButton = QPushButton(self.widget)
        self.signInButton.setObjectName(u"signInButton")
        self.signInButton.setGeometry(QRect(555, 453, 51, 16))
        font3 = QFont()
        font3.setFamily(u"Montserrat")
        font3.setBold(True)
        font3.setWeight(75)
        self.signInButton.setFont(font3)
        self.signInButton.setAutoFillBackground(False)
        self.signInButton.setStyleSheet(u"QPushButton#signInButton {\n"
                                        "	color: rgba(128,0,128,1);\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border: None;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#signInButton:hover {\n"
                                        "  color: rgb(240, 101, 131);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton#signInButton:pressed{\n"
                                        "	color: rgba(248, 131, 121, 255);\n"
                                        "}\n"
                                        "\n"
                                        "")

        self.signInButton.setCheckable(False)
        self.signInButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 325, 470))
        self.label.setStyleSheet(u"border-image: url(:/images/cave.jpg);\n"
                                 "border-top-left-radius: 50px;")
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(395, 250, 250, 41))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setEchoMode(
            QtWidgets.QLineEdit.Password)  # show the dots
        self.lineEdit_4.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(8,80,120,200);\n"
                                      "color: rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(395, 300, 250, 41))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setEchoMode(
            QtWidgets.QLineEdit.Password)  # show the dots
        self.lineEdit_5.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(8,80,120,200);\n"
                                      "color: rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(395, 200, 250, 41))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(8,80,120,200);\n"
                                      "color: rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;")
        self.err = QLabel(self.widget)
        self.err.setObjectName(u"label_4")
        self.err.setGeometry(QRect(395, 350, 250, 16))
        self.err.setFont(font1)
        self.err.setStyleSheet(u"color: rgb(255,0,0)")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label_3.setText(
            QCoreApplication.translate("Form", u"Sign up", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", u"username", None))
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"Register", None))
        self.label_5.setText(QCoreApplication.translate(
            "Form", u" Already have an account?", None))
        self.signInButton.setText(
            QCoreApplication.translate("Form", u"Sign in", None))
        self.label.setText("")
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("Form", u"password", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("Form", u"confirm password", None))
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("Form", u"email address", None))
    # retranslateUi
