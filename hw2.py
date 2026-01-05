# CS1210: HW2
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone else.

def signed():
    return(["jevanderbloemen"])


######################################################################
# Book Class

from string import *
class Book():
    def __init__(self, file):
        '''Initialization method called by class constructor.'''

        #read file into list
        infile = open(file, 'r')
        #removes lines containing only ALL CAPS
        self.text = ''
        for line in infile.readlines():
            if not line.isupper():
                self.text += line
        #close file
        infile.close()

        #cleans up text + words
        self.text = self.cleanUpText(self.text)
        self.words, inxSent = self.cleanUpWords(self.text.split())

        #creates disired tuples from list of indexs
        self.sentences =[]
        for i in range(len(inxSent)-1):
            self.sentences += [(inxSent[i], inxSent[i+1])]
        
        #sets list of syllables
        self.syllables = self.findSyllables()

        #readablity functions
        self.forcast = self.forcast()
        self.ars = self.ars()
        self.fki = self.fki()
        self.cli = self.cli()
        
        
    def cleanUpText(self, text):
        '''takes string of text and cleans it up according to specifications
Returns cleaned up string'''
        
        cleanText = ''
        
        #punctuation w/out ".?!"
        punc = list(punctuation)
        punc.remove(".")
        punc.remove("?")
        punc.remove("!")

        #char is the index of a character in the string
        char = 0
        while char < len(text):
            
            #checks for ' 
            if "'m" == text[char:char+2]: 
                cleanText += " am"
                char += 1 #skip one character (m)
            elif "'d" == text[char:char+2]:
                cleanText += " had"
                char += 1
            elif "'ll" == text[char:char+3]:
                cleanText += " will"
                char += 2
            elif "'ve" == text[char:char+3]:
                cleanText += " have"
                char += 2
            elif "'re" == text[char:char+3]:
                cleanText += " are"
                char += 2
            elif "n't" == text[char:char+3]:
                cleanText += " not"
                char += 2

            #replaces punctuation with space
            elif text[char] in punc:
                cleanText += ' '

            #always end in a period
            elif text[char] in ".?!":
                #skips if consecutive periods
                if cleanText[-1] != ".":
                    cleanText += '.'

            else:
                cleanText += text[char]

            char += 1  #next character
        
        return " ".join(cleanText.split()) #removes extra blank space


    def cleanUpWords(self, words):
        '''takes a list of words remove any remaning periods.
Returns tuple with list of cleaned words and list of index corresponding to end of sentence'''
        cleanWords = []
        inxSent = [0]
        
        for word in words:
            #only account for period at end of word
            if '.' == word[-1]:
                word = word.strip('.')
                cleanWords.append(word)
                #index for end of sentences
                inxSent.append(len(cleanWords))
            else:
                cleanWords.append(word)
            
        return (cleanWords, inxSent)

    
    def findSyllables(self):
        '''returns list of syllables corresponding to words in attribute'''
        syllables = []
        for word in self.words:
            count = 0
            word = (word[:-1] + word[-1].strip('es')).lower()
            for i in range(len(word)-1): 
                #checks for v-c by i+1
                if word[i] in 'aeiou' and word[i+1] not in 'aeiou':
                    count +=1
                #checks for y (not first letter or surrounded by vowels)
                elif i != 0 and word[i] == 'y' and word[i+1] not in 'aeiouy' and word[i-1] not in 'aeiouy':
                    count +=1
                    
            #checks last index
            if word[-1] in 'aeiou':
                count +=1
            elif word[-1] == 'y' and word[-2] not in 'aeiou':
                count +=1
            
            syllables.append(count or 1)
        return syllables


    def forcast(self):
        '''returns readability number based on Forcast Metric'''
        x = 0
        for i in range(len(self.words)):
            if self.syllables[i] == 1:
                x +=1
        return 20 - (x*150)/(len(self.words)*10)


    def ars(self):
        '''returns readability number based on Automated Readability Score'''
        cpw = len("".join(self.text.split()))/len(self.words)
        wps = len(self.words)/len(self.sentences)
        return 4.71 * cpw + 0.5 * wps - 21.43


    def fki(self):
        '''returns readability number based on Flesch-Kincaid Index'''
        wps = len(self.words)/len(self.sentences)
        spw = sum(self.syllables)/len(self.words)
        return 0.39 * wps + 11.8 * spw - 15.59


    def cli(self):
        '''returns readability number based on Coleman-Liau Index'''
        cphw = (len("".join(self.text.split()))-len(self.sentences))/len(self.words)*100
        sphw = len(self.sentences)/len(self.words)*100
        return 0.0588 * cphw - 0.296 * sphw - 15.8

