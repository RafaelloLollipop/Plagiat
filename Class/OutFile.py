# -*- coding: utf-8 -*-
import sys
import re
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
        Input: tekst ze źródła, który ma zostać podzielony
        Output: True, jeżeli proces poszedł dobrze (czyli aktualnie zawsze:P)
        Description: użyłem następujących założeń: 1) Szukam substringa zaczynącego się od małej litery i zakończonego .!? Następnie sprawdzam czy ostatnie słowo nie jest skrótem np. mgr. prof. km. Jeżeli tak to to zdanie i następne należy połączyć. Jeżeli ostatnie słowo nie jest skrótem to to zdanie i następne należy rodzielić.
        Nie ma problemu ze wielokrotnymi kropkami itp. ponieważ zostaną usuniętę w metodzie PrepareSectenceToHash
        '''
        
        print text
        query = "[A-Z]*[.?!] " # Zapytanie regex
        temp=re.split(query ,text) # Wstępny podział tekstu
    
        lista = []
        skrot = 0;
        
        for el in temp:
            if (skrot==0): # sprawdzam czy to zdanie jest po skrócie
                # zdanie nie jest po skrócie
                if ((el[-2]==' ') or (el[-3]==' ') or (el[-4]==' ') or (el[-5]==' ')): # szukam skrótu
                    lista.append(el)
                    skrot = 1;
                else:
                    lista.append(el)
            else:   # zdanie jest po skrócie
                lista[-1] = lista[-1] + ". " + el # zatem dopisuję do ostatniego wpisu
                if ((el[-2]==' ') or (el[-3]==' ') or (el[-4]==' ') or (el[-5]==' ')): # czy teraz na końcu znów nie ma skrótu?
                    skrot = 1;
                else:
                    skrot = 0
        
        for sentence in lista:
            print sentence
            # metody jeszcze nie napisane, więc jeszcze komment
            #sentencePrepared = self.PrepareSectenceToHash(sentence)
            #sentenceHash=self.HashSentence(sentencePrepared)
            #self.hashedText.append(sentenceHash)
        
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
    