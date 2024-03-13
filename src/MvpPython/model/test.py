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
from SignaturesFinder import Localization_Predictions

file_path = '/home/danil/PycharmProjects/TrialSignaturesWF/src/MvpPython/model/contract-signature-page-example-new-elgin-munity-college-faculty-association-eccfa-of-contract-signature-page-example.png'

P = Localization_Predictions(file_path)
cl_si = P.get_localization_predict()
plot_np_array(cl_si).show()
sign1 = P.get_signature(0)
plot_np_array(sign1).show()
sign2 = P.get_signature(1)
sign3 = P.get_signature(0)


print(P.verify_signature(sign1,sign2))
print(P.verify_signature(sign1,sign1))

