import sys
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class OutFile(File):
    '''Constructor'''
    def __init__(self,path):
        
        File.__init__(self,path)
        self.repeats=[] # list of int,  - no repeat, x - number of senetnce 
        self.hashedText=[] # Text from file transported to List 
        self.raportGenereted=False   # Raport exist checker
        self.Generate(path)
        
    '''Return ->raportGenereted'''
    def GetRaportGenereted(self):
        return self.raportGenereted
     
    
    ''' Automatic function started in Constructor    
     Taking path (MUST BE IN CONSUTRCTOR) (local or www) & preapre it
     At finish method start MakeHashedText method with clear text
     www, http are REMOVED!! '''
    def Generate(self,path):
        ''' This method end when OutFile is properly created
            TODO: KAMIL
        '''
        if (self.IsLink(path)):  # Contain www or http ? 
            pathToDownloadedFile=self.Download(path)  
            text=self.LoadTextFromFile(pathToDownloadedFile)
            text=self.ParseHTML(text)
        else:
            text=text=self.LoadTextFromFile(path)
        
        self.MakeHashedText(text)
            
        
        
        return True
    
    
    '''Take text, fork text to sentence, prepare it and hash
        At end we get hashedText List - List of senetence hash '''
    def MakeHashedText(self,text):
        '''
        text(string) - clear text like " Rafal jest ok. Kamil spoko loko.
        TODO:KAMIL
        '''
        
        # Loop
        sentence=""
        sentencePrepared=self.PrepareSectenceToHash(sentence)
        sentenceHash=self.HashSentence(sentencePrepared)
        self.hashedText.append(sentenceHash)
        # End loop
        
        return True



    '''Method Download file and return path to it'''
    def Download(self,link):
        '''
        TODO: RAFAL
        '''
        pathToFile=''
        return pathToFile
    
    
    '''Method generate raport and save it'''
    def GenerateRaport(self):
        '''
        TODO: KAMIL
        '''
        self.raportGenereted=True
        return True
    