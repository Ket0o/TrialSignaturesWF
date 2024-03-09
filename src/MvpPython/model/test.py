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
from SignaturesFinder import Localization_Predictions

file_path = 'C:/Users/Кирилл/PycharmProjects/TrialSignaturesWF/src/MvpPython/view/test.png'

image_np = data_utils.img_to_np_array(file_path)
P = Localization_Predictions()
# plot_np_array(P.get_localization_predict(),title="Document and Extracted Signatures").show()
# plot_np_array(P.get_signature(2)).show()
print(type(P.get_localization_predict()))
print(P.invert_image().__doc__)
