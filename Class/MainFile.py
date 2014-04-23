# -*- coding: utf-8 -*-
import sys
import json
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class MainFile(File):
    '''Constructor'''
    def __init__(self,path,isConfig=False):
        File.__init__(self)
        self.wwwAdress=[] # Contain a www sites from MainFile
        if(isConfig):
            self.GenerateMainFileFromJSONConfig(path)
        else:
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
        if(path.find('.json')):
            self.GetMainFileFromJSONConfig(path)
        else:
            self.fileName=path.split('/')[len(path.split('/'))-1]

            text=self.LoadTextFromFile(path)
            if (self.IsLink(path)):  #notwork
                text=self.ParseHTML(text)
                self.searchForWWW(text)#not work
                self.MakeClearAndHashedText(text)
        
        return True
    

    '''search for www in text and add it to field wwwAdress'''
    def searchForWWW(self,text):
        #TODOKAMIL
        return True
    
    def GenerateMainFileFromJSONConfig(self,config):    
        self.hashedText=config['Hashes']
        self.fileName=config['name']
        self.wwwAdress=config['wwwAdress']
        self.clearText=config['Sentences']
        return True
    
    
    def CreateJSONConfig(self,configName):

        mainFile={ "name":self.fileName,
        "Sentences": self.clearText,
        "Hashes": self.hashedText,
        "wwwAdress" : self.wwwAdress}

        config = { 'mainFile': mainFile}
        config['outFiles']={}

        configToSave=json.dumps(config, indent=2)

        f = open(configName+".json", 'w')
        f.write(configToSave)
        f.close()
                
        return True
