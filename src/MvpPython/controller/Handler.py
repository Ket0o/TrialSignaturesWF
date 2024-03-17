from PIL import Image
from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem
from model.SignaturesFinder import Localization_Predictions


class Handler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.prediction = None
        self.first_file_path = None
        self.second_file_path = None

        self.view.chooseImageButton.clicked.connect(lambda: self.select_image(self.view.originalImageScene,
                                                                              self.view.chooseImageButton))
        self.view.secondChooseImageButton.clicked.connect(lambda: self.select_image(self.view.secondOriginalImageScene,
                                                                                    self.view.secondChooseImageButton))


        self.view.findSignaturesButton.clicked.connect(lambda: self.show_image(
            self.view.signaturesList, self.first_file_path,
            self.view.secondSignaturesList, self.second_file_path
        ))
        self.view.compareSignaturesButton.clicked.connect(self.compare_signatures)

        self.view.signaturesList.clicked.connect(self.find_signatures)
        self.view.secondSignaturesList.clicked.connect(self.find_signatures)

        self.view.originalImageView.setScene(self.view.originalImageScene)
        self.view.secondOriginalImageView.setScene(self.view.secondOriginalImageScene)

        self.view.processedImageView.setScene(self.view.processedImageScene)
        self.view.secondProcessedImageView.setScene(self.view.secondProcessedImageScene)



    def select_image(self, scene, button):
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            if (button.objectName() == "chooseImageButton"):
                self.first_file_path = file_path
            else:
                self.second_file_path = file_path
            self.preparation_image(scene, file_path)

    def preparation_image(self, scene, file_path):
        pixmap = QPixmap(file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.clear()
        scene.addItem(pixmap_item)

    def show_image(self, firstSignaturesList, first_file_path, secondSignaturesList, second_file_path):
        self.load_new_image(firstSignaturesList, first_file_path)
        self.load_new_image(secondSignaturesList, second_file_path)

    def load_new_image(self, signaturesList, file_path):
        self.prediction = Localization_Predictions(file_path)
        self.prediction.create_list_signatures()
        #TODO: разделить подписи с разных изображений
        signatures = self.prediction.signatures
        self.signatures_list(signatures, signaturesList)

    def find_signatures(self, scene, signaturesList, signatures):
        scene.clear()
        #TODO: сделать разделение сохранения
        Image.fromarray(signatures[signaturesList.currentIndex().row()]).save('firstOutput.png')
        first_pixmap_item = QGraphicsPixmapItem(QPixmap('firstOutput.png'))
        scene.addItem(first_pixmap_item)

    def signatures_list(self, signatures, signaturesList):
        count = 1
        model = QStandardItemModel()
        for signature in signatures:
            item = QStandardItem(f"{count}. Signature")
            model.appendRow(item)
            count += 1
        signaturesList.setModel(model)

    def compare_signatures(self):
        first_signature = self.prediction.get_signature(self.view.signaturesList.currentIndex().row())
        second_signature = self.secondPredication.get_signature(self.view.secondSignaturesList.currentIndex().row())
        result = self.prediction.verify_signature(first_signature, second_signature)
        self.view.resultTextBrowser.append(str(result))
