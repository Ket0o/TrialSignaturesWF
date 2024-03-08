from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem


class Handler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.file_path = None
        self.view.chooseImageButton.clicked.connect(self.select_image)
        self.view.originalImageView.setScene(self.view.scene)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.view.scene.clear()
        self.view.scene.addItem(pixmap_item)

    def get_file_path(self):
        return self.file_path
