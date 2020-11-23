# IMT2019525 VIJAY JAISANKAR
import math 
from argparse import ArgumentParser
import random

# Helper Functions
def convert_decimal_to_binary(n):
    return bin(n).replace("0b","")

def convert_binary_to_decimal(b):
    s = b.replace("0b","")
    return int(s,2)

# Each index of the cache consists of 4 wayElements - these form the 'ways'
class wayElement:
    # Instance Variables
    _tag = None
    _valid = None 
    
    # Constructor
    def __init__(self):
        self._tag = None
        self._valid = 0 
    
    # Setter functions
    def setTag(self,tag):
        self._tag = tag 
    
    def setValid(self,val):
        self._valid = val 

    # Getter functions
    def getTag(self):
        return self._tag
    
    def getValid(self):
        return self._valid

# The main cache class
class SetAssociativeCache:
    # Instance variables
    _numHits = None 
    _numMiss = None 
    _numberOfBlocks = None 
    _indexLists = []
    _numberOfWays = None

    # Constructor
    def __init__(self):
        self._numHits = 0
        self._numMiss = 0
        self._numberOfBlocks = int(math.pow(2,14))
        self._numberOfWays = 4
        # Each index has 4 way elements
        for i in range(self._numberOfBlocks):
            l = []
            for j in range(self._numberOfWays):
                l.append(wayElement())
            self._indexLists.append(l)
    
    # Converts the given address into tag bits and decimal index
    def sortTheAddress(self,addr):
        tag = addr[0:16]
        index = addr[16:30]
        decimalIndex = convert_binary_to_decimal(index)
        offset = addr[30:]
        l = []
        l.append(tag)
        l.append(decimalIndex)
        return l 


    # Computes the descriptors
    def getNumHits(self):
        return self._numHits
    
    def getNumMiss(self):
        return self._numMiss
    
    def getTotalAccesses(self):
        return self._numHits + self._numMiss
    
    def getHitRate(self):
        return self._numHits/(self.getTotalAccesses())
    
    def getMissRate(self):
        return self._numMiss/(self.getTotalAccesses())
    
    def getHitvsMissRate(self):
        return self._numHits/self._numMiss

    # Checks hit/miss and updates cache(if required)
    def updateCache(self,addr):
        l = self.sortTheAddress(addr)
        tag = l[0]
        decimalIndex = l[1]
        listOfWays = self._indexLists[decimalIndex]
        # Cache hit - in any of the ways
        for i in range(self._numberOfWays):
            originalTag = listOfWays[i].getTag()
            val = listOfWays[i].getValid()
            if originalTag == tag and val == 1:
                self._numHits+=1 
                return 
        # We add into the first(by index) empty spot - as indicated by Tag being None
        for i in range(self._numberOfWays):
            originalTag = listOfWays[i].getTag()
            val = listOfWays[i].getValid()
            # Updating the cache
            if originalTag == None or val == 0:
                self._numMiss+=1
                self._indexLists[decimalIndex][i].setTag(tag) 
                self._indexLists[decimalIndex][i].setValid(1)
                return 

        # If all are full, we replace the first way - FIFO
        self._indexLists[decimalIndex][0].setTag(tag) 
        self._indexLists[decimalIndex][0].setValid(1)
        self._numMiss += 1 


if __name__ == "__main__":
    # Taking input from command line
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
    args = parser.parse_args()
    myFile = args.myFile
    
    # Initialises the cache
    sa = SetAssociativeCache()
    
    with open(myFile,'r') as f:
        for line in f:
            # Filtering the address
            s = line.split(' ')
            addr = s[1].replace("0x","")
            integer = int(addr,16)
            x = format(integer, '0>32b')
            # Updating the cache
            sa.updateCache(x)

    # Printing the descriptors
    print('Total number of accessed = ',sa.getTotalAccesses())
    print('Number of hits = ',sa.getNumHits())
    print('Number of misses = ',sa.getNumMiss())
    print('Hit rate = ',sa.getHitRate())
    print('Miss rate = ',sa.getMissRate())
    print('Hit/Miss rate = ',sa.getHitvsMissRate())
    print('')
    print('')

    
         
                
