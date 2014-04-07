import nltk   
import StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader
import urllib


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
        ''' #At return must be completly edited STRING, for ex from sentence "Rafal jest ok." Make "rafaljestok"
        @TODO:KAMIL
        '''
        clearedSentence=""
        return clearedSentence
    
        '''Hashing sentence Method'''
    def HashSentence(self,sentece):
        """Hashing sentece 
        parameters:
        sentece - sentence to hash
         for ex. "rafaljestok" -> 23D#@fA25F#2!S
         TODO:KAMIL
         """
        hashedSentence=""
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

