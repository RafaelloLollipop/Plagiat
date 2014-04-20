# -*- coding: utf-8 -*-
import nltk   
import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader
import urllib
import re                       # do wyrażeń regularnych!
from hashlib import sha224      # do tworzenia hashy!
import xml.etree.ElementTree as ET


class File():
    def __init__(self):
        self.fileName=''
        self.pathToFile=''
        self.clearText=[]
        self.hashedText=[]  
    
        '''Return hashedText'''  
    def GetHashedText(self):
        
        return self.hashedText    
    
        '''Return clearText'''  
    def GetClearText(self):
        
        return self.clearText
    
    def FromListToTxt(self,list):
        text=""
        for sentence in list:
            text+=sentence
        return text
    
    def MakeClearAndHashedText(self,text):
        '''
        Input: tekst ze źródła, który ma zostać podzielony
        Output: True, jeżeli proces poszedł dobrze (czyli aktualnie zawsze:P)
        Description: użyłem następujących założeń: 1) Szukam substringa zaczynącego się od małej litery i zakończonego .!? Następnie sprawdzam czy ostatnie słowo nie jest skrótem np. mgr. prof. km. Jeżeli tak to to zdanie i następne należy połączyć. Jeżeli ostatnie słowo nie jest skrótem to to zdanie i następne należy rodzielić.
        Nie ma problemu ze wielokrotnymi kropkami itp. ponieważ zostaną usuniętę w metodzie PrepareSectenceToHash
        
        @TODO KAMIL
        RAFAL: Pamiętaj, że będą tutaj też linki, chyba trzeba je też filtrować, żeby nie wyglądało głupio:) Pozdrawiam
        '''
        

        text="Można się w nim dopatrzyć nawet odpowiednika owłosienia łonowego. Ale to nasz mózg dokłada wszelkich starań, by odnaleźć podobieństwa, zwłaszcza do tych części ciała, które uważamy za szczególnie interesujące. Podejrzewam, że tak właśnie ich szuka w wyglądzie orzechów kokosowych i profilu Kennedy’ego na zboczu wzgórza."
            
        print text
        query = "[A-Z]*[.?!] " # Zapytanie regex
        temp=re.split(query ,text) # Wstępny podział tekstu
    
        lista = []
        skrot = 0;
        #@TODO: KAMIL Jak już to naprawisz zrób z tego dodatkową metodę, najlepiej w file, ponieważ w MainFile też jej bęzdie trzeba użyć
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
            #self.clearText.append(sentence)
            #sentencePrepared = self.PrepareSectenceToHash(sentence)
            #sentenceHash=self.HashSentence(sentencePrepared)
            #self.hashedText.append(sentenceHash)
        
        return True
        
    
    '''Delete colons, space, making the letters small'''
    def PrepareSentenceToHash(self,sentence):
        ''' #Input: string sentence (unprocessed) 
        Output: string sentence (processed)
        Description: Function makes lower cases, deletes all punctuations (all spaces as well), polish joins-word (i, ale, pod) and changes polish letter to english equivalent.
        '''
        
         # 0. do małych liter
        sentence = sentence.lower()
        # 1. znaki interpunkcyjne
        interpunkcja = [',', ':', ';', '!', '@', '#', '$', '%', '^', '&', '\*', '\.', '\(', '\)', '-', '_', '\+', '=', '\{', '\}', '\[', '\]', '\|', '<', '>', '\?']
        # polskie łączniki
        laczniki = ['i', 'a', 'w', 'o', 'lub','jednak', 'na', 'u', 'pod', 'powyżej', 'poniżej', 'ponad', ]
        # polskie znaki ę ą 
        polskie_znaki = {'ę': 'e', 'ó': 'o', 'ą': 'a', 'ś': 's', 'ł': 'l', 'ż': 'z', 'ź': 'z', 'ć': 'c', 'ń': 'n', 'Ę': 'e', 'Ó': 'o', 'Ą': 'a', 'Ś': 's', 'Ł': 'l', 'Ż': 'z', 'Ź': 'z', 'Ć': 'c', 'Ń': 'n'}
        
        
        for pol, ang in polskie_znaki.items():
            sentence = sentence.replace(pol, ang)
        for char in interpunkcja:
            sentence = re.sub(char, '', sentence)
        for char in laczniki:
            sentence = re.sub('\W'+char+'\W', '', sentence)  # znak w środku
            sentence = re.sub('^'+char+'\W', '', sentence) # znak na początku tekstu
            sentence = re.sub('\W'+char+'$', '', sentence) # znak na końcu tekstu
        sentence = re.sub(' ', '', sentence) # usuwanie spacji
        
        clearedSentence = sentence
        return clearedSentence
    
        '''Hashing sentence Method'''
    
    def HashSentence(self,sentece):
        ''' #Input: string sentence (processed) 
        Output: hash-tag (52 bites)
        Description: Function using hashlib library creates hast-tag from proceesed sentence.
        '''
        
        hashedSentence = sha224(sentence).hexdigest()
        return hashedSentence
    
    '''Method take HTML code and delete from it tags, operators etc. At end we have clear text'''
    def ParseHTML(self,HTMLtext):
        parsedText = nltk.clean_html(HTMLtext)  
        return parsedText
    
    '''Method get path and return big text from file'''
    def LoadTextFromFile(self,path):
        '''TODO: RAFAL '''
        text=''
        if(path.find('.pdf')>=0):
            text=self.LoadFromPdf(path)
        if(path.find('.txt')>=0):
            text=self.LoadFromTxt(path)
        if(path.find('.html')>=0):
            text=self.LoadFromHtml(path)      
        return text
    
    '''download text from www'''
    def DownloadText(self,path):
        usock = urllib.urlopen(path)
        text=usock.read()
        usock.close()
        return text

    ''' Return parsed text from .html'''
    def LoadFromHtml(self,path):
        HTMLtext=self.LoadFromTxt(path)
        text=self.ParseHTML(HTMLtext)
        return text
    
    ''' Return text from .txt'''
    def LoadFromTxt(self,path):
        f = open(path, 'r')
        text=f.read()
        f.close()
        return text
    
    ''' Return text from .pdf'''
    def LoadFromPdf(self,path):
        text = ""
        # Load PDF into pyPDF
        pdf = PdfFileReader(open("path", "rb"))
        # Iterate pages
        for i in range(0, pdf.getNumPages()):
            # Extract text from page and add to content
            print i
            text += pdf.getPage(i).extractText() + "\n"
        
        return text

    '''Return true if contain www or http
    '''
    def IsLink(self,path):
        '''
        TODO: RAFAL
        '''
        return True
    
 
