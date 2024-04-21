import os

from PIL import Image

from model.Implementation.SignaturesFinder import Localization_Predictions


class Handler():
    def __init__(self):
        super().__init__()

    def get_captions_from_image(self, image):
        image.save("images/" + image.filename)
        predict = Localization_Predictions("images/" + image.filename)
        predict.create_list_signatures()
        count = 0
        for signature in predict.signatures:
            Image.fromarray(signature).save("images/signatures/" + str(count) + ".png")
            count += 1
        return predict.signatures

    def compare_two_signatures(self, first_signature, second_signature):
        predict = Localization_Predictions()
        result = predict.verify_signature(first_signature, second_signature)
        return result

