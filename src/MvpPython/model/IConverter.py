import abc


class IConverter(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def convert_data(self, file_path: str, file_name, output_folder: str = ".") -> str:
        """Convert data from file to another format and return path"""
        raise NotImplementedError
