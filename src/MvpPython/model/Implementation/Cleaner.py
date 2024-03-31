from model.ICleaner import ICleaner
import os


class Cleaner(ICleaner):
    @staticmethod
    def clean_all_image(folder: str , extension: str = ".png", **kwargs) -> str:
        for filename in os.listdir(folder):
            if filename.endswith(extension):
                os.remove(os.path.join(folder, filename))
