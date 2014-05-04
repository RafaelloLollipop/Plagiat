# -*- coding: utf-8 -*-
#pyuic4 gui.ui > gui.py
#QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
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
        QtCore.QObject.connect(self.ui.Button_LoadConfig,QtCore.SIGNAL("clicked()"), self.LoadConfig_Button)
        QtCore.QObject.connect(self.ui.Button_Next1,QtCore.SIGNAL("clicked()"), self.Next1_Button)
        QtCore.QObject.connect(self.ui.Button_Next2,QtCore.SIGNAL("clicked()"), self.Next2_Button)
        QtCore.QObject.connect(self.ui.Button_LoadOutFileCandidate,QtCore.SIGNAL("clicked()"), self.LoadOutFileCandidate)
        QtCore.QObject.connect(self.ui.Button_RemoveOutFileCandidate,QtCore.SIGNAL("clicked()"), self.RemoveOutFileCandidate)
        QtCore.QObject.connect(self.ui.Button_RemoveOutFile,QtCore.SIGNAL("clicked()"), self.RemoveOutFile)
        QtCore.QObject.connect(self.ui.Button_LoadOutFileCandidateFromWWW,QtCore.SIGNAL("clicked()"), self.LoadOutFileCandidateFromWWW)
        QtCore.QObject.connect(self.ui.testButton,QtCore.SIGNAL("clicked()"), self.RunProgram)
        QtCore.QObject.connect(self.ui.Button_AddOutFromCandidate,QtCore.SIGNAL("clicked()"), self.AddOutFromCandidate)
        QtCore.QObject.connect(self.ui.Button_ShowRaport,QtCore.SIGNAL("clicked()"), self.ShowRaport)
        QtCore.QObject.connect(self.ui.listWidget_OutFilesList,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.ChangeOutFile)
        QtCore.QObject.connect(self.ui.listWidget_MainFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_MainFileDClicked)
        QtCore.QObject.connect(self.ui.listWidget_ChoosenOutFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_ChoosenOutFileDClicked)
        QtCore.QObject.connect(self.ui.Button_BackToPage_2,QtCore.SIGNAL("clicked()"), self.Button_BackToPage_2)
        QtCore.QObject.connect(self.ui.Button_BackToPage_1,QtCore.SIGNAL("clicked()"), self.Button_BackToPage_1)
#0        
    def RunProgram(self):
        value=self.ui.progressBar_StartProgram.value()+23
        self.ui.progressBar_StartProgram.setValue(value)
        value= 100
        if(value>99):
            self.ui.stackedWidget.setCurrentIndex(1)


#1    
    
    def InicializeWWWlist(self):
        list= self.source.GetAdressFromMainFile()
        for adress in list:
            self.ui.listWidget_wwwFromMainFile.addItem(adress)
    
    def Next1_Button(self):
        self.source.PrepareMainFile()
        self.source.configName=self.ui.lineEdit_LoadMainFile_Name.displayText() 
        self.source.CreateConfig()
        self.InicializeWWWlist()
        self.ui.stackedWidget.setCurrentIndex(2)

            
    def Next2_Button(self):
        self.source.LoadConfig()
        self.ui.stackedWidget.setCurrentIndex(2)

    
    def LoadMainFile_Button(self):
        self.ui.lineEdit_LoadMainFile_Name.setText("XD")
        path=self.source.SearchFile()
        self.ui.Line_LoadMainFile_Path.setText(path)
        self.source.pathToMainFile=path
        
    def LoadConfig_Button(self):
        path=self.source.SearchConfig()
        self.ui.Line_LoadConfig_Path.setText(path)
        self.source.pathToMainFile=path
    
#2

    
    def LoadOutFileCandidateFromWWW(self):
        list= self.source.GetAdressFromMainFile()
        currentRow=self.ui.listWidget_wwwFromMainFile.currentRow()
        path=list[currentRow]
        self.source.AddOutFileCandidate(path)
        self.ui.listWidget_CandidateOutFiles.clear()
        for path in self.source.OutFilesCandidate:
            self.ui.listWidget_CandidateOutFiles.addItem(path)

    
    def RemoveOutFileCandidate(self):
        list= self.source.GetAdressFromMainFile()
        currentRow=self.ui.listWidget_CandidateOutFiles.currentRow()
        self.source.RemoveOutFileCandidate(currentRow)
        self.ui.listWidget_CandidateOutFiles.clear()
        for path in self.source.OutFilesCandidate:
            self.ui.listWidget_CandidateOutFiles.addItem(path)    
    
    def LoadOutFileCandidate(self):
        path=self.source.SearchFile()
        self.ui.Line_LoadOutFile_Path.setText(path)
        self.source.AddOutFileCandidate(path)
        self.ui.listWidget_CandidateOutFiles.clear()
        for path in self.source.OutFilesCandidate:
            self.ui.listWidget_CandidateOutFiles.addItem(path)
    
    def RemoveOutFile(self):
        currentRow=self.ui.listWidget_OutFiles.currentRow()
        self.ui.listWidget_OutFiles.clear()
        if(self.source.RemoveOutFile(currentRow)):

            for outFile in self.source.OutFiles:
                print path
                self.ui.listWidget_OutFiles.addItem(outFile.GetFileName())   

    def AddOutFromCandidate(self):
        self.source.GenerateOutFile(self.source.OutFilesCandidate)
        self.ui.listWidget_CandidateOutFiles.clear()
        self.ui.listWidget_OutFiles.clear()
        for outFile in self.source.OutFiles:
            self.ui.listWidget_OutFiles.addItem(outFile.GetFileName())
    
    def ShowRaport(self):
        self.source.GenerateRaport() # Create raport
        print self.source.raportStructure
        self.ui.stackedWidget.setCurrentIndex(3)  # Change scene
        self.ui.listWidget_MainFile.clear()
        for sentence in self.source.GetMainFileClearText():  # show MainFile text to left widget 
            self.ui.listWidget_MainFile.addItem(sentence) 
            
        self.ui.listWidget_OutFilesList.clear()
        for outFile in self.source.GetOutFiles():  # make list of outfiles in top widget
            self.ui.listWidget_OutFilesList.addItem(outFile.fileName)  
            self.ui.listWidget_ChoosenOutFile.clear()
            for sentence in outFile.GetClearText():   # show acutal OutFile text            
                self.ui.listWidget_ChoosenOutFile.addItem(sentence)
        self.ui.listWidget_OutFilesList.setCurrentRow(0)     #default start watching from '0' index file
        
        self.ColorMainFile()        
    
    def ColorMainFile(self):    
        ListOfSentencesToColor=self.source.ListOfMainFileSentenceToColor()
        colors=self.GetColors()
        colorIt=-1
        for outFile in ListOfSentencesToColor:
            colorIt+=1
            color=colors[colorIt]
            for number in outFile:
                item=self.ui.listWidget_MainFile.item(number)
                item.setBackgroundColor(color)
            
    def GetColors(self):
        colors=[]
        colors.append(QtGui.QColor(176,23,31))
        colors.append(QtGui.QColor(65,105,225))
        colors.append(QtGui.QColor(93,71,139))
        colors.append(QtGui.QColor(238,162,173))
        colors.append(QtGui.QColor(39   , 64  ,  139))
        colors.append(QtGui.QColor(189    ,252   , 201))
        colors.append(QtGui.QColor(139   , 117  ,  0))
        colors.append(QtGui.QColor(61    ,145 ,   64    ))
        colors.append(QtGui.QColor(124  ,  252  ,  0))
        colors.append(QtGui.QColor(255  ,  246  ,  143))
        colors.append(QtGui.QColor(0   , 245 ,   255))
        colors.append(QtGui.QColor(222  ,  184 ,   135))
        colors.append(QtGui.QColor(238  ,  118  ,  0))
        colors.append(QtGui.QColor(238  ,  149  ,  114))
        colors.append(QtGui.QColor(205   , 201  ,  201))
        colors.append(QtGui.QColor(56  ,  142,    142    ))
        colors.append(QtGui.QColor(113  ,  198  ,  113))
        colors.append(QtGui.QColor(198  ,  113   , 113))

        return colors        
    def UpdateRaport(self):
        currentRow=self.ui.listWidget_OutFilesList.currentRow()
        print currentRow
        self.ui.listWidget_ChoosenOutFile.clear()
        for sentence in self.source.OutFiles[currentRow].clearText:
            self.ui.listWidget_ChoosenOutFile.addItem(sentence)
    
    def ChangeOutFile(self):
        self.UpdateRaport()
    def Button_BackToPage_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    #3    
    def Button_BackToPage_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def listWidget_MainFileDClicked(self):
        currentRow=self.ui.listWidget_MainFile.currentRow() # number of clicked Sentence
        #self.source.raportStructure=[{0:2}, {}, {}, {}, {}, {}, {}, {}]
        
        if(len(self.source.raportStructure[currentRow].keys())>0):   # repeat exist
            fileNumber=self.source.raportStructure[currentRow].keys()[0]   # number of file when is repeat
            sentenceNumber=self.source.raportStructure[currentRow].values()[0]   # number of sentence in fileNumber where is repeat
        
            self.ui.listWidget_OutFilesList.setCurrentRow(fileNumber)  #change outFile text to show
            self.UpdateRaport() # update widget
            self.ui.listWidget_ChoosenOutFile.setCurrentRow(sentenceNumber) # make focus on sentence
        
    def listWidget_ChoosenOutFileDClicked(self):
        clickedRow=self.ui.listWidget_ChoosenOutFile.currentRow() # number of clicked sentence
        #self.source.raportStructure=[{0:2}, {}, {}, {}, {}, {}, {}, {}]
        outFileNumber=self.ui.listWidget_OutFilesList.currentRow()  # in what file was that sentence
        #self.source.OutFiles[outFileNumber].repeats=[2,2,2,2,2,2,2]
        mainFileSentenceNumber=self.source.OutFiles[outFileNumber].repeats[clickedRow]  # search for repeat number
        self.ui.listWidget_MainFile.setCurrentRow(mainFileSentenceNumber) #change focus on left widget
    

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