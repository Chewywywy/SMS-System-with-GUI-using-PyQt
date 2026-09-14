# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_board_pecson.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
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
        self.widget.setGeometry(QRect(259, 122, 614, 405))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(31, 63, 521, 36))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_button = QPushButton(self.widget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(493, 349, 79, 24))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

