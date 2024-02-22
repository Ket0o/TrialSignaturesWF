from PySide6.QtWidgets import QMainWindow, QGraphicsScene
from view.MainWindow import Ui_MainWindow

class SignaturesDetector(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.originalImageView.setScene(self.scene)

