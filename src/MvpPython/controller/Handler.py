import os.path

from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem
from signver.utils import data_utils
from model.SignaturesFinder import Localization_Predictions


class Handler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.file_path = ""
        self.view.chooseImageButton.clicked.connect(self.select_image)
        self.view.findSignaturesButton.clicked.connect(self.find_signatures)
        self.view.originalImageView.setScene(self.view.originalImageScene)
        self.view.processedImageView.setScene(self.view.processedImageScene)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.file_path = file_path
            self.load_image(file_path)

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.view.originalImageScene.clear()
        self.view.originalImageScene.addItem(pixmap_item)

    def load_new_image(self):
        self.find_signatures(os.path.abspath(self.file_path))

    def find_signatures(self, file_path):
        image_np = data_utils.img_to_np_array(file_path)
        prediction = Localization_Predictions()
        pixmap_item = QGraphicsPixmapItem(prediction.get_localization_predict())
        self.view.processedImageScene.clear()
        self.view.processedImageScene.addItem(pixmap_item)
