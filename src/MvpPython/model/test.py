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
from Implementation.SignaturesFinder import Localization_Predictions

#file_path = '/home/danil/PycharmProjects/TrialSignaturesWF/src/MvpPython/model/contract-signature-page-example-new-elgin-munity-college-faculty-association-eccfa-of-contract-signature-page-example.png'
file_path = '/home/danil/PycharmProjects/TrialSignaturesWF/src/MvpPython/model/test1.png'
P = Localization_Predictions(file_path)
cl_si = P.get_localization_predict()
plot_np_array(cl_si).show()


