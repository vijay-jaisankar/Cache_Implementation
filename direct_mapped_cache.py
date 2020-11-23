# IMT2019525 VIJAY JAISANKAR
import math 
from argparse import ArgumentParser

# Helper Functions
def convert_decimal_to_binary(n):
    return bin(n).replace("0b","")

def convert_binary_to_decimal(b):
    s = b.replace("0b","")
    return int(s,2)

class DirectMappedCache:
    # Instance Variables
    _numHits = None 
    _numMiss = None 
    _numberOfBlocks = None 
    _tags = [] # This is a list of all the tags
    _valid_bits = [] # This is a list of all the valid bits
    
    # Constructor
    def __init__(self):
        self._numHits = 0
        self._numMiss = 0
        self._numberOfBlocks = int(math.pow(2,16))
        for i in range(self._numberOfBlocks):
            self._valid_bits.append(0)
            self._tags.append(None)
    
    # Converts the given address into tag bits and decimal index
    def sortTheAddress(self,addr):
        tag = addr[0:14]
        index = addr[14:29]
        decimalIndex = convert_binary_to_decimal(index)
        offset = addr[30:]
        l = []
        l.append(tag)
        l.append(decimalIndex)
        return l 
    
    # Checks hit/miss and updates cache(if required)
    def updateCache(self,addr):
        l = self.sortTheAddress(addr)
        tag = l[0]
        decimalIndex = l[1]
        val = self._valid_bits[decimalIndex]
        tagOriginal = self._tags[decimalIndex]
        # Cache hit
        if tag == tagOriginal and val == 1:
            self._numHits += 1
        # Cache miss
        else:
            self._numMiss += 1
            # Updating the cache
            self._valid_bits[decimalIndex] = 1
            self._tags[decimalIndex] = tag 

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
        





if __name__ == "__main__":
    # Taking input from command line 
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
    args = parser.parse_args()
    myFile = args.myFile
    
    # Initialises the cache
    d = DirectMappedCache()
    
    with open(myFile,'r') as f:
        for line in f:
            # Filtering the address
            s = line.split(' ')
            addr = s[1].replace("0x","")
            integer = int(addr,16)
            x = format(integer, '0>32b')
            # Updating the cache
            d.updateCache(x)

    # Printing the descriptors
    print('Total number of accessed = ',d.getTotalAccesses())
    print('Number of hits = ',d.getNumHits())
    print('Number of misses = ',d.getNumMiss())
    print('Hit rate = ',d.getHitRate())
    print('Miss rate = ',d.getMissRate())
    print('Hit/Miss rate = ',d.getHitvsMissRate())
    print(' ')
    print(' ')

    
            