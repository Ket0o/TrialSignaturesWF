# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QListView,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 691)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Times New Roman;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 10, 611, 671))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.originalImageView = QGraphicsView(self.layoutWidget)
        self.originalImageView.setObjectName(u"originalImageView")

        self.verticalLayout_2.addWidget(self.originalImageView)

        self.processedImageView = QGraphicsView(self.layoutWidget)
        self.processedImageView.setObjectName(u"processedImageView")

        self.verticalLayout_2.addWidget(self.processedImageView)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 161, 671))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.choseImageLabel = QLabel(self.layoutWidget1)
        self.choseImageLabel.setObjectName(u"choseImageLabel")
        self.choseImageLabel.setTextFormat(Qt.AutoText)

        self.verticalLayout.addWidget(self.choseImageLabel)

        self.chooseImageButton = QPushButton(self.layoutWidget1)
        self.chooseImageButton.setObjectName(u"chooseImageButton")

        self.verticalLayout.addWidget(self.chooseImageButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.signaturesList = QListView(self.layoutWidget1)
        self.signaturesList.setObjectName(u"signaturesList")

        self.verticalLayout_3.addWidget(self.signaturesList)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438", None))
        self.choseImageLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435:", None))
        self.chooseImageButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

