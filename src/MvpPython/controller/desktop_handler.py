from PIL import Image
from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem

from model.Implementation.PdfToImageConverter import PdfToImageConverter
from model.Implementation.SignaturesFinder import Localization_Predictions


class Handler(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.prediction = None
        self.first_file_path = None
        self.second_file_path = None
        self.first_signatures = None
        self.second_signatures = None
        self.first_model = QStandardItemModel()
        self.second_model = QStandardItemModel()

        self.view.chooseImageButton.clicked.connect(lambda: self.select_image(self.view.originalImageScene,
                                                                              self.view.chooseImageButton))
        self.view.secondChooseImageButton.clicked.connect(lambda: self.select_image(self.view.secondOriginalImageScene,
                                                                                    self.view.secondChooseImageButton))


        self.view.findSignaturesButton.clicked.connect(lambda: self.show_image(
            self.view.signaturesList, self.first_file_path,
            self.view.secondSignaturesList, self.second_file_path
        ))
        self.view.compareSignaturesButton.clicked.connect(lambda: self.compare_signatures(
            self.view.signaturesList,
            self.view.secondSignaturesList,
            self.view.resultTextBrowser
        ))

        self.view.signaturesList.clicked.connect(lambda: self.find_signatures(self.view.processedImageScene,
                                                                              self.view.signaturesList,
                                                                              self.first_signatures))
        self.view.secondSignaturesList.clicked.connect(lambda: self.find_signatures(self.view.secondProcessedImageScene,
                                                                                    self.view.secondSignaturesList,
                                                                                    self.second_signatures))

        self.view.originalImageView.setScene(self.view.originalImageScene)
        self.view.secondOriginalImageView.setScene(self.view.secondOriginalImageScene)

        self.view.processedImageView.setScene(self.view.processedImageScene)
        self.view.secondProcessedImageView.setScene(self.view.secondProcessedImageScene)

    def select_image(self, scene, button):
        scene.clear()
        file_path, _ = QFileDialog.getOpenFileName(
            self.view, "Select Image", "", "Images (*.png *.jpg *.jpeg *.pdf)"
        )
        if file_path:
            if (button.objectName() == "chooseImageButton"):
                self.first_file_path \
                    = PdfToImageConverter.convert_data(
                    file_path=file_path,
                    file_name="first_image",
                    output_folder='images') \
                    if file_path.split('.')[-1] == 'pdf' \
                    else file_path
                self.clear_components(
                    {self.first_model},
                    {self.view.originalImageScene, self.view.processedImageScene},
                    {self.view.resultTextBrowser})
            else:
                self.second_file_path \
                    = PdfToImageConverter.convert_data(
                    file_path=file_path,
                    file_name="second_image",
                    output_folder='images') \
                    if file_path.split('.')[-1] == 'pdf' \
                    else file_path
                self.clear_components(
                    {self.second_model},
                    {self.view.secondOriginalImageScene, self.view.secondProcessedImageScene},
                    {self.view.resultTextBrowser})
            self.preparation_image(scene, file_path)

    def preparation_image(self, scene, file_path):
        pixmap = QPixmap(file_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.clear_components(None, {scene}, None)
        scene.addItem(pixmap_item)

    def show_image(self, firstSignaturesList, first_file_path, secondSignaturesList, second_file_path):
        self.clear_components(
            {self.first_model, self.second_model},
            {self.view.processedImageScene, self.view.secondProcessedImageScene},
            {self.view.resultTextBrowser})
        self.load_new_image(firstSignaturesList, first_file_path)
        self.load_new_image(secondSignaturesList, second_file_path)

    def load_new_image(self, signaturesList, file_path):
        self.prediction = Localization_Predictions(file_path)
        self.prediction.create_list_signatures()
        if (signaturesList.objectName() == "signaturesList"):
            self.first_signatures = self.prediction.signatures
        else:
            self.second_signatures = self.prediction.signatures
        self.signatures_list(self.prediction.signatures, signaturesList)

    def find_signatures(self, scene, signaturesList, signatures):
        self.clear_components(None, {scene}, None)
        if (signaturesList.objectName() == "signaturesList"):
            Image.fromarray(signatures[signaturesList.currentIndex().row()]).save('images/firstOutput.png')
            first_pixmap_item = QGraphicsPixmapItem(QPixmap('images/firstOutput.png'))
        else:
            Image.fromarray(signatures[signaturesList.currentIndex().row()]).save('images/secondOutput.png')
            first_pixmap_item = QGraphicsPixmapItem(QPixmap('images/secondOutput.png'))

        scene.addItem(first_pixmap_item)

    def signatures_list(self, signatures, signaturesList):
        count = 1
        model = QStandardItemModel()
        for signature in signatures:
            item = QStandardItem(f"{count}. Signature")
            model.appendRow(item)
            count += 1
        if (signaturesList.objectName() == "signaturesList"):
            self.first_model = model
        else:
            self.second_model = model
        signaturesList.setModel(model)

    def compare_signatures(self, firstSignaturesList, secondSignaturesList, resultTextBrowser):
        self.clear_components(None, None, {resultTextBrowser})
        first_signature = self.first_signatures[firstSignaturesList.currentIndex().row()]
        second_signature = self.second_signatures[secondSignaturesList.currentIndex().row()]
        result = self.prediction.verify_signature(first_signature, second_signature)
        resultTextBrowser.append(str(result))

    def clear_components(self, models, scenes, textBrowsers):
        if models is not None:
            for model in models:
                model.clear()
        if scenes is not None:
            for scene in scenes:
                scene.clear()
        if textBrowsers is not None:
            for textBrowser in textBrowsers:
                textBrowser.clear()