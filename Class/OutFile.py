# -*- coding: utf-8 -*-
import sys
import re
import json
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class OutFile(File):
    '''Constructor'''
    def __init__(self,path):
        
        File.__init__(self)
        self.repeats=[] # list of int,  - no repeat, x - number of senetnce 
        self.GenerateOutFile(path)
    
    ''' Automatic function started in Constructor    
     Taking path (MUST BE IN CONSUTRCTOR) (local or www) & preapre it
     At finish method start MakeHashedText method with clear text
     www, http are REMOVED!! '''

    def GenerateOutFile(self,path):
        ''' This method end when OutFile is properly created
            
            TODO: KAMIL, pamietaj zeby bylo filename
        '''
        self.fileName=path.split('/')[len(path.split('/'))-1]
        if (self.IsLink(path)):  # Contain www or http ? 
            downText=self.DownloadText(path)  
            text=self.ParseHTML(downText)
        else:
            text=text=self.LoadTextFromFile(path)
            
        self.MakeClearAndHashedText(text)

        return True
    
    
    def AddOutFileToConfigJSON(self,configName):
        f = open(configName+'.json', 'r')
        config=f.read()
        f.close()
        config= json.loads(config,encoding="ISO-8859-1")
        
        outFile={
        "Sentences": self.clearText,
        "Hashes" : self.hashedText,
        "Repeats": self.repeats
        }
        config['outFiles'][self.fileName]=outFile
        config= json.dumps(config,indent=2)
        f = open(configName+'.json', 'w')
        f.write(config)
        f.close()
        
        return True
    
