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
    
    
    ''' Add this OutFile to configName.xml'''
    def AddOutFileToConfigXML(self,configName):
    
        text=self.FromListToTxt(self.clearText)
        hashedText=self.FromListToTxt(self.hashedText)
        repeats=self.FromListToTxt(self.repeats)
        
        tree= ET.parse(configName+".xml")
        root=tree.getroot()
    
        files=ET.SubElement(root, 'OutFile',{'name':self.fileName})
    
        sentences=ET.SubElement(files, 'Sentences')
        sentences.text=text
    
        hashes=ET.SubElement(files, 'Hashes')
        hashes.text=hashedText
    
        rep=ET.SubElement(files, 'Repeats')
        rep.text=repeats
    
        tree.write(configName+".xml")
        
        return True
    
