from curses import window
import PyQt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://www.duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

app=QApplication(sys.argv)
QApplication.setApplicationName("Świątynia")
window=MainWindow()
app.exec()

