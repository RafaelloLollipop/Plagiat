# -*- coding: utf-8 -*-                                    
#pyuic4 gui.ui > gui.py
#QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
from os import path
from Tkinter import Tk
from tkFileDialog import askopenfilename
import sys
import time                                     
import webbrowser
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
        QtCore.QObject.connect(self.ui.Button_LoadOutFile,QtCore.SIGNAL("clicked()"), self.Button_LoadOutFileCandidate)      
        QtCore.QObject.connect(self.ui.Button_RemoveOutFile,QtCore.SIGNAL("clicked()"), self.Button_RemoveOutFile)
        QtCore.QObject.connect(self.ui.Button_AddWWW,QtCore.SIGNAL("clicked()"), self.Button_AddWWWClicked)
        QtCore.QObject.connect(self.ui.Button_Przelicz,QtCore.SIGNAL("clicked()"), self.Button_Przelicz)
        QtCore.QObject.connect(self.ui.horizontalSlider_Threshold,QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_ThresholdValueChanged)
        QtCore.QObject.connect(self.ui.Button_LoadOutFileCandidateFromWWW,QtCore.SIGNAL("clicked()"), self.Button_LoadOutFileCandidateFromWWW)
        QtCore.QObject.connect(self.ui.listWidget_OutFilesList,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_OutFilesListDClicked)        
        QtCore.QObject.connect(self.ui.listWidget_MainFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_MainFileDClicked)
        QtCore.QObject.connect(self.ui.listWidget_ChoosenOutFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_ChoosenOutFileDClicked)
        QtCore.QObject.connect(self.ui.comboBox_MethodList,QtCore.SIGNAL("currentIndexChanged(int)"), self.comboBox_MethodListClicked)
        QtCore.QObject.connect(self.ui.listWidget_wwwFromMainFile,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.listWidget_wwwFromMainFileDClicked)
        #actions
        QtCore.QObject.connect(self.ui.actionNowy_projekt,QtCore.SIGNAL("triggered()"), self.Button_LoadMainFilePath)
        QtCore.QObject.connect(self.ui.actionOtw_rz_projekt,QtCore.SIGNAL("triggered()"), self.Button_LoadConfigPath)
        QtCore.QObject.connect(self.ui.actionDodaj_plik,QtCore.SIGNAL("triggered()"), self.Button_LoadOutFileCandidate)
        QtCore.QObject.connect(self.ui.actionDodaj_WWW,QtCore.SIGNAL("triggered()"), self.Button_LoadOutFileCandidateFromWWW)
        QtCore.QObject.connect(self.ui.actionUsu_plik,QtCore.SIGNAL("triggered()"), self.Button_RemoveOutFile)
        QtCore.QObject.connect(self.ui.actionDokumentacja,QtCore.SIGNAL("triggered()"), self.Action_Dokumentacja)                




    '''Methods to load propertly 1 site'''

    def Action_Dokumentacja(self):
        webbrowser.open_new_tab("https://github.com/Vallher/Plagiat/wiki")
    
    
    def Button_LoadMainFilePath(self): #
        path=(self.source.SearchFile())[0]
        self.source.SetPath(path)
        
        self.source.PrepareMainFile()
        name="XD" #TODOO
        self.source.SetConfigName(name) 
        self.source.CreateConfig()
        self.RefreshDisplay()
        
    def Button_LoadConfigPath(self):  #
        path=self.source.SearchConfig()
        self.source.SetPath(path)
        self.source.LoadConfig()
        self.RefreshDisplay()
    
    #2
    ''''Methods to load properly 2 site'''    
    def UpdateOutFilesList(self):    
        self.ui.listWidget_OutFilesList.clear()
        for outFile in self.source.OutFiles:
            name=outFile.GetFileName()
            self.ui.listWidget_OutFilesList.addItem(name)
        return True
    
    
    def UpdateWWWlist(self):
        self.ui.listWidget_wwwFromMainFile.clear()
        list= self.source.GetAdressFromMainFile()
        for adress in list:
            self.ui.listWidget_wwwFromMainFile.addItem(adress)    
    
    
    def RefreshDisplay(self):
        self.UpdateMainFileText()
        self.UpdateWWWlist()
        self.UpdateOutFilesList()
        self.UpdateMainFileText()
        self.source.GenerateRaport()
        self.LoadOutFilesListInRaport()
        self.UpdateChoosenOutFileText()    
        self.UpdateRaportStats()
        self.ColorMainFile()
        self.ColorOutFilesList()
        threshold=self.ui.horizontalSlider_Threshold.value()
        self.ui.label_numberOfThreshold.setText(str(threshold))
        return True
    
    
    def listWidget_wwwFromMainFileDClicked(self):
        adressList= self.source.GetAdressFromMainFile()
        clickedRow=self.ui.listWidget_wwwFromMainFile.currentRow()
        path=[adressList[clickedRow]]
        self.source.AddOutFileCandidate(path)
        self.AddOutFiles()

    
    def Button_AddWWWClicked(self):
        path=[str(self.ui.lineEdit_wwwPath.text())]
        self.source.AddOutFileCandidate(path)
        self.AddOutFiles()
    
    #button
    def Button_LoadOutFileCandidateFromWWW(self):
        self.ui.listWidget_wwwFromMainFile.setVisible(not self.ui.listWidget_wwwFromMainFile.isVisible())    
        self.ui.lineEdit_wwwPath.setVisible(not self.ui.lineEdit_wwwPath.isVisible()) 
        self.ui.Button_AddWWW.setVisible(not self.ui.Button_AddWWW.isVisible())  
        return True
    
    def Button_LoadOutFileCandidate(self):
        path=self.source.SearchFile()
        self.source.AddOutFileCandidate(path)
        self.AddOutFiles()
    
    def Button_RemoveOutFile(self):
        clickedRow=self.ui.listWidget_OutFilesList.currentRow()
        self.source.RemoveOutFile(clickedRow)
        self.UpdateOutFilesList()
        self.RefreshDisplay()
    
    def AddOutFiles(self):
        self.ui.progressBar_GenerateOutFile.setValue(0)
        howMuchOut=len(self.source.OutFilesCandidate)
        print howMuchOut
        valueRaise=100.0/howMuchOut
        done=[]
        for outFile in self.source.OutFilesCandidate:
            print "BLAD" + outFile
            self.ui.progressBar_GenerateOutFile.setValue(self.ui.progressBar_GenerateOutFile.value()+valueRaise)
            try:
                self.source.GenerateOutFile([outFile])
            except Exception as ex:
                self.ui.listWidget_errorList.addItem(ex.args[0]+": "+ex.args[1]) 
            done.append(outFile)
            self.UpdateOutFilesList()
        for complete in done:
            self.source.OutFilesCandidate.remove(complete)
        self.UpdateOutFilesList()
        self.RefreshDisplay()
            
    def horizontalSlider_ThresholdValueChanged(self):
        threshold=self.ui.horizontalSlider_Threshold.value()
        self.source.threshold=threshold
        self.RefreshDisplay()

        return True
    def Button_Przelicz(self):
        self.ui.progressBar_GenerateOutFile.setValue(0)
        howMuchOut=len(self.source.OutFiles)+1
        valueRaise=100.0/howMuchOut
        
        
        for OutFile in self.source.OutFiles:
            self.ui.progressBar_GenerateOutFile.setValue(self.ui.progressBar_GenerateOutFile.value()+valueRaise)
            OutFile.repeats.pop()
            self.source.CheckSimilarity(OutFile)
        self.ui.progressBar_GenerateOutFile.setValue(100)
        self.RefreshDisplay()
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
        try:
            for sentence in self.source.OutFiles[currentRow].clearText:
                self.ui.listWidget_ChoosenOutFile.addItem(sentence)
        except:
           print "BRAK OUTFILOW"
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
   #     colors.append(QtGui.QColor(176,23,31))
    #    colors.append(QtGui.QColor(65,105,225))
     #   colors.append(QtGui.QColor(93,71,139))
      #  colors.append(QtGui.QColor(238,162,173))
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


    def listWidget_OutFilesListDClicked(self):
        self.UpdateChoosenOutFileText()
    
    
    def comboBox_MethodListClicked(self):
        self.ColorMainFile()
        currentMethodRow=self.ui.comboBox_MethodList.currentIndex()
        
        if(currentMethodRow == 0):
            self.ui.horizontalSlider_Threshold.setEnabled(False)
        else:
            self.ui.horizontalSlider_Threshold.setEnabled(True)
        
    
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