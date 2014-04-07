# -*- coding: utf-8 -*-

import nltk   
import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader
import urllib
import re                       # do wyrażeń regularnych!
from hashlib import sha224      # do tworzenia hashy!
class File():
    def __init__(self,path):
        self.pathToFile=path
        #self.repeats
        #self.hashedText
    
    
        '''Return hashedText'''  
    def GetHashedText(self):
        
        return self.hashedText    
    
    '''Delete colons, space, making the letters small'''
    def PrepareSentenceToHash(self,sentence):
        ''' #Input: string sentence (unprocessed) 
        Output: string sentence (processed)
        Description: Function makes lower cases, deletes all punctuations (all spaces as well), polish joins-word (i, ale, pod) and changes polish letter to english equivalent.
        '''
        
        sentence = "Australijski okręt biorący udział w poszukiwaniach samolotu malezyjskich linii lotniczych wykrył sygnały podobne do tych, jakie emitują czarne skrzynki - poinformowały w poniedziałek władze w Canberze."
         # 0. do małych liter
        sentence = sentence.lower()
        # 1. znaki interpunkcyjne
        interpunkcja = [',', ':', ';', '!', '@', '#', '$', '%', '^', '&', '\*', '\.', '\(', '\)', '-', '_', '\+', '=', '\{', '\}', '\[', '\]', '\|', '<', '>', '\?']
        # polskie łączniki
        laczniki = ['i', 'a', 'w', 'o', 'lub','jednak', 'na', 'u', 'pod', 'powyżej', 'poniżej', 'ponad', ]
        # polskie znaki ę ą 
        polskie_znaki = {'ę': 'e', 'ó': 'o', 'ą': 'a', 'ś': 's', 'ł': 'l', 'ż': 'z', 'ź': 'z', 'ć': 'c', 'ń': 'n', 'Ę': 'e', 'Ó': 'o', 'Ą': 'a', 'Ś': 's', 'Ł': 'l', 'Ż': 'z', 'Ź': 'z', 'Ć': 'c', 'Ń': 'n'}
        
        print polskie_znaki
        
        
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
        Description: Fuction using hashlib library creates hast-tag from proceesed sentence.
        '''
        
        hashedSentence = sha224(sentence).hexdigest()
        return hashedSentence
    
    
    '''Method take HTML code and delete from it tags, operators etc. At end we have clear text'''
    def ParseHTML(self,HTMLtext):
        #TODO:RAFAL
        parsedText = nltk.clean_html(HTMLtext)  
        return parsedText
    
    '''Method get path and return big text from file'''
    def LoadTextFromFile(self,path):
        '''TODO: RAFAL '''
        if(path.find('.pdf')>=0):
            text=self.LoadFromPdf(path)
        if(path.find('.txt')>=0):
            text=self.LoadFromTxt(path)
        if(path.find('.html')>=0):
            text=self.LoadFromHtml(path)      
        return text
    
    '''download file'''
    def Download(self,path):
        #TODO:RAFAL
        usock = urllib.urlopen(path)
        text=usock.read()
        usock.close()
        return text

    ''' Return text from .html'''
    def LoadFromHtml(self,path):
        #TODO:RAFAL
        HTMLtext=self.LoadFromTxt(path)
        text=self.ParseHTML(HTMLtext)
        return text
    
    ''' Return text from .txt'''
    def LoadFromTxt(self,path):
        #TODO:RAFAL
        f = open(path, 'r')
        HTMLtext=f.read()
        f.close()
        return text
    
    ''' Return text from .pdf'''
    def LoadFromPdf(self,path):
        #TODO:RAFAL
        text = ""
        # Load PDF into pyPDF
        pdf = PdfFileReader(open("path", "rb"))
        # Iterate pages
        for i in range(0, pdf.getNumPages()):
            # Extract text from page and add to content
            print i
            text += pdf.getPage(i).extractText() + "\n"
        
        return text

    '''Return true if contain www or http'''
    def IsLink(self,sentence):
        '''
        TODO: RAFAL
        '''
        return True

