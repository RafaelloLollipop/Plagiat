# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append(path.abspath('./Class'))
from MainFile import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
from OutFile import OutFile
import json

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
    
    
    # Tych dwoch metod nie jestem pewien :D
    '''getery i setery jebac to'''
    def AddOutFileCandidate(self,outFilePath):
        self.OutFilesCandidate.append(outFilePath)
        return True
    
    def AddOutFile(self,outFile):
        self.OutFiles.append(outFile)
        return True
    
    def GetAdress(self):
        return self.Adress
    
    def AddAdress(self,adress):
        self.Adress.append(adress)
        return True
 
    def RemoveOutFile(self,outFile):
        self.OutFiles.remove(outFile)
        return True 
    
    def RemoveAdress(self,adress):
        self.Adress.remove(adress)
        return True
       
    def LoadChoosedLinks(self):
        ''' this method load all adress choosen from BiographyLinks 
        and show it in the table
        '''
        self.GetAdress()
        return True
    
    def LoadBiographyLink(self):
        ''' this method load all unused adress from wwwAdress list in mainFile object
        and show it in the table
        '''
        self.mainFile.GetwwwAdress()
        return True
    
    def SearchFile(self):
        """ This function return path to File"""
        #TODO:RAFAL

        self.file_opt = options = {}
        myFormats = [
            ('Text','*.txt'),
            ('PDF','*.pdf'),
            ('HTML','*.html'),
            ('Microsoft Office .doc','*.doc'),
            ]
        
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        path=askopenfilename(filetypes=myFormats ) 

        
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
    
    def CreateConfig(self):
        self.mainFile.CreateJSONConfig(self.configName)

    
    
    def GenerateOutFile(self,pathList):
        '''
        After button click
        TODO:KAMIL
        '''
        print pathList
        #pathList = []  # lista adresow
        for path in pathList:  
            newOutFile=OutFile(path)
            self.OutFilesCandidate.remove(path)
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
        self.GenerateRaport(OutFile)
        #EndOfLoop
        return True

    def CompareHashMethod(self,OutFile):
        ''' 
        TODO:KAMIL
        make repeats list in OutFile complete         '''

        
        return True
    
    def GenerateRaport(self,OutFile):
        ''' End when Raport is sucesfully generated
        TODO:KAMIL
        '''
        OutFile.AddOutFileToConfigJSON(self.configName)
        return True
    
    def ShowRaports(self):
        ''' Start by click
        TODO:RAFAL
        '''
        return True 
    
    def GetOutFileFromJSONConfig(self,outFileName):
        f = open(self.configName+'.json', 'r')
        config=f.read()
        f.close()
        config= json.loads(config,encoding="ISO-8859-1")
        
        outFileDict=config['outFiles'][outFileName]
    
        return outFileDict
    
    def GetMainFileFromJSONConfig(self):
        '''return dictionary
          "mainFile": {
            "Hashes": [
              "cc0020a591a12020164ff4ac6012ce965ea4c60b83b8f97137fc336a"
            ], 
            "name": "test.txt", 
            "wwwAdress": [], 
            "Sentences": [
              "zcxczczxcx\u00b3"
            ]
          },  '''
        f = open(self.configName+'.json', 'r')
        config=f.read()
        f.close()
        config= json.loads(config,encoding="ISO-8859-1")
        
        mainFileDict=config['mainFile']
    
        return mainFileDict
    
    
    def RemoveOutFileFromJSONConfig(self,outFileName):
        f = open(self.configName+'.json', 'r')
        config=f.read()
        f.close()
        
        config= json.loads(config,encoding="ISO-8859-1")
        config['outFiles'].pop(outFileName)
                
        f = open(self.configName+'.json', 'w')
        f.write(config)
        f.close()
        return True
    