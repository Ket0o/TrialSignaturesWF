from PIL import Image
from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem
from model.SignaturesFinder import Localization_Predictions


class Handler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.firstPrediction = None
        self.first_file_path = None
        self.file_path = None
        self.second_file_path = None
        self.secondPredication = None
        self.first_model = QStandardItemModel()
        self.second_model = QStandardItemModel()

        self.view.chooseImageButton.clicked.connect(lambda: self.select_image(self.view.originalImageScene))
        self.view.secondChooseImageButton.clicked.connect(self.second_select_image)


        self.view.findSignaturesButton.clicked.connect(self.load_new_image)
        self.view.compareSignaturesButton.clicked.connect(self.compare_signatures)

        self.view.signaturesList.clicked.connect(self.first_find_signatures)
        self.view.secondSignaturesList.clicked.connect(self.second_find_signatures)
        self.view.originalImageView.setScene(self.view.originalImageScene)
        self.view.secondOriginalImageView.setScene(self.view.secondOriginalImageScene)
        self.view.processedImageView.setScene(self.view.processedImageScene)
        self.view.secondProcessedImageView.setScene(self.view.secondProcessedImageScene)



    def select_image(self, scene):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.file_path = file_path
            self.preparation_image(scene)

    def preparation_image(self, scene):
        pixmap = QPixmap(self.file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.clear()
        scene.addItem(pixmap_item)

    def second_select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.second_file_path = file_path
            self.second_preparation_image()

    def second_preparation_image(self):
        pixmap = QPixmap(self.second_file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.view.secondOriginalImageScene.clear()
        self.view.secondOriginalImageScene.addItem(pixmap_item)

    def load_new_image(self):
        self.firstPrediction = Localization_Predictions(self.file_path)
        self.secondPredication = Localization_Predictions(self.second_file_path)
        self.firstPrediction.create_list_signatures()
        self.secondPredication.create_list_signatures()
        self.first_signatures_list()
        self.second_signatures_list()

    def first_find_signatures(self):
        self.view.processedImageScene.clear()
        Image.fromarray(self.firstPrediction.get_signature(self.view.signaturesList.currentIndex().row())).save('firstOutput.png')
        first_pixmap_item = QGraphicsPixmapItem(QPixmap('firstOutput.png'))
        self.view.processedImageScene.addItem(first_pixmap_item)

    def second_find_signatures(self):
        self.view.secondProcessedImageScene.clear()
        Image.fromarray(self.secondPredication.get_signature(self.view.secondSignaturesList.currentIndex().row())).save('secondOutput.png')
        second_pixmap_item = QGraphicsPixmapItem(QPixmap('secondOutput.png'))
        self.view.secondProcessedImageScene.addItem(second_pixmap_item)

    def first_signatures_list(self):
        count = 1
        for signature in self.firstPrediction.signatures:
            item = QStandardItem(f"{count}. Signature")
            self.first_model.appendRow(item)
            count += 1
        self.view.signaturesList.setModel(self.first_model)

    def second_signatures_list(self):
        count = 1
        for signature in self.secondPredication.signatures:
            item = QStandardItem(f"{count}. Signature")
            self.second_model.appendRow(item)
            count += 1
        self.view.secondSignaturesList.setModel(self.second_model)

    def compare_signatures(self):
        first_signature = self.firstPrediction.get_signature(self.view.signaturesList.currentIndex().row())
        second_signature = self.secondPredication.get_signature(self.view.secondSignaturesList.currentIndex().row())
        result = self.firstPrediction.verify_signature(first_signature, second_signature)
        self.view.resultTextBrowser.append(str(result))
