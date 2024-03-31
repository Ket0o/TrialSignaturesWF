import fitz
from model.IConverter import IConverter


class PdfToImageConverter(IConverter):
    @staticmethod
    def convert_data(file_path, file_name, output_folder=".", **kwargs) -> str:
        doc = fitz.open(file_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        image_path = f"{output_folder}/{file_name}.png"
        pix.writePNG(image_path)
        return image_path
