# -*- coding: utf-8 -*-
import sys
import re
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class OutFile(File):
    '''Constructor'''
    def __init__(self,path):
        
        File.__init__(self)
        self.repeats=[] # list of int,  - no repeat, x - number of senetnce 
        self.raportGenereted=false
        self.GenerateOutFile(path)
    
    ''' Automatic function started in Constructor    
     Taking path (MUST BE IN CONSUTRCTOR) (local or www) & preapre it
     At finish method start MakeHashedText method with clear text
     www, http are REMOVED!! '''
        
    def SetRaportGenereted(self):
        self.raportGenereted=true
        
    def GenerateOutFile(self,path):
        ''' This method end when OutFile is properly created
            TODO: KAMIL
        '''
        if (self.IsLink(path)):  # Contain www or http ? 
            downText=self.DownloadText(path)  
            text=self.ParseHTML(downText)
        else:
            text=text=self.LoadTextFromFile(path)
        
        self.MakeClearAndHashedText(text)

        return True
    
    
    
    '''Take text, fork text to sentence, prepare it and hash
        At end we get hashedText List - List of senetence hash '''
    
    '''Method generate raport and save it'''
    def GenerateRaport(self,path):
        '''
        TODO: KAMIL
        path -> directory where raport should be
        '''
        return True
    