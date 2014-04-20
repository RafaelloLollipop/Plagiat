# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class MainFile(File):
    '''Constructor'''
    def __init__(self,path):
        File.__init__(self)
        self.wwwAdress=[] # Contain a www sites from MainFile
        self.GenerateMainFile(path) #AutoGenerateMethod Start
        
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
    def GenerateMainFile(self,path):
        ''' Start all methods
        '''
        text=self.LoadTextFromFile('')
        if (self.IsLink(path)):
            text=self.ParseHTML(text)
        self.searchForWWW(text)
        self.MakeClearAndHashedText(text)
        
        return True
    

    '''search for www in text and add it to field wwwAdress'''
    def searchForWWW(self,text):
        
        return True
    

    '''Crate XML config from given name'''
    def CreateXMLConfig(self,configName):
        '''
        TODO:RAFAL
        '''
        text=self.FromListToTxt(self.clearText)
        hashedText=self.FromListToTxt(self.hashedText)
            
        root=ET.Element('Config',{'name':configName})
        tree=ET.ElementTree(root)
        files=ET.SubElement(root, 'MainFile',{'name':self.fileName})
        sentences=ET.SubElement(files, 'Sentences')
        sentences.text=text
    
        hashes=ET.SubElement(files, 'Hashes')
        hashes.text=hashedText
        tree.write(configName+".xml")
        return True
