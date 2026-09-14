# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_pecson.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import pecson_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 658)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(155, 0, 5, 255), stop:1 rgba(255, 255, 255, 255)) \n"
"}\n"
"\n"
"#widget {\n"
"background-color: #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#label {\n"
"color: #000:\n"
"}\n"
"\n"
"QLineEdit {\n"
"border: none;\n"
"border-bottom: 2px solid #cccccc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border-bottom: 2px solid #28e2a2;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #0d6efd;\n"
"border: 2px solid #fff;\n"
"color: #fff:\n"
"border-radius: 5px;\n"
"padding: 6px;\n"
"margin-top: 10px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"background-color: #0b5ed7;\n"
"border: 2px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(160, 50, 801, 521))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.widget = QWidget(self.layoutWidget1)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.login_title_text = QLabel(self.widget)
        self.login_title_text.setObjectName(u"login_title_text")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.login_title_text.setFont(font)
        self.login_title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.login_title_text)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.username_text = QLabel(self.widget)
        self.username_text.setObjectName(u"username_text")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.username_text.setFont(font1)

        self.verticalLayout_2.addWidget(self.username_text)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setPointSize(13)
        self.lineEdit.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.password_text = QLabel(self.widget)
        self.password_text.setObjectName(u"password_text")
        self.password_text.setFont(font1)

        self.verticalLayout.addWidget(self.password_text)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.show_password_login_checkbox = QCheckBox(self.widget)
        self.show_password_login_checkbox.setObjectName(u"show_password_login_checkbox")

        self.verticalLayout.addWidget(self.show_password_login_checkbox)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.register_button = QPushButton(self.widget)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setFont(font1)

        self.horizontalLayout.addWidget(self.register_button)

        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setFont(font1)

        self.horizontalLayout.addWidget(self.login_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_title_text.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username_text.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_text.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.show_password_login_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

