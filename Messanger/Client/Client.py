from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication 
from PySide6.QtGui import QWindow


import sys

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec())
    
