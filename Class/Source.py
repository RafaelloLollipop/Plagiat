# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append(path.abspath('./Class'))
from MainFile import *
from Tkinter import Tk
from tkFileDialog import askopenfilename,askopenfilenames
import Tkinter,tkFileDialog
from OutFile import OutFile
import json
import ngram

class Source():
    """Config class """
    '''Constructor'''
    def __init__(self):
        self.pathToMainFile="" # .txt,.pdf etc
        self.configName="" # dunno, nic z tym nie robilem bo nie pamietam jak to tam mialo byc xD
        #self.mainFile=MainFile('s')   # mainFile object
        self.Adress=[] # list of adress when we want to search for OutFile, www & local
        self.OutFiles=[] # List of OutFiles, with raports
        self.OutFilesCandidate=[] # List of filles who we want to make OutFile, path list
        self.raportStructure=[] # [{z ktorego outFile:ktore zdanie z outFile},[],[]]   raportStructure[0] jest 1 zdaniem z clearText    
        self.lock=False # Locker to LoadWindow
        self._threshold=0
        # 
    
    
    @property
    def threshold(self):
        return self._threshold
    
    @threshold.setter
    def threshold(self,value):
        self._threshold=value
            
    def SetConfigName(self,name):
        self.configName=name
        return True
    
    def SetPath(self,path):
        self.pathToMainFile=path
        return True
    
    def GetPath(self):
        return self.pathToMainFile
    
    def HowManySentencesRepeats(self):
        ''' Return how many sentences from mainFile was found in outFiles '''
        howMany=0
        for dir in self.raportStructure:
           if(len(dir)): howMany+=1
        return howMany
    
    def HowManySentencesRepeatsInOutFiles(self):
        '''return list of all outfiles repeats number
        for ex. if 3 outfiles in database, it wil return [0,1,20]
        '''
        list=[]
        for outFile in self.OutFiles:
            list.append(outFile.HowManyRepeats())
        return list
    
    def HowManySentencesInMainFile(self):
        return len(self.raportStructure)
    
    def GetOutFiles(self):
        return self.OutFiles
    
    def GetMainFileClearText(self):
        return self.mainFile.GetClearText()
    
    def AddOutFileCandidate(self,outFilePath):
        for path in outFilePath:
            self.OutFilesCandidate.append(path)
        return True
    
    def RemoveOutFileCandidate(self,number):
        self.OutFilesCandidate.pop(number)
        return True
    
    def AddOutFile(self,outFile):
        self.OutFiles.append(outFile)
        return True
    
    def GetAdress(self):
        
        return self.Adress
    
    def GetAdressFromMainFile(self):
        
        return self.mainFile.GetwwwAdress()
    
    def AddAdress(self,adress):
        self.Adress.append(adress)
        return True
 
    def RemoveOutFile(self,outFileNumber):
        #TODOXD
        outFileName=self.OutFiles[outFileNumber].GetFileName()
        self.OutFiles.pop(outFileNumber)
        self.RemoveOutFileFromJSONConfig(outFileName)

        return True 
    
    def RemoveAdress(self,adress):
        self.Adress.remove(adress)
        return True
       
    
    def GenerateRaport(self):
        '''@TODO RAFAL'''
        self.raportStructure=[]
        temp={}

        for i in range(len(self.mainFile.clearText)):
            self.raportStructure.append(temp)
    
        #print raportStructure
        for outFileNumber in range(len(self.OutFiles)):
            for method in self.OutFiles[outFileNumber].repeats:
                
                #repeats=self.OutFiles[outFileNumber].repeats
                repeats=method
                #print self.OutFiles[outFileNumber].repeats
                for repeatNumber in range(len(repeats)):
                    if repeats[repeatNumber]>=0:
                        #print [repeatNumber,repeats[repeatNumber]]  
                        #print "outFile numer "+str(outFileNumber) + ' w ktorym zdanie numer ' + str(repeatNumber) + ' jest zdaniem w main numer: '+str(repeats[repeatNumber])
                        self.raportStructure[repeats[repeatNumber]]={outFileNumber:repeatNumber}
        return True
    
    def ListOfMainFileSentenceToColor(self):
        '''return
        [file1 sentences list],[file2senteneslist]]
        want
        [[file 1 method 1 list,file 1 method 2 list],[file 2 method 1 list,file 2 method 2 list]]
        '''
        list=[]
        for outFileNumber in range(len(self.OutFiles)):
            outList=[]
            fileList=[]
            for method in self.OutFiles[outFileNumber].repeats:
                repeats=method
                for repeatNumber in range(len(repeats)):
                    if repeats[repeatNumber]>=0:
                        #print [repeatNumber,repeats[repeatNumber]]  
                        outList.append(repeats[repeatNumber])
                fileList.append(outList)
                outList=[]
            list.append(fileList)
        return list
    
    def SearchFile(self):
        """ This function return path to File"""
        file_opt = {}
        myFormats = [
            ('Text','*.txt'),
            ('PDF','*.pdf'),
            ('HTML','*.html'),
            ('Microsoft Office .doc','*.doc'),
            ]
    
        path=''
        pathList=[]
        if(not self.lock):
            self.lock=True
            root=Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            path=askopenfilenames(filetypes=myFormats)
            path = path.strip('{}').split('} {')
            self.lock=False

        return path
    
    
    def SearchConfig(self):
        """ This function return path to File"""

        self.file_opt = options = {}
        myFormats = [
            ('JSON','*.json')
            ]
        
        path=''
        if(not self.lock):
            self.lock=True
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            path=askopenfilename(filetypes=myFormats ) 
            self.lock=False
        return path
        
    def PrepareMainFile(self):
        '''Create objectMainFile
        Used after click event
        To add:
        Check pathToMainFile correctness
        TODO:RAFAL
        '''
        self.mainFile=MainFile(self.pathToMainFile)
        return True
    
    
    def LoadConfig(self):
        f = open(self.pathToMainFile, 'r')
        config = f.read()
        f.close()
        config = json.loads(config)  
       
        configName=self.pathToMainFile.split('/')[len(self.pathToMainFile.split('/'))-1][:-5]
        #self.pathToMainFile="" # .txt,.pdf etc
        self.configName=configName 

        mainFileJSON=config['mainFile']
        self.mainFile=MainFile(mainFileJSON,True)
        
        for outName in config['outFiles']:
            self.OutFiles.append(OutFile(config['outFiles'][outName],True,outName))
        return True
    
    def CreateConfig(self):
        self.mainFile.CreateJSONConfig(self.configName)
    
    def GenerateOutFile(self,pathList):
        '''
        After button click
        TODO:KAMIL
        '''
        print pathList
        for path in pathList:  
            print path
            try:
                newOutFile=OutFile(path)
            except:
                raise Exception('OutFileCoddingError',path);
            self.OutFiles.append(newOutFile)
            self.SearchPlagiarsim(newOutFile)
            
        return True
    
    def SearchPlagiarsim(self,OutFile):
        '''Start crazy machine : D
        start by click
        TODO:KAMIL
        '''    
        #Loop
        self.CompareHashMethod(OutFile)
        self.CheckSimilarity(OutFile)     # tutaj jako drugi argument treshold z gui 
        self.AddOutFileToJSONConfig(OutFile)
        #EndOfLoop
        return True

    def CompareHashMethod(self,OutFile):
        ''' 
        TODO:KAMIL
        make repeats list in OutFile complete         '''
        print "Tutaj hashe z Main File";
        outRepeats=[]
        powtorki = []
        for hashOutFile in OutFile.hashedText:
            iteracjaMain = 0;
            dodany = 0;
            for hashMainFile in self.mainFile.hashedText: 
                #print hashOutFile + " " + hashMainFile;
                if (hashOutFile == hashMainFile):
                    #print iteracjaMain;
                    outRepeats.append(iteracjaMain);
                    dodany = 1;
                iteracjaMain +=1;
            if (dodany!=1):
               outRepeats.append(-1);
        
        OutFile.repeats.append(outRepeats)
        #for el in OutFile.repeats:
            #print el;
        return True
    
    def CheckSimilarity(self, OutFile):
        result = []
        for zdanie_ref in OutFile.clearText: 
            i = 0
            best_comparison = 0
            best_iteration = -1
            for zdanie_glo in self.mainFile.clearText: 
                comparison = ngram.NGram.compare(zdanie_ref,zdanie_glo,N=1)
                if (comparison > best_comparison):
                    best_comparison = comparison
                    best_iteration = i
                i+=1
            if (best_comparison > self.threshold/100.0):
                result.append(best_iteration)
            else:
                result.append(-1)
        
        #print result 
        OutFile.repeats.append(result)
        return True       # Tutaj masz wyniki tak na takiej samej zasadzie jak w metodzie CompareHashMethod
    
    def AddOutFileToJSONConfig(self,OutFile):
        ''' End when Raport is sucesfully generated
        '''
        OutFile.AddOutFileToConfigJSON(self.configName)
        return True
    
    def GetOutFileFromJSONConfig(self,outFileName):
        f = open(self.configName+'.json', 'r')
        config=f.read()
        f.close()
        config= json.loads(config)
        
        outFileDict=config['outFiles'][outFileName]
    
        return outFileDict
        
    
    
    def RemoveOutFileFromJSONConfig(self,outFileName):
        f = open(self.configName+'.json', 'r')
        config=f.read()
        f.close()
        
        config= json.loads(config)
        if(config['outFiles'].has_key(outFileName)): config['outFiles'].pop(outFileName)
        f = open(self.configName+'.json', 'w')
        config = json.dumps(config,indent=2)
        f.write(config)
        f.close()
        return True
    