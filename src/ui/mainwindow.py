'''
Created on Oct 24, 2015

@author: anon
'''
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextBrowser
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import *

#src. for paydev parser
from src.ui.ui_mainwindow import Ui_MainWindow
from src.dictionaries.jmdict import JMDict
from src.dictionaries.deinflecter import Deinflecter

#@PydevCodeAnalysisIgnore
from lxml import etree as ET

class MainWindow(QMainWindow):
    ui = Ui_MainWindow()
    di = JMDict()
    de = Deinflecter()
    
    def __init__(self):
        super().__init__();        
        self.ui.setupUi(self)
        self.ui.textInput.textChanged.connect(self.inputTextChanged)
        
    @pyqtSlot()
    def inputTextChanged(self):
        text = MainWindow.ui.textInput.toPlainText()
        
        res = MainWindow.de.deinflectWord(text)
        #print(res)

        directHits = [MainWindow.di[w.deinflected] for w in res]
        #Flatten
        directHits = [item for sublist in directHits for item in sublist]
        for it in directHits:
            ET.dump(it)
        frame = MainWindow.ui.frameInfo
        layout = QtWidgets.QVBoxLayout()
        #print(directHits)
        #print (frame.layout())
        for hit in directHits:
            #print(MainWindow.di.toHTML(hit))
            txt = QTextBrowser()
            txt.setHtml(str(MainWindow.di.toHTML(hit)))
            layout.addWidget(txt)
        
        
            
        QWidget().setLayout(frame.layout())
        frame.setLayout(layout)

