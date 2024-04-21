from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QListView,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1331, 830)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Times New Roman;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 10, 481, 671))
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

        self.findSignaturesButton = QPushButton(self.layoutWidget1)
        self.findSignaturesButton.setObjectName(u"findSignaturesButton")

        self.verticalLayout.addWidget(self.findSignaturesButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.signaturesList = QListView(self.layoutWidget1)
        self.signaturesList.setObjectName(u"signaturesList")

        self.verticalLayout_3.addWidget(self.signaturesList)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(670, 10, 481, 671))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.secondOriginalImageView = QGraphicsView(self.layoutWidget_2)
        self.secondOriginalImageView.setObjectName(u"secondOriginalImageView")

        self.verticalLayout_4.addWidget(self.secondOriginalImageView)

        self.secondProcessedImageView = QGraphicsView(self.layoutWidget_2)
        self.secondProcessedImageView.setObjectName(u"secondProcessedImageView")

        self.verticalLayout_4.addWidget(self.secondProcessedImageView)

        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(1160, 10, 161, 671))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.secondChoseImageLabel = QLabel(self.layoutWidget_3)
        self.secondChoseImageLabel.setObjectName(u"secondChoseImageLabel")
        self.secondChoseImageLabel.setTextFormat(Qt.AutoText)

        self.verticalLayout_6.addWidget(self.secondChoseImageLabel)

        self.secondChooseImageButton = QPushButton(self.layoutWidget_3)
        self.secondChooseImageButton.setObjectName(u"secondChooseImageButton")

        self.verticalLayout_6.addWidget(self.secondChooseImageButton)

        self.compareSignaturesButton = QPushButton(self.layoutWidget_3)
        self.compareSignaturesButton.setObjectName(u"compareSignaturesButton")

        self.verticalLayout_6.addWidget(self.compareSignaturesButton)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.compareSignaturesPlaneButton = QPushButton(self.layoutWidget_3)
        self.compareSignaturesPlaneButton.setObjectName(u"compareSignaturesPlaneButton")

        self.verticalLayout_5.addWidget(self.compareSignaturesPlaneButton)

        self.secondSignaturesList = QListView(self.layoutWidget_3)
        self.secondSignaturesList.setObjectName(u"secondSignaturesList")

        self.verticalLayout_5.addWidget(self.secondSignaturesList)

        self.resultTextBrowser = QTextBrowser(self.centralwidget)
        self.resultTextBrowser.setObjectName(u"resultTextBrowser")
        self.resultTextBrowser.setGeometry(QRect(10, 690, 1311, 131))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438", None))
        self.choseImageLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435:", None))
        self.chooseImageButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.findSignaturesButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043f\u043e\u0434\u043f\u0438\u0441\u0438", None))
        self.secondChoseImageLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435:", None))
        self.secondChooseImageButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.compareSignaturesButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438", None))
        self.compareSignaturesPlaneButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438", None))
    # retranslateUi