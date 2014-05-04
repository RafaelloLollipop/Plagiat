# -*- coding: utf-8 -*-
import nltk   
import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader
import urllib
import re                       # do wyrażeń regularnych!
from hashlib import sha224      # do tworzenia hashy!
import json

class File():
    def __init__(self):
        self.fileName=''
        self.pathToFile=''
        self.clearText=[]
        self.hashedText=[]  
    
        '''Return hashedText'''  
    
    def GetFileName(self):
        return self.fileName
    
    def GetHashedText(self):
        
        return self.hashedText    
    
        '''Return clearText'''  
    def GetClearText(self):
        
        return self.clearText
    
    def FromListToTxt(self,list):
        text=""
        for sentence in list:
            text+=sentence+'. '
        return text
    
    '''Delete colons, space, making the letters small'''
    def PrepareSentenceToHash(self,sentence):
        ''' #Input: string sentence (unprocessed) 
        Output: string sentence (processed)
        Description: Function makes lower cases, deletes all punctuations (all spaces as well), polish joins-word (i, ale, pod) and changes polish letter to english equivalent.
        '''
        
         # 0. do małych liter
        sentence = sentence.lower()
        # 1. znaki interpunkcyjne
        interpunkcja = [',', ':', ';', '!', '@', '#', '$', '%', '^', '&', '\*', '\.', '\(', '\)', '-', '_', '\+', '=', '\{', '\}', '\[', '\]', '\|', '<', '>', '\?', '\n', '\t']
        # polskie łączniki
        laczniki = ['i', 'a', 'w', 'o', 'lub','jednak', 'na', 'u', 'pod', 'powyżej', 'poniżej', 'ponad', 'ale',]
        # polskie znaki ę ą 
        polskie_znaki = {'ę': 'e', 'ó': 'o', 'ą': 'a', 'ś': 's', 'ł': 'l', 'ż': 'z', 'ź': 'z', 'ć': 'c', 'ń': 'n', 'Ę': 'e', 'Ó': 'o', 'Ą': 'a', 'Ś': 's', 'Ł': 'l', 'Ż': 'z', 'Ź': 'z', 'Ć': 'c', 'Ń': 'n'}
        
        
        
        for char in interpunkcja:
            sentence = re.sub(char, '', sentence)
        for char in laczniki:
            sentence = re.sub('\W'+char+'\W', '', sentence)  # znak w środku
            sentence = re.sub('^'+char+'\W', '', sentence) # znak na początku tekstu
            sentence = re.sub('\W'+char+'$', '', sentence) # znak na końcu tekstu
        for pol, ang in polskie_znaki.items():
            sentence = sentence.replace(pol, ang)
        sentence = re.sub(' ', '', sentence) # usuwanie spacji
        
        
        clearedSentence = sentence
        return clearedSentence
    
        '''Hashing sentence Method'''
    
    def HashSentence(self,sentence):
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
    
  
    
    
    def MakeClearAndHashedText(self,text):
        '''
        Input: tekst ze źródła, który ma zostać podzielony
        Output: True, jeżeli proces poszedł dobrze (czyli aktualnie zawsze:P)
        Description: użyłem następujących założeń: 1) Szukam substringa zaczynącego się od małej litery i zakończonego .!? Następnie sprawdzam czy ostatnie słowo nie jest skrótem np. mgr. prof. km. Jeżeli tak to to zdanie i następne należy połączyć. Jeżeli ostatnie słowo nie jest skrótem to to zdanie i następne należy rodzielić.
        Nie ma problemu ze wielokrotnymi kropkami itp. ponieważ zostaną usuniętę w metodzie PrepareSectenceToHash
        
        @TODO KAMIL
        
        '''
        
        query = "[A-Z]*[.?!][ \\n\\t]+" # Zapytanie regex. Wzór: duża litera + coś + kropka, pytajnik, wykrzyknić + spacja enter lub tab
        lista_temp=re.split(query ,text) # Wstępny podział tekstu
        
        print "text: " + text;
        lista = [];
        print "000000";
        for el in lista_temp:
            lista.append(el);
#             if ((el[1]=="\n") or (el[1]==" ") or (el[1]=="\t")):
#                 print el;
#                 print "TU";
#                 print el[2:];
#                 lista.append(el[2:]);
#             else:
#                 print el;
#                 lista.append(el);
        for sentence in lista:
            # metody jeszcze nie napisane, więc jeszcze komment
            self.clearText.append(sentence)
            sentencePrepared = self.PrepareSentenceToHash(sentence)
            sentenceHash=self.HashSentence(sentencePrepared)
            self.hashedText.append(sentenceHash)
        return True
        
    
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
        if (path.startswith('www')): path='http://'+path
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
        pdf = PdfFileReader(open(path, "rb"))
        # Iterate pages
        for i in range(0, pdf.getNumPages()):
            # Extract text from page and add to content
            
            text += pdf.getPage(i).extractText() + "\n"
        
        return text

    '''Return true if contain www or http
    '''
    def IsLink(self,path):
        '''
        '''
        path=path.lower()
        if (path.startswith('www') or path.startswith('http')): return True
        
        return False
    
 
