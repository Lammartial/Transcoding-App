from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc


class MainWindowUI(object):
    def initUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
# endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
# endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
# endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "	color: #ffffff;\n"
                                 "	background-color: rgba(27, 29, 35, 160);\n"
                                 "	border: 1px solid rgb(40, 40, 40);\n"
                                 "	border-radius: 2px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
                                         "color: rgb(210, 210, 210);")

        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
                                      "QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* SCROLL BARS */\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 14px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    background: rgb(85, 170, 255);\n"
                                      "    min-width: 25px;\n"
                                      "	border-radius: 7px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-right-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: right;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      ""
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    subcontrol-position: left;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 14px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(85, 170, 255);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 7px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "     border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "     subcontrol-position: bottom;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(55, 63"
                                      ", 77);\n"
                                      "     height: 20px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "     subcontrol-position: top;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "/* CHECKBOX */\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    background: 3px solid rgb(52, 59, 72);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* RADIO BUTTON */\n"
                                      "QRadioButton::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius"
                                      ": 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "    background: 3px solid rgb(94, 106, 130);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "}\n"
                                      "\n"
                                      "/* COMBOBOX */\n"
                                      "QComboBox{\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb("
                                      "85, 170, 255);	\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}\n"
                                      "\n"
                                      "/* SLIDERS */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border-radius: 9px;\n"
                                      "    height: 18px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:horizontal:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "    border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border-radius: 9px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:verti"
                                      "cal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "	border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u" background-color: rgba(27,18,18,200);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(
            u"background-color: rgba(27,18,18,200);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setStyleSheet(
            u"background-color: rgba(27,18,18,200);")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background-color: rgba(27,18,18,200);\n"
                                               "")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(
            self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
                                        "	border: none;\n"
                                        "	background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(240, 101, 131);\n"
                                        "}\n"
                                        "")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(
            self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
                                                "	border: none;\n"
                                                "	background-color: transparent;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "	background-color: rgb(52, 59, 72);\n"
                                                "}\n"
                                                "QPushButton:pressed {	\n"
                                                "	background-color: rgb(240, 101, 131);\n"
                                                "}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(
            self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
                                     "	border: none;\n"
                                     "	background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color: rgb(240, 101, 131);\n"
                                     "\n"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(
            self.frame_btns_right, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: transparent;")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_welcome = QLabel(self.frame_top_info)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_welcome.setFont(font2)
        self.label_welcome.setStyleSheet(u"color: rgb(98, 103, 111); ")
        self.label_welcome.setIndent(-1)

        self.horizontalLayout_8.addWidget(self.label_welcome)

        self.verticalLayout_2.addWidget(self.frame_top_info)

        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy2)
        self.frame_center.setStyleSheet(u"background-color: rgba(27,18,18,200);\n"
                                        "")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.frame_center)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(27,18,18,200);")
        self.message_label = QLabel(self.widget)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setGeometry(QRect(50, 80, 81, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.message_label.setFont(font3)
        self.message_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                         "background-color:none")
        self.output_label = QLabel(self.widget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(50, 170, 81, 31))
        self.output_label.setFont(font3)
        self.output_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                        "background-color:none")
        self.lineEdit_mes = QLineEdit(self.widget)
        self.lineEdit_mes.setObjectName(u"lineEdit_mes")
        self.lineEdit_mes.setGeometry(QRect(145, 80, 600, 40))
        font4 = QFont()
        font4.setPointSize(12)
        self.lineEdit_mes.setFont(font4)
        self.lineEdit_mes.setStyleSheet(u"background-color: rgba(255, 255, 255, 230);\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border: 1px solid rgb(255, 175, 123);")
        self.lineEdit_output = QLineEdit(self.widget)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setGeometry(QRect(145, 170, 600, 40))
        self.lineEdit_output.setFont(font4)
        self.lineEdit_output.setStyleSheet(u"background-color: rgba(255, 255, 255, 230);\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border: 1px solid rgb(255, 175, 123);")
        self.lineEdit_output.setReadOnly(True)
        self.mode_label = QLabel(self.widget)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setGeometry(QRect(50, 252, 81, 31))
        self.mode_label.setFont(font3)
        self.mode_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                      "background-color:none")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(210, 260, 101, 17))
        self.checkBox.setFont(font2)
        self.checkBox.setStyleSheet(u"background-color:  transparent;\n"
                                    "")
        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(380, 260, 101, 17))
        self.checkBox_2.setFont(font2)
        self.checkBox_2.setStyleSheet(u"background-color: transparent")
        self.encode_decode_label = QLabel(self.widget)
        self.encode_decode_label.setObjectName(u"encode_decode_label")
        self.encode_decode_label.setGeometry(QRect(340, 10, 321, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.encode_decode_label.setFont(font5)
        self.encode_decode_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                               "background-color: transparent\n"
                                               "")
        self.algorithm_label = QLabel(self.widget)
        self.algorithm_label.setObjectName(u"algorithm_label")
        self.algorithm_label.setGeometry(QRect(50, 330, 91, 31))
        self.algorithm_label.setFont(font3)
        self.algorithm_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                           "background-color:none")
        self.algorithm_list = QComboBox(self.widget)
        self.algorithm_list.addItem("")
        self.algorithm_list.setObjectName(u"algorithm_list")
        self.algorithm_list.setGeometry(QRect(168, 332, 140, 31))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        self.algorithm_list.setFont(font6)
        self.algorithm_list.setStyleSheet(u"background-color: transparent;\n"
                                          "color: rgb(255, 175, 191);\n"
                                          "border: 1px solid rgba(255, 184, 140, 226);")
        self.memory_label = QLabel(self.widget)
        self.memory_label.setObjectName(u"memory_label")
        self.memory_label.setGeometry(QRect(50, 410, 91, 31))
        self.memory_label.setFont(font3)
        self.memory_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                        "background-color:none")
        self.lineEdit_memory = QLineEdit(self.widget)
        self.lineEdit_memory.setObjectName(u"lineEdit_memory")
        self.lineEdit_memory.setGeometry(QRect(150, 410, 100, 31))
        self.lineEdit_memory.setFont(font4)
        self.lineEdit_memory.setStyleSheet(u"background-color: rgba(255, 255, 255, 230);\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border: 1px solid rgb(255, 175, 123);")
        self.lineEdit_memory.setReadOnly(True)
        self.MB_label = QLabel(self.widget)
        self.MB_label.setObjectName(u"MB_label")
        self.MB_label.setGeometry(QRect(260, 410, 41, 31))
        self.MB_label.setFont(font3)
        self.MB_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                    "background-color:none")
        self.time_label = QLabel(self.widget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(380, 410, 141, 31))
        self.time_label.setFont(font3)
        self.time_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                      "background-color:none")
        self.lineEdit_time = QLineEdit(self.widget)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setGeometry(QRect(535, 410, 120, 31))
        self.lineEdit_time.setFont(font4)
        self.lineEdit_time.setStyleSheet(u"background-color: rgba(255, 255, 255, 230);\n"
                                         "border-radius: 10px;\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border: 1px solid rgb(255, 175, 123);")
        self.lineEdit_time.setReadOnly(True)
        self.credit_label = QLabel(self.widget)
        self.credit_label.setObjectName(u"credit_label")
        self.credit_label.setGeometry(QRect(6, 600, 211, 20))
        font7 = QFont()
        font7.setBold(True)
        font7.setItalic(True)
        font7.setWeight(75)
        self.credit_label.setFont(font7)
        self.credit_label.setStyleSheet(u"background-color:transparent;\n"
                                        "")
        self.version_label = QLabel(self.widget)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(897, 600, 211, 20))
        self.version_label.setFont(font7)
        self.version_label.setStyleSheet(u"background-color:transparent;\n"
                                         "")
        self.frame_icon_clock = QFrame(self.widget)
        self.frame_icon_clock.setObjectName(u"frame_icon_clock")
        self.frame_icon_clock.setGeometry(QRect(505, 412, 30, 30))
        self.frame_icon_clock.setMaximumSize(QSize(30, 30))
        self.frame_icon_clock.setStyleSheet(u"background: transparent;\n"
                                            "background-image: url(:/16x16/icons/16x16/cil-alarm.png);\n"
                                            "background-position: center;\n"
                                            "background-repeat: no-repeat;\n"
                                            "")
        self.frame_icon_clock.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_clock.setFrameShadow(QFrame.Raised)
        self.dropdown_icon_label = QLabel(self.widget)
        self.dropdown_icon_label.setObjectName(u"dropdown_icon_label")
        self.dropdown_icon_label.setGeometry(QRect(288, 340, 16, 16))
        self.dropdown_icon_label.setStyleSheet(
            u"background-image: url(:/16x16/icons/16x16/cil-caret-bottom.png);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 500, 250, 41))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
                                 "border-radius: 10px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 500, 250, 41))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.pushButton.setFont(font8)
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

        self.key_label = QLabel(self.widget)
        self.key_label.setObjectName(u"key_label")
        self.key_label.setGeometry(QRect(380, 330, 61, 31))
        self.key_label.setFont(font3)
        self.key_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                     "background-color:none")
        self.lineEdit_key = QLineEdit(self.widget)
        self.lineEdit_key.setObjectName(u"lineEdit_key")
        self.lineEdit_key.setGeometry(QRect(450, 330, 81, 31))
        self.lineEdit_key.setFont(font4)
        self.lineEdit_key.setStyleSheet(u"background-color: rgba(255, 255, 255, 230);\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border: 1px solid rgb(255, 175, 123);")

        self.err = QLabel(self.widget)
        self.err.setObjectName(u"err")
        self.err.setGeometry(QRect(50, 550, 251, 21))
        self.err.setFont(font1)
        self.err.setStyleSheet(u"background-color: transparent;\n"
                               "color: rgb(255, 0, 0);")

        self.key_label_2 = QLabel(self.widget)
        self.key_label_2.setObjectName(u"key_label_2")
        self.key_label_2.setGeometry(QRect(590, 330, 61, 31))
        self.key_label_2.setFont(font3)
        self.key_label_2.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                       "background-color:none")
        self.lineEdit_key_2 = QLineEdit(self.widget)
        self.lineEdit_key_2.setObjectName(u"lineEdit_key_2")
        self.lineEdit_key_2.setGeometry(QRect(660, 330, 81, 31))
        self.lineEdit_key_2.setFont(font4)
        self.lineEdit_key_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 230);\n"
                                          "border-radius: 10px;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "border: 1px solid rgb(255, 175, 123);")

        self.label_seconds = QLabel(self.widget)
        self.label_seconds.setObjectName(u"label_seconds")
        self.label_seconds.setGeometry(QRect(665, 410, 81, 31))
        self.label_seconds.setFont(font3)
        self.label_seconds.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(58, 28,113), stop:1 rgb(215, 109, 119));\n"
                                         "background-color:none")

        self.horizontalLayout_2.addWidget(self.widget)

        self.verticalLayout.addWidget(self.frame_center)

        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate(
            "MainWindow", u"Transcoding App", None))
# if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(
            QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
# if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(
            QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
# if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_welcome.setText(QCoreApplication.translate(
            "MainWindow", u"Welcome, ", None))
        self.message_label.setText(
            QCoreApplication.translate("MainWindow", u"Message", None))
        self.output_label.setText(
            QCoreApplication.translate("MainWindow", u"Output", None))
        self.lineEdit_mes.setText("")
        self.lineEdit_output.setText("")
        self.mode_label.setText(
            QCoreApplication.translate("MainWindow", u"Mode", None))
        self.checkBox.setText(QCoreApplication.translate(
            "MainWindow", u"Encode", None))
        self.checkBox_2.setText(QCoreApplication.translate(
            "MainWindow", u"Decode", None))
        self.encode_decode_label.setText(QCoreApplication.translate(
            "MainWindow", u"ENCODING-DECODING", None))
        self.algorithm_label.setText(
            QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.algorithm_list.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Diffie_Hellman", None))
        self.memory_label.setText(
            QCoreApplication.translate("MainWindow", u"Memory", None))
        self.lineEdit_memory.setText("")
        self.MB_label.setText(
            QCoreApplication.translate("MainWindow", u"MB", None))
        self.time_label.setText(QCoreApplication.translate(
            "MainWindow", u"Time Duration", None))
        self.lineEdit_time.setText("")
        self.credit_label.setText(QCoreApplication.translate(
            "MainWindow", u"Created by: Miniteam", None))
        self.version_label.setText(QCoreApplication.translate(
            "MainWindow", u"Version: 1.0.0", None))
        self.dropdown_icon_label.setText("")
        self.label.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"START", None))
        self.key_label.setText(QCoreApplication.translate(
            "MainWindow", u"A_KEY", None))
        self.lineEdit_key.setText("")
        self.err.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.key_label_2.setText(
            QCoreApplication.translate("MainWindow", u"B_KEY", None))
        self.lineEdit_key_2.setText("")
        self.label_seconds.setText(
            QCoreApplication.translate("MainWindow", u"seconds", None))
    # retranslateUi
