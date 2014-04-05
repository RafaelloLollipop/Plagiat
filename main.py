from Tkinter import Tk
from tkFileDialog import askopenfilename

class OutFile():
    '''Constructor'''
    def __init__(self,path):
        self.pathToFile="" # Generated File by this class, file contain raport
        self.repeats=[] # list of int,  - no repeat, x - number of senetnce 
        self.hashedText=[] # Text from file transported to List 
        self.raportGenereted=False   # Raport exist checker
        self.Generate(path)
        
    '''Return ->raportGenereted'''
    def GetRaportGenereted(self):
        return self.raportGenereted
     
    '''Return hashedText'''  
    def GetHashedText(self):
        return self.hashedText    
    
    ''' Automatic function started in Constructor    
     Taking path (MUST BE IN CONSUTRCTOR) (local or www) & preapre it
     At finish method start HashText method with clear text
     www, http are REMOVED!! '''
    def Generate(self,path):
        ''' This method end when OutFile is properly created
            TODO: KTOS
        '''
        if (self.IsLink(path)):  # Contain www or http ? 
            pathToDownloadedFile=self.Download(path)  
            text=self.LoadTextFromFile(pathToDownloadedFile)
            text=self.ParseHTML(text)
        else:
            text=text=self.LoadTextFromFile(path)
        
        self.HashText(text)
            
        
        
        return True
    
    '''Delete colons, space, making the letters small'''
    def PrepareSentenceToHash(self,sentence):
        ''' #At return must be completly edited STRING, for ex from sentence "Rafal jest ok." Make "rafaljestok"
        @TODO:KTOS
        '''
        clearedSentence=""
        return clearedSentence
    
    '''Hashing sentence Method'''
    def HashSentence(self,sentece):
        """Hashing sentece 
        parameters:
        sentece - sentence to hash
         for ex. "rafaljestok" -> 23D#@fA25F#2!S
         TODO:KTOS
         """
        hashedSentence=""
        return hashedSentence

    '''Take text, fork text to sentence, prepare it and hash
        At end we get hashedText List - List of senetence hash '''
    def HashText(self,text):
        '''
        text(string) - clear text like " Rafal jest ok. Kamil spoko loko.
        TODO:KTOS
        '''
        
        # Loop
        sentence=""
        sentencePrepared=self.PrepareSectenceToHash(sentence)
        sentenceHash=self.HashSentence(sentencePrepared)
        self.hashedText.append(sentenceHash)
        # End loop
        
        return True

    '''Method take HTML code and delete from it tags, operators etc. At end we have clear text'''
    def ParseHTML(self,HTMLtext):
        '''TODO:KTOS'''
        parsedText=""
        return parsedText

    '''Method get path and return big text from file'''
    def LoadTextFromFile(self,path):
        '''TODO: KTOS '''
        text=''
        return text

    '''Method Download file and return path to it'''
    def Download(self,link):
        '''
        TODO: KTOS
        '''
        pathToFile=''
        return pathToFile
    
    '''Return true if contain www or http'''
    def IsLink(self,sentence):
        '''
        TODO: KTOS
        '''
        return True
    
    '''Method generate raport and save it'''
    def GenerateRaport(self):
        '''
        TODO: KTOS
        '''
        self.raportGenereted=True
        return True
    
class MainFile():
    '''Constructor'''
    def __init__(self, _path):
        self.path=_path  #Path to main File
        self.repeatNumber=[]  # Nie pamietam po chuj to, w domysle bool to mialo byc?XD bool [nameFile]
        self.structure={}  # { sentence : hash }
        self.wwwAdress=[] # Contain a www sites from MainFile
        self.Create() #AutoCreateMethod Start
        
    '''Return structue'''
    def GetStructure(self):
        return self.structure
    
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
        And make structure
    '''
    def Create(self):
        ''' Start all methods
        '''
        text=self.LoadFileText()
        text=self.MakeStructure(text)
        
        return True
    
    '''Delete colonos etc, same in OutFile!'''
    def PrepareSectenceToHash(self,sentence):
        ''' Delete colons, space, making the letters small
        TODO:KTOS SAME IN OUTFILE
        '''
        clearedSentence=""
        return clearedSentence
    
    '''Method started by Create()
    Method taking address from text or bibliography and collect it in the wwwAdress list
    next fork and hash
    '''
    def MakeStructure(self,text):
        ''' This functon at end of work guarantees properly make structure
        TODO: KTOS Analogy to HashText in OUTFILE
        '''
        # Loop
        sentence=""
        if (self.IsLink(sentence)):
            #TODO:KTOS
            # Fork adress
            # Add to wwwAdress
            return False
        else:
            sentenceHash=self.PrepareSectenceToHash(sentence)
            sentenceHash=self.HashSentence(sentence)
            self.structure[sentence]=sentenceHash
        # End loop
        
        return True
    
    '''If start with www or http'''
    def IsLink(self,sentence):
        #TODO:KTOS SAME IN THE OUTFILE
        return True
    
    def LoadFileText(self):
        '''Return text(string) -  content of file
        self.path - path to file
        Remember to parse html !!
        '''
        text=""
        return text
    
    '''Method take HTML code and delete from it tags, operators etc. At end we have clear text'''
    def ParseHTML(self,HTMLtext):
        '''TODO:KTOS analog in OutFile'''
        parsedText=""
        return parsedText
    
    '''Hashing sentence Method'''
    def HashSentence(self,sentece):
        """Hashing sentece 
        parameters:
        sentece - sentence to hash
         for ex. "rafaljestok" -> 23D#@fA25F#2!S
         TODO:KTOS ANALOGICZNE W OUTFILE
         """
        hashedSentence=""
        return hashedSentence



class Source():
    """Main Class of program """
    '''Constructor'''
    def __init__(self):
        self.pathToMainFile="" # .txt,.pdf etc
        self.configPath="" # dunno, nic z tym nie robilem bo nie pamietam jak to tam mialo byc xD
        self.mainFile   # mainFile object
        self.Adress=[] # list of adress when we want to search for OutFile, www & local
        self.OutFiles=[] # List of OutFiles
    
    # Tych dwoch metod nie jestem pewien :D
    '''getery i setery jebac to'''
    def AddOutFile(self,outFile):
        self.OutFiles.append(outFile)
        return True
    
    def GetAdress(self):
        return self.Adress
    
    def AddAdress(self,adress):
        self.Adress.append(adress)
        return True
 
    def RemoveOutFile(self,outFile):
        self.OutFiles.remove(outFile)
        return True 
    
    def RemoveAdress(self,adress):
        self.Adress.remove(adress)
        return True
       
    def LoadChoosedLinks(self):
        ''' this method load all adress choosen from BiographyLinks 
        and show it in the table
        '''
        self.GetAdress()
        return True
    
    def LoadBiographyLink(self):
        ''' this method load all unused adress from wwwAdress list in mainFile object
        and show it in the table
        '''
        self.mainFile.GetwwwAdress()
        return True
    
    def SearchFile(self):
        """ This function return path to File"""
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        self.pathToMainFile=askopenfilename() 
        return True
        
    def PreapreMainFile(self):
        '''Create objectMainFile
        Used after click event
        To add:
        Check pathToMainFile correctness
        '''
        self.mainFile=MainFile(self.pathToMainFile)
        return True
    
    def GenerateOutFile(self):
        '''
        After button click
        '''
        #Loop
        adress=""  # Pobrany z self.Adress
        newOutFile=OutFile(adress)
        self.OutFiles.append(newOutFile)
        #EndOfLopp
        return True
    
    def SearchPlagiarsim(self):
        '''Start crazy machine : D
        '''    
        #Loop
        OutFile=''
        self.CompareHash(OutFile)
        self.GenerateRaport(OutFile)
        #EndOfLoop
        return True

    def CompareHash(self,OutFile):
        ''' Compare  MainFile.structue(use GetStructure Method) with hashedText ( use GetHashedText Method)
        Remember that 1st one is a dictionary, 2nd is list!
        '''
        return True
    
    def GenerateRaport(self,OutFile):
        ''' End when Raport is sucesfully generated
        '''
        OutFile.GenerateRaport()
        return True
    
    def ShowRaports(self):
        ''' Start by click
        '''
        return True 
    
    
#DUNNO

class Main():
    """Open Gui, Load basic classes etc """
    x=0
    
