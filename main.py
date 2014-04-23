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
        QtCore.QObject.connect(self.ui.Button_LoadOutFileCandidate,QtCore.SIGNAL("clicked()"), self.LoadOutFileCandidate)
        QtCore.QObject.connect(self.ui.testButton,QtCore.SIGNAL("clicked()"), self.RunProgram)
        QtCore.QObject.connect(self.ui.Button_AddOutFromCandidate,QtCore.SIGNAL("clicked()"), self.AddOutFromCandidate)
        QtCore.QObject.connect(self.ui.Button_ShowRaport,QtCore.SIGNAL("clicked()"), self.ShowRaport)

#1        
    def RunProgram(self):
        value=self.ui.progressBar_StartProgram.value()+23
        self.ui.progressBar_StartProgram.setValue(value)
        if(value>99):
            self.ui.stackedWidget.setCurrentIndex(1)


#2    
    
    def Next1_Button(self):
        self.source.PrepareMainFile()
        self.source.configName=self.ui.lineEdit_LoadMainFile_Name.displayText() 
        self.source.CreateConfig()
        self.ui.testText.setText(self.source.mainFile.FromListToTxt(self.source.mainFile.hashedText))
        self.ui.stackedWidget.setCurrentIndex(2)

            
  
    def LoadMainFile_Button(self):
        self.ui.lineEdit_LoadMainFile_Name.setText("XD")
        path=self.source.SearchFile()
        self.ui.Line_LoadMainFile_Path.setText(path)
        self.source.pathToMainFile=path
    
#3
    def LoadOutFileCandidate(self):
        path=self.source.SearchFile()
        self.ui.Line_LoadOutFile_Path.setText(path)
        self.source.AddOutFileCandidate(path)
        self.ui.listWidget_CandidateOutFiles.clear()
        for path in self.source.OutFilesCandidate:
            self.ui.listWidget_CandidateOutFiles.addItem(path)

        
    def AddOutFromCandidate(self):
        self.source.GenerateOutFile(self.source.OutFilesCandidate)
        self.ui.listWidget_CandidateOutFiles.clear()
        self.ui.listWidget_OutFiles.clear()
        for outFile in self.source.OutFiles:
            self.ui.listWidget_OutFiles.addItem(outFile.fileName)
    
    def ShowRaport(self):
        self.ui.stackedWidget.setCurrentIndex(3) 
        for sentence in self.source.mainFile.clearText:
            self.ui.listWidget_MainFile.addItem(sentence)
            print sentence
        for outFile in self.source.OutFiles:
            self.ui.listWidget_OutFilesList.addItem(outFile.fileName)
        for sentence in self.source.OutFiles[0].clearText:
            self.ui.listWidget_ChoosenOutFile.addItem(sentence)

    #4
            


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app_holder=app.setActiveWindow(MainWindow)
    ui = Ui_MainWindow()
    ui_holder=ui.setupUi(MainWindow)
    myapp = StartQT4()
    myapp_holder=myapp.show()
    sys_holder=sys.exit(app.exec_())
    myapp_runprogram_hollder=myapp.RunProgram()