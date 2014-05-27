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
        
        QtCore.QObject.connect(self.ui.Button_LoadMainFilePath,QtCore.SIGNAL("clicked()"), self.Button_LoadMainFilePath)
        QtCore.QObject.connect(self.ui.Button_LoadConfigPath,QtCore.SIGNAL("clicked()"), self.Button_LoadConfigPath)
        QtCore.QObject.connect(self.ui.Button_Next1,QtCore.SIGNAL("clicked()"), self.Button_Next1)
        QtCore.QObject.connect(self.ui.Button_Next2,QtCore.SIGNAL("clicked()"), self.Button_Next2)
        QtCore.QObject.connect(self.ui.Button_LoadOutFileCandidate,QtCore.SIGNAL("clicked()"), self.Button_LoadOutFileCandidate)
        QtCore.QObject.connect(self.ui.Button_RemoveOutFileCandidate,QtCore.SIGNAL("clicked()"), self.Button_RemoveOutFileCandidate)
        QtCore.QObject.connect(self.ui.Button_RemoveOutFile,QtCore.SIGNAL("clicked()"), self.Button_RemoveOutFile)
        QtCore.QObject.connect(self.ui.horizontalSlider_Threshold,QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_ThresholdValueChanged)
        QtCore.QObject.connect(self.ui.Button_LoadOutFileCandidateFromWWW,QtCore.SIGNAL("clicked()"), self.Button_LoadOutFileCandidateFromWWW)
        QtCore.QObject.connect(self.ui.testButton,QtCore.SIGNAL("clicked()"), self.RunProgram)
        QtCore.QObject.connect(self.ui.Button_AddOutFromCandidate,QtCore.SIGNAL("clicked()"), self.Button_AddOutFromCandidate)
        QtCore.QObject.connect(self.ui.Button_ShowRaport,QtCore.SIGNAL("clicked()"), self.Button_ShowRaport)
        QtCore.QObject.connect(self.ui.listWidget_OutFilesList,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_OutFilesListDClicked)        
        QtCore.QObject.connect(self.ui.listWidget_MainFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_MainFileDClicked)
        QtCore.QObject.connect(self.ui.listWidget_ChoosenOutFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_ChoosenOutFileDClicked)
        QtCore.QObject.connect(self.ui.Button_BackToPage_2,QtCore.SIGNAL("clicked()"), self.Button_BackToPage_2)
        QtCore.QObject.connect(self.ui.Button_BackToPage_1,QtCore.SIGNAL("clicked()"), self.Button_BackToPage_1)
        QtCore.QObject.connect(self.ui.comboBox_MethodList,QtCore.SIGNAL("currentIndexChanged(int)"), self.comboBox_MethodListClicked)
        
#0      
    '''Methods to load propertly 0 site'''
        
    '''Buttons'''
    
    '''Others'''  
    def RunProgram(self):
        value=self.ui.progressBar_StartProgram.value()+23
        self.ui.progressBar_StartProgram.setValue(value)
        value= 100
        if(value>99):
            self.Load1PageDisplay()

#1  
    '''Methods to load propertly 1 site'''

    def Load1PageDisplay(self):
        self.ui.lineEdit_LoadMainFile_Name.clear()
        self.ui.Line_LoadConfig_Path.clear()
        self.ui.Line_LoadMainFile_Path.clear()
        self.ui.stackedWidget.setCurrentIndex(1)

        
    '''Buttons'''
    def Button_Next1(self):
        '''Load from file button'''
        
        self.source.PrepareMainFile()
        name=self.ui.lineEdit_LoadMainFile_Name.displayText() 
        self.source.SetConfigName(name) 
        self.source.CreateConfig()
        self.Load2PageDisplay()
        self.ui.Line_LoadConfig_Path.clear()

    def Button_Next2(self):
        '''Load from config button'''
        self.source.LoadConfig()
        self.Load2PageDisplay()
        self.ui.lineEdit_LoadMainFile_Name.clear()
        self.ui.Line_LoadMainFile_Path.clear()
    
    def Button_LoadMainFilePath(self):
        self.ui.lineEdit_LoadMainFile_Name.setText("XD") #TODELETE
        path=self.source.SearchFile()
        self.ui.Line_LoadMainFile_Path.setText(path)
        self.source.SetPath(path)
        
    def Button_LoadConfigPath(self):
        path=self.source.SearchConfig()
        self.ui.Line_LoadConfig_Path.setText(path)
        self.source.SetPath(path)
    
    #2
    ''''Methods to load properly 2 site'''    
    def UpdateOutFilesList(self):    
        self.ui.listWidget_OutFiles.clear()
        for outFile in self.source.OutFiles:
            name=outFile.GetFileName()
            print name
            self.ui.listWidget_OutFiles.addItem(name)
        return True
    
    def UpdateOutFilesCandidateList(self):    
        self.ui.listWidget_CandidateOutFiles.clear()
        for outFileName in self.source.OutFilesCandidate:
            self.ui.listWidget_CandidateOutFiles.addItem(outFileName)
        return True
    
    
    def UpdateWWWlist(self):
        self.ui.listWidget_wwwFromMainFile.clear()
        list= self.source.GetAdressFromMainFile()
        for adress in list:
            self.ui.listWidget_wwwFromMainFile.addItem(adress)    
    
    def UpdatePathToFile(self):
        path=self.source.GetPath()
        self.ui.Line_LoadMainFile_Path.setText(path)
        return True
    
    
    def Load2PageDisplay(self):
        self.UpdateWWWlist()
        self.UpdateOutFilesList()
        self.UpdatePathToFile()
        self.UpdateOutFilesCandidateList()
        self.ui.stackedWidget.setCurrentIndex(2)
        return True
    
    #button
    def Button_LoadOutFileCandidateFromWWW(self):
        adressList= self.source.GetAdressFromMainFile()
        clickedRow=self.ui.listWidget_wwwFromMainFile.currentRow()
        path=adressList[clickedRow]
        self.source.AddOutFileCandidate(path)
        self.UpdateOutFilesCandidateList()     
        return True
        
    def Button_RemoveOutFileCandidate(self):
        clickedRow=self.ui.listWidget_CandidateOutFiles.currentRow()
        self.source.RemoveOutFileCandidate(clicked)
        self.UpdateOutFilesCandidateList() 
        
        return True
    
    def Button_LoadOutFileCandidate(self):
        path=self.source.SearchFile()
        self.ui.Line_LoadOutFile_Path.setText(path)
        self.source.AddOutFileCandidate(path)
        self.UpdateOutFilesCandidateList()
    
    def Button_RemoveOutFile(self):
        clickedRow=self.ui.listWidget_OutFiles.currentRow()
        self.source.RemoveOutFile(clickedRow)
        self.UpdateOutFilesList()

    def Button_AddOutFromCandidate(self):
        self.source.GenerateOutFile(self.source.OutFilesCandidate)
        self.UpdateOutFilesCandidateList()
        self.UpdateOutFilesList()

    def Button_BackToPage_1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def Button_ShowRaport(self):
        self.source.GenerateRaport() # Create raport
        self.Load3PageDisplay()
        return True
            
    def horizontalSlider_ThresholdValueChanged(self):
        self.source.threshold=self.ui.horizontalSlider_Threshold.value()
        return True

        '''Method to properly load 3 site'''
    
    def UpdateRaportStats(self):
        mainFileSentencesNumber=self.source.HowManySentencesInMainFile()
        numberOfRepeatSentences=self.source.HowManySentencesRepeats()
        self.ui.label_numberOfSentences.setText(str(mainFileSentencesNumber))
        self.ui.label_numberOfRepeatSentences.setText(str(numberOfRepeatSentences))
        percentValue=numberOfRepeatSentences*100/mainFileSentencesNumber
        self.ui.label_repeatSentencesProcent.setText(str(percentValue)+' %')
        pass

    def UpdateMainFileText(self):
        self.ui.listWidget_MainFile.clear()
        for sentence in self.source.GetMainFileClearText():  # show MainFile text to left widget 
            self.ui.listWidget_MainFile.addItem(sentence) 

    def UpdateChoosenOutFileText(self):
        currentRow=self.ui.listWidget_OutFilesList.currentRow()
        self.ui.listWidget_ChoosenOutFile.clear()
        currentMethodRow=self.ui.comboBox_MethodList.currentIndex()
        for sentence in self.source.OutFiles[currentRow].clearText:
            self.ui.listWidget_ChoosenOutFile.addItem(sentence)
       
    def ColorMainFile(self):    
        self.ClearColorOnMainFile()
        currentMethodRow=self.ui.comboBox_MethodList.currentIndex()
        ListOfSentencesToColor=self.source.ListOfMainFileSentenceToColor()
        print ListOfSentencesToColor
        colors=self.GetColors()
        colorIt=-1
        for outFile in ListOfSentencesToColor:
            outFileCurrentMethod=outFile[currentMethodRow]
            colorIt+=1
            color=colors[colorIt]
            for number in outFileCurrentMethod:
                print "KOLORUJE"
                print number
                item=self.ui.listWidget_MainFile.item(number)
                item.setBackgroundColor(color)
    
    def ClearColorOnMainFile(self):
        for number in range(self.source.HowManySentencesInMainFile()):
            item=self.ui.listWidget_MainFile.item(number)
            item.setBackgroundColor(QtGui.QColor(255,255,255))
    
    def ColorOutFilesList(self):    
        numberOfOutFiles=len(self.source.GetOutFiles())
        colors=self.GetColors()
        colorIt=-1
        for outFileNumber in range(numberOfOutFiles):
            colorIt+=1
            color=colors[colorIt]
            item=self.ui.listWidget_OutFilesList.item(outFileNumber)
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

    def LoadOutFilesListInRaport(self):
        self.ui.listWidget_OutFilesList.clear()
        for outFile in self.source.GetOutFiles():  # make list of outfiles in top widget
            outFileName=outFile.GetFileName()
            self.ui.listWidget_OutFilesList.addItem(outFileName)  
        self.ui.listWidget_OutFilesList.setCurrentRow(0)

        

    def Load3PageDisplay(self):
        self.UpdateRaportStats()
        self.UpdateMainFileText()
        self.LoadOutFilesListInRaport()
        self.UpdateChoosenOutFileText()    
        self.ColorMainFile()
        self.ColorOutFilesList()

        self.ui.stackedWidget.setCurrentIndex(3) 
        return True
            
    def Button_BackToPage_2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def listWidget_OutFilesListDClicked(self):
        self.UpdateChoosenOutFileText()
    
    
    def comboBox_MethodListClicked(self):
        self.ColorMainFile()
        
    
    def listWidget_MainFileDClicked(self):
        currentRow=self.ui.listWidget_MainFile.currentRow() # number of clicked Sentence
        
        if(len(self.source.raportStructure[currentRow].keys())>0):   # repeat exist
            fileNumber=self.source.raportStructure[currentRow].keys()[0]   # number of file when is repeat
            sentenceNumber=self.source.raportStructure[currentRow].values()[0]   # number of sentence in fileNumber where is repeat
        
            self.ui.listWidget_OutFilesList.setCurrentRow(fileNumber)  #change outFile text to show
            self.UpdateChoosenOutFileText() # update widget
            self.ui.listWidget_ChoosenOutFile.setCurrentRow(sentenceNumber) # make focus on sentence
        
    def listWidget_ChoosenOutFileDClicked(self):
        currentMethodRow=self.ui.comboBox_MethodList.currentIndex()
        #self.Change_listWidget_ChoosenOutFileFoucs()
        clickedRow=self.ui.listWidget_ChoosenOutFile.currentRow() # number of clicked sentence
        #self.source.raportStructure=[{0:2}, {}, {}, {}, {}, {}, {}, {}]
        outFileNumber=self.ui.listWidget_OutFilesList.currentRow()  # in what file was that sentence
        #self.source.OutFiles[outFileNumber].repeats=[2,2,2,2,2,2,2]
        mainFileSentenceNumber=self.source.OutFiles[outFileNumber].repeats[currentMethodRow][clickedRow]  # search for repeat number
        self.ui.listWidget_MainFile.setCurrentRow(mainFileSentenceNumber) #change focus on left widget
        return True
        
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