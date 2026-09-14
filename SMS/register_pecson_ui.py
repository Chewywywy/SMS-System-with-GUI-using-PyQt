# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_pecson.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import resource_rc

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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(308, 98, 611, 409))
        self.register_reg_button = QLabel(self.widget)
        self.register_reg_button.setObjectName(u"register_reg_button")
        self.register_reg_button.setGeometry(QRect(260, 20, 118, 36))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.register_reg_button.setFont(font)
        self.register_reg_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.register_title_text = QPushButton(self.widget)
        self.register_title_text.setObjectName(u"register_title_text")
        self.register_title_text.setGeometry(QRect(514, 364, 79, 31))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.register_title_text.setFont(font1)
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(36, 246, 251, 58))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.username_register_text_2 = QLabel(self.layoutWidget)
        self.username_register_text_2.setObjectName(u"username_register_text_2")
        self.username_register_text_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.username_register_text_2)

        self.username_register_textbox_2 = QLineEdit(self.layoutWidget)
        self.username_register_textbox_2.setObjectName(u"username_register_textbox_2")
        font2 = QFont()
        font2.setPointSize(13)
        self.username_register_textbox_2.setFont(font2)

        self.verticalLayout_8.addWidget(self.username_register_textbox_2)

        self.container_password_email = QWidget(self.widget)
        self.container_password_email.setObjectName(u"container_password_email")
        self.container_password_email.setGeometry(QRect(321, 75, 258, 287))
        self.verticalLayout_9 = QVBoxLayout(self.container_password_email)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.password_register_text = QLabel(self.container_password_email)
        self.password_register_text.setObjectName(u"password_register_text")
        self.password_register_text.setFont(font1)

        self.verticalLayout_2.addWidget(self.password_register_text)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.container_password_email)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(8)
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.container_password_email)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.container_password_email)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.container_password_email)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.container_password_email)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.password_register_textbox = QLineEdit(self.container_password_email)
        self.password_register_textbox.setObjectName(u"password_register_textbox")
        self.password_register_textbox.setFont(font2)

        self.verticalLayout_3.addWidget(self.password_register_textbox)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.show_password_register_checkbox = QCheckBox(self.container_password_email)
        self.show_password_register_checkbox.setObjectName(u"show_password_register_checkbox")

        self.verticalLayout_4.addWidget(self.show_password_register_checkbox)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.confirm_password_register_text = QLabel(self.container_password_email)
        self.confirm_password_register_text.setObjectName(u"confirm_password_register_text")
        self.confirm_password_register_text.setFont(font1)

        self.verticalLayout_7.addWidget(self.confirm_password_register_text)

        self.confirm_password_register_textbox = QLineEdit(self.container_password_email)
        self.confirm_password_register_textbox.setObjectName(u"confirm_password_register_textbox")
        self.confirm_password_register_textbox.setFont(font2)

        self.verticalLayout_7.addWidget(self.confirm_password_register_textbox)

        self.show_confirm_password_register_checkbox = QCheckBox(self.container_password_email)
        self.show_confirm_password_register_checkbox.setObjectName(u"show_confirm_password_register_checkbox")

        self.verticalLayout_7.addWidget(self.show_confirm_password_register_checkbox)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.container_password_rules = QWidget(self.widget)
        self.container_password_rules.setObjectName(u"container_password_rules")
        self.container_password_rules.setGeometry(QRect(35, 143, 252, 58))
        self.verticalLayout_5 = QVBoxLayout(self.container_password_rules)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.email_register_text = QLabel(self.container_password_rules)
        self.email_register_text.setObjectName(u"email_register_text")
        self.email_register_text.setFont(font1)

        self.verticalLayout_5.addWidget(self.email_register_text)

        self.email_register_textbox = QLineEdit(self.container_password_rules)
        self.email_register_textbox.setObjectName(u"email_register_textbox")
        self.email_register_textbox.setMinimumSize(QSize(250, 0))
        self.email_register_textbox.setFont(font2)

        self.verticalLayout_5.addWidget(self.email_register_textbox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1053, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.register_reg_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.register_title_text.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.username_register_text_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_register_text.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password must have:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Atleast 1 Upper case letter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Atleast 1 Number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Atleast 1 Lower Case Letter", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Minimum of 8 characters", None))
        self.show_password_register_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.confirm_password_register_text.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.show_confirm_password_register_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.email_register_text.setText(QCoreApplication.translate("MainWindow", u"Email", None))
    # retranslateUi

