
from PySide6.QtWidgets import QMainWindow

from ui_client import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        

