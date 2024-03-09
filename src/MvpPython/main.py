
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import view.View
from controller.Handler import Handler

app = QApplication(sys.argv)
window = view.View.SignaturesDetector()
handler = Handler(window)
window.show()
app.exec()