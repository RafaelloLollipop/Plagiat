# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class MainFile(File):
    '''Constructor'''
    def __init__(self, path):
        File.__init__(self,path)
        self.repeats=[]  # Nie pamietam po chuj to, w domysle bool to mialo byc?XD bool [nameFile]
        self.hashedText={}  # { sentence : hash }
        self.wwwAdress=[] # Contain a www sites from MainFile
        self.Generate() #AutoGenerateMethod Start
        
    '''Return wwwAdress'''
    def GetwwwAdress(self):
        return self.wwwAdress
    
    ''' Add wwwAdress'''
    def AddwwwAdress(self,adress):
        self.wwwAdress.append(adress)
        return True
    
    '''Method started by constructor
        Making object ready to use
        Order to LoadText from file
        And make hashedText
    '''
    def Generate(self):
        ''' Start all methods
        '''
        text=self.LoadTextFromFile('')
        if (self.DotHTML()):
            text=self.ParseHTML(text)
        text=self.MakeHashedText(text)
        
        return True
    

    
    '''check te path to mainFile, if end with .html or .htm return true'''
    def DotHTML(self):
        return True
    
    '''Method started by Create()
    Method taking address from text or bibliography and collect it in the wwwAdress list
    next fork and hash
    '''
    def MakeHashedText(self,text):
        ''' This functon at end of work guarantees properly make hashedText
        TODO: RAFAL
        '''
        # Loop
        sentence=""
        if (self.IsLink(sentence)):
            #TODO:RAFAL
            # Fork adress
            # Add to wwwAdress
            return False
        else:
            sentenceHash=self.PrepareSectenceToHash(sentence)
            sentenceHash=self.HashSentence(sentence)
            self.hashedText[sentence]=sentenceHash
        # End loop
        
        return True
    
