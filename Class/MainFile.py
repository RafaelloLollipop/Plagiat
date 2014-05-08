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

        self.fileName=path.split('/')[len(path.split('/'))-1]

        text=self.LoadTextFromFile(path)
        if (self.IsLink(path)):
            text=self.ParseHTML(text)
        self.searchForWWW(text)#not work
        self.MakeClearAndHashedText(text)
        
        return True
    

    '''search for www in text and add it to field wwwAdress
        Pretty good working, wrong recognision: sthwww.page.com
    '''
    def searchForWWW(self,text):
        exp = '(https?:\/\/|www)?([\da-zA-z]+)([\da-zA-Z\.-]+)\.([a-zA-Z]{2,6})([\/\.-][\S]+)?'; # http:// lub https:// adres.rozszerzenie/cos-z-myslnikami
        www_temp = re.findall(exp, text);
        www = [];
#         print "--------";
#         www = [];
#         for el in www_temp:
#             print el;
        for el in www_temp:
            adres = el[0]+el[1]+el[2]+"."+el[3]+el[4]   # dodaj wszystko do siebie
            if ((adres[-1]==".") or (adres[-1]=="!") or (adres[-1]=="?")): # jeżeli na końcu www jest .!? to usuń ją
                adres = adres[:-1];
            self.wwwAdress.append(adres); # dodawanie do listy self.wwwAdress
        print "-------------";
        for el in self.wwwAdress:
            print el;
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
