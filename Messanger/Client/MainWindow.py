from PySide6.QtWidgets import QMainWindow
# from Python.Messanger.Client.ui_client import Ui_MainWindow

from ui_client import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        

