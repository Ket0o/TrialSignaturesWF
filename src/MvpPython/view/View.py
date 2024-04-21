import os
from PySide6.QtWidgets import QMainWindow, QGraphicsScene
from model.Implementation.Cleaner import Cleaner
from view.MainWindow import Ui_MainWindow


class SignaturesDetector(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.originalImageScene = QGraphicsScene()
        self.secondOriginalImageScene = QGraphicsScene()
        self.processedImageScene = QGraphicsScene()
        self.secondProcessedImageScene = QGraphicsScene()
        self.originalImageView.setScene(self.originalImageScene)
        self.secondOriginalImageView.setScene(self.secondOriginalImageScene)
        self.processedImageView.setScene(self.processedImageScene)
        self.secondProcessedImageView.setScene(self.secondProcessedImageScene)

    def closeEvent(self, event):
        Cleaner.clean_all_image(os.path.join(os.path.dirname(__file__), '..', 'images'))
        event.accept()
