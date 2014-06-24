# -*- coding: utf-8 -*-
import nltk   
import sys
import StringIO
import codecs
from PyPDF2 import PdfFileWriter, PdfFileReader
import urllib
try:
    import re                       # do wyrażeń regularnych!
except ImportError:
    print "Nie udało się załadować biblioteki re"
try:
    from hashlib import sha224      # do tworzenia hashy!
except ImportError:
    print "Nie udało się załadować biblioteki hashlib"
import json
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
 

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
    
    
    def SaveChars(self):
        inter = [',', ':', ';', '!', '@', '#', '$', '%', '^', '&', '\*', '\.', '\(', '\)', '-', '_', '\+', '=', '\{', '\}', '\[', '\]', '\|', '<', '>', '\n', '\t']
        abbList = ["mgr", "prof", "hab"]
        lacz = ['i', 'a', 'w', 'o', 'lub','jednak', 'na', 'u', 'pod', 'ponad', 'ale',]
        struct=[]
        struct.append(inter)
        struct.append(lacz)
        struct.append(abbList)
        #configToSave=json.dumps(struct, indent=2,ensure_ascii=False,encoding='utf8')
        
        #f = open('Database'+".json", 'w')
        f = codecs.open('Database'+'.json', "w")
        json.dump(struct, f, indent=2)
        #f.write(configToSave)
        f.close()
        return True
    
    def LoadCharsDatabase(self):
        data=[]
        #f = open('Database'+'.json', 'r')
        f  = file('Database'+'.json', "r")
        #data=f.read()
        data = json.loads(f.read().decode('utf-8'))
        f.close()
        
        #data= json.loads(data,encoding='unicode')
        return data
    
    '''Delete colons, space, making the letters small'''
    def PrepareSentenceToHash(self,sentence):
        ''' #Input: string sentence (unprocessed) 
        Output: string sentence (processed)
        Description: Function makes lower cases, deletes all punctuations (all spaces as well), polish joins-word (i, ale, pod) and changes polish letter to english equivalent.
        '''
         # 0. do małych liter
        sentence = sentence.lower()
        [interpunkcja,laczniki,abbList]=self.LoadCharsDatabase()
        #print polskie_znaki

        # polskie łączniki

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
        # usuwanie znaków, które nie są literami lub cyframi
        re.sub(r'\W+', '', sentence)
        sentence =  ''.join(ch for ch in sentence if ch.isalnum())
        
        
        clearedSentence = sentence
        
        return clearedSentence
    
        '''Hashing sentence Method'''
    
    def HashSentence(self,sentence):
        ''' #Input: string sentence (processed) 
        Output: hash-tag (52 bites)
        Description: Function using hashlib library creates hast-tag from proceesed sentence.
        '''
        try:
            hashedSentence = sha224(sentence).hexdigest()
        except:
            print "Nie udało się zahashować zdania"
        return hashedSentence
    
    '''Method take HTML code and delete from it tags, operators etc. At end we have clear text'''
    def ParseHTML(self,HTMLtext):
        parsedText = nltk.clean_html(HTMLtext)  
        return parsedText
    
  
    def HasAbb(self, sentence):
        '''
        This method checks if the sentence ends with abbreviation (for instance: prof., mgr.). Return true if exists or false if not.
        '''
        result = False
        [interpunkcja,laczniki,abbList]=self.LoadCharsDatabase()
        abbList=["mgr", "prof", "hab"]
        for abb in abbList:
            if (sentence.endswith(abb)):
                result = True
        return result
    
    def MakeClearAndHashedText(self,text):
        '''
        Input: tekst ze źródła, który ma zostać podzielony
        Output: True, jeżeli proces poszedł dobrze (czyli aktualnie zawsze:P)
        Description: użyłem następujących założeń: 1) Szukam substringa zaczynącego się od małej litery i zakończonego .!? Następnie sprawdzam czy ostatnie słowo nie jest skrótem np. mgr. prof. km. Jeżeli tak to to zdanie i następne należy połączyć. Jeżeli ostatnie słowo nie jest skrótem to to zdanie i następne należy rodzielić.
        Nie ma problemu ze wielokrotnymi kropkami itp. ponieważ zostaną usuniętę w metodzie PrepareSectenceToHash
        
        @TODO KAMIL
        
        '''
        
        query = "[A-Z]*[\\.\\?!][ \\n\\t]+" # Zapytanie regex. Wzór: duża litera + coś + kropka, pytajnik, wykrzyknić + spacja enter lub tab
        lista_temp=re.split(query ,text) # Wstępny podział tekstu
        
        lista = [];
        schowek = ""
        for el in lista_temp:
            # usuwanie wielokoptnych spacji, enterów i tebów
            el = " ".join(el.split());
            # sprawdzanie skrotow
            if (self.HasAbb(el)==True):
                schowek = el
            else:
                if (schowek!=""):
                    lista.append(schowek + ". " + el)
                else:
                    lista.append(el)
                schowek = ""
       
        for sentence in lista:
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
            return self.LoadFromPdf(path)
        if(path.find('.txt')>=0):
            return self.LoadFromTxt(path)
        if(path.find('.html')>=0):
            return self.LoadFromHtml(path)      
        if(path.find('.docx')>=0):
            return self.LoadFromDocx(path)
        #MakeError
        return False
    
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
    
    def LoadFromDocx(self,path): 
        """
        Take the path of a docx file as argument, return the text in unicode.
        """
        document = zipfile.ZipFile(path)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)
 
        paragraphs = []
        for paragraph in tree.getiterator(PARA):
            texts = [node.text
                     for node in paragraph.getiterator(TEXT)
                     if node.text]
            if texts:
                paragraphs.append(''.join(texts))
 
        return '\n\n'.join(paragraphs)

    '''Return true if contain www or http
    '''
    def IsLink(self,path):
        '''
        '''
        path=path.lower()
        if (path.startswith('www') or path.startswith('http')): return True
        
        return False
    
    def LinuxPDF(self,path):
        text="";
        script="pdftotext -layout " + pliczek.nazwa;
        nazwa2=pliczek.nazwa.rstrip('pdf')+"txt";
        os.system(script);
        text=open(nazwa2).read();
        return text;
    
 
