from src.MvpPython.signver.detector import Detector
from src.MvpPython.signver.cleaner import Cleaner
from src.MvpPython.signver.extractor import MetricExtractor
from src.MvpPython.signver.matcher import Matcher
from src.MvpPython.signver.utils import data_utils, visualization_utils
from src.MvpPython.signver.utils.data_utils import invert_img, resnet_preprocess
from src.MvpPython.signver.utils.visualization_utils import plot_np_array, visualize_boxes, get_image_crops, make_square

import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
from new import Localization_Predictions

file_path = '/home/danil/PycharmProjects/TrialSignaturesMVP/src/MvpPython/model/testFile.png'

image_np = data_utils.img_to_np_array(file_path)
P = Localization_Predictions()
# plot_np_array(P.get_localization_predict(),title="Document and Extracted Signatures").show()
# plot_np_array(P.get_signature(2)).show()
print(type(P.get_localization_predict()))
print(P.invert_image().__doc__)
