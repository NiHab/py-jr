'''
Created on Oct 23, 2015

@author: anon
'''
from src.dictionaries.jmdict import JMDict
from src.dictionaries.deinflecter import Deinflecter
from src.ui.mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication

import sys
if __name__ == '__main__':
    
    #===============================================================================
    # PROTOTYPE
    # ENTIRE DICT IS STORED IN MEMORY AS XMLTREE
    # EXPECT FIREFOX-LEVELS OF MEMORY USAGE
    #===============================================================================
            
    JMDict().load("../data/JMdict_e", "../data/transform.xml")
    Deinflecter().load("../data/inflections")
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())

    
