

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

