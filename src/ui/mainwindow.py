'''
Created on Oct 24, 2015

@author: anon
'''
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextBrowser
from PyQt5.QtCore import QObject, pyqtSlot


#src. for pydev parser
from src.ui.ui_mainwindow import Ui_MainWindow

from src.dictionaries.lookup import Lookup

class MainWindow(QMainWindow):

    ui = Ui_MainWindow()
    
    def __init__(self):
        super().__init__();        
        self.ui.setupUi(self)
        self.ui.textInput.textChanged.connect(self.inputTextChanged)
        self.l = Lookup()
        
    @pyqtSlot()
    def inputTextChanged(self):
        text = MainWindow.ui.textInput.toPlainText()
        
        #self.l.lookup(text)
        
        MainWindow.ui.textBrowser.setHtml(self.l.lookup(text, asHtml=True))

