from signver.detector import Detector
from signver.cleaner import Cleaner
from signver.extractor import MetricExtractor
from signver.matcher import Matcher
from signver.utils import data_utils, visualization_utils
from signver.utils.data_utils import invert_img, resnet_preprocess
from signver.utils.visualization_utils import plot_np_array, visualize_boxes, get_image_crops, make_square

import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt


class Localization_Predictions:
    def __init__(self):
        super().__init__()
        self.detector_model_path = 'C:/Users/Кирилл/PycharmProjects/TrialSignaturesWF/src/MvpPython/models/detector/small'
        self.detector = Detector()
        self.detector.load(self.detector_model_path)
        self.threshold = 0.22

    def invert_image(self, file_path):
        """
        Инвертирует изображение.
        :return:
        """
        data_utils.img_to_np_array(file_path)
        self.inverted_image_np = data_utils.img_to_np_array(file_path, invert_image=True)
        self.img_tensor = tf.convert_to_tensor(self.inverted_image_np)
        self.img_tensor = self.img_tensor[tf.newaxis, ...]


    def get_localization_predict(self):
        """
        Предсказывает нахождение подписей на изображении
        :return: размеченное изображение. Type: numpy.ndarray
        """
        self.invert_image()
        self.boxes, self.scores, self.classes, self.detections = self.detector.detect(self.img_tensor)
        self.annotated_image = visualize_boxes(self.image_np, self.boxes, self.scores, threshold=self.threshold, color="green")
        return self.annotated_image

    def create_list_signatures(self):
        """
        Создает список подписей
        :return:
        """
        self.get_localization_predict()
        self.signatures = get_image_crops(self.image_np, self.boxes, self.scores, self.threshold)

    def get_len_signatures(self):
        """
        Возвращает длину списка подписей
        :return: Type: int
        """
        self.create_list_signatures()
        return len(self.signatures)

    def get_signature(self,index):
        """
        Возвращает подпись из списка
        :param index: Индекс подписи
        :return: Подпись по индексу списка. Type: numpy.ndarray
        """
        self.create_list_signatures()
        return self.signatures[index]