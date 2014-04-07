# -*- coding: utf-8 -*-
import re                       # do wyrażeń regularnych
from hashlib import sha224      # do tworzenia hashy

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
        Description: Fuction makes lower cases, deletes all punctuations (all spaces as well), polish joins-word (i, ale, pod) and changes polish letter to english equivalent.
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
        '''TODO:RAFAL'''
        parsedText=""
        return parsedText
    
    '''Method get path and return big text from file'''
    def LoadTextFromFile(self,path):
        '''TODO: RAFAL '''
        text=''
        return text
    
    '''Return true if contain www or http'''
    def IsLink(self,sentence):
        '''
        TODO: RAFAL
        '''
        return True

