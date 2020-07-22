from PyQt5 import QtWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    xpos    = 200
    ypos    = 200
    width   = 300
    height  = 300

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("TechWithNathan")

    win.show()
    sys.exit(app.exec_())
