from PIL import Image
from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem
from model.SignaturesFinder import Localization_Predictions


class Handler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.file_path = None
        self.prediction = None
        self.model = QStandardItemModel()

        self.view.chooseImageButton.clicked.connect(self.select_image)
        self.view.findSignaturesButton.clicked.connect(self.load_new_image)

        self.view.signaturesList.clicked.connect(self.find_signatures)
        self.view.originalImageView.setScene(self.view.originalImageScene)
        self.view.processedImageView.setScene(self.view.processedImageScene)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.file_path = file_path
            self.load_image()

    def load_image(self):
        pixmap = QPixmap(self.file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.view.originalImageScene.clear()
        self.view.originalImageScene.addItem(pixmap_item)

    def load_new_image(self):
        self.prediction = Localization_Predictions(self.file_path)
        self.prediction.create_list_signatures()
        self.signatures_list()

    def find_signatures(self):
        self.view.processedImageScene.clear()
        Image.fromarray(self.prediction.signatures[self.view.signaturesList.currentIndex().row()]).save('output.png')
        pixmap_item = QGraphicsPixmapItem(QPixmap('output.png'))
        self.view.processedImageScene.addItem(pixmap_item)

    def signatures_list(self):
        count = 1
        for signature in self.prediction.signatures:
            item = QStandardItem(f"{count}. Signature")
            self.model.appendRow(item)
            count += 1
        self.view.signaturesList.setModel(self.model)

