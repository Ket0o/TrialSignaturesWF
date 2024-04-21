import sys
from PySide6.QtWidgets import QApplication
import view.View
from controller.desktop_handler import Handler

app = QApplication(sys.argv)
window = view.View.SignaturesDetector()
handler = Handler(window)
window.show()
app.exec()