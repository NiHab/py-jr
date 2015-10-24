'''
Created on Oct 24, 2015

@author: anon
'''
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextBrowser
from PyQt5.QtCore import QObject, pyqtSlot
import timeit


#src. for pydev parser
from src.ui.ui_mainwindow import Ui_MainWindow

from src.dictionaries.lookup import Lookup

class MainWindow(QMainWindow):

    ui = Ui_MainWindow()
    
    def __init__(self):
        super().__init__();        
        self.ui.setupUi(self)
        self.ui.textInput.selectionChanged.connect(self.selectionChanged)
        #self.ui.textInput.cursorPositionChanged.connect(self.cursorPositionChanged)
        self.l = Lookup()
        
        self.previousSelection = ''
        self.lastLookup = timeit.default_timer()
        
        
    #TODO: Optimize, don't do full lookup
    def hasResults(self, text):
        return self.l.lookup(text)[1] > 0
        
    def doLookup(self, text):
        if not (text == self.previousSelection):         
        
            if timeit.default_timer() - self.lastLookup > 0.100:
                #print('lookup')
                res = self.l.lookup(text, asHtml=True)  
                MainWindow.ui.textBrowser.setHtml(res[0])
                self.previousSelection = text
                self.lastLookup = timeit.default_timer()

    
#===============================================================================
#     @pyqtSlot()
#     def cursorPositionChanged(self):
#         pos = (MainWindow.ui.textInput.textCursor().anchor())
# 
#         
#         n = 0
#         txt = MainWindow.ui.textInput.document().characterAt(pos)
#         while self.hasResults(txt):
#             n += 1
#             txt += MainWindow.ui.textInput.document().characterAt(pos + n)
#         
#         print(txt, txt[:-1])
#         self.doLookup(txt[:-1])
#===============================================================================
        
        
        
    
    @pyqtSlot()
    def selectionChanged(self):        
        self.doLookup(MainWindow.ui.textInput.textCursor().selectedText())
        

