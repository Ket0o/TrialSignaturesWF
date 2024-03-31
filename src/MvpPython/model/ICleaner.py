import abc


class ICleaner(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def clean_all_image(self, folder: str = ".", extensions: [] = [".png", ".jpg"]) -> str:
        """Convert data from file to another format and return path"""
        raise NotImplementedError
