# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append(path.abspath('./Class'))
from MainFile import *
from Tkinter import Tk
from tkFileDialog import askopenfilename


class Source():
    """Main Class of program """
    '''Constructor'''
    def __init__(self):
        self.pathToMainFile="" # .txt,.pdf etc
        self.configPath="" # dunno, nic z tym nie robilem bo nie pamietam jak to tam mialo byc xD
        self.mainFile=MainFile('s')   # mainFile object
        self.Adress=[] # list of adress when we want to search for OutFile, www & local
        self.OutFiles=[] # List of OutFiles, with raports
        self.OutFilesCandidate=[] # List of filles who we want to make OutFile, path list
    
    
    # Tych dwoch metod nie jestem pewien :D
    '''getery i setery jebac to'''
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

        self.pathToMainFile=path
        return path
        
    def PreapreMainFile(self):
        '''Create objectMainFile
        Used after click event
        To add:
        Check pathToMainFile correctness
        TODO:RAFAL
        '''
        self.mainFile=MainFile(self.pathToMainFile)
        return True
    
    def GenerateOutFile(self,pathList):
        '''
        After button click
        TODO:KAMIL
        '''
        pathList = []  # lista adresow
        #Loop
        path=""  
        newOutFile=OutFile(path)
        self.OutFilesCandidate.remove(path)
        self.OutFiles.append(newOutFile)
        self.SearchPlagiarsim(path)
        #EndOfLopp
        return True
    
    def SearchPlagiarsim(self,path):
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
        if (OutFile.GenerateRaport(path)):
            OutFile.SetRaportGenereted()
        
        
        return True
    
    def ShowRaports(self):
        ''' Start by click
        TODO:RAFAL
        '''
        return True 
    
    