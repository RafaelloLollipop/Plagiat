# -*- coding: utf-8 -*-
#pyuic4 gui.ui > gui.py
from os import path
from Tkinter import Tk
from tkFileDialog import askopenfilename
import sys
import time
from PyQt4 import QtCore, QtGui

sys.path.append(path.abspath('./Class'))
from Source import Source

from gui import Ui_MainWindow

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # nazwa klasy
        self.source=Source()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.Button_LoadMainFile,QtCore.SIGNAL("clicked()"), self.LoadMainFile_Button)
        QtCore.QObject.connect(self.ui.Button_Next1,QtCore.SIGNAL("clicked()"), self.Next1_Button)
        QtCore.QObject.connect(self.ui.Button_Next2,QtCore.SIGNAL("clicked()"), self.Next1_Button)
        QtCore.QObject.connect(self.ui.Back_Button,QtCore.SIGNAL("clicked()"), self.Back_Button)
        QtCore.QObject.connect(self.ui.testButton,QtCore.SIGNAL("clicked()"), self.RunProgram)

        
    def RunProgram(self):
        value=self.ui.progressBar_StartProgram.value()+23
        self.ui.progressBar_StartProgram.setValue(value)
        if(value>99):
            self.ui.stackedWidget.setCurrentIndex(1)
        
    def LoadMainFile_Button(self):
        text=self.source.SearchFile()
        self.ui.Line_LoadMainFile.setText(text)
        
    def Next1_Button(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def Back_Button(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        

        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app.setActiveWindow(MainWindow)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
    myapp.RunProgram()


 
