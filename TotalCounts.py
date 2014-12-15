# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 09:27:24 2014

@author: dmasi
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 13:23:18 2014

@author: dmasi
"""

import sys, json, os.path, pickle
#sys.path.insert(0,'/h/brendano/proc')
#sys.path.insert(0,'/mal1/brendano/twi/twproc/proc')
#sys.path.insert(0, os.path.join(os.path.dirname(__file__),'../nlp'))
from Twokenize import tokenizeRawTweetText
from pprint import pprint
from collections import Counter
#def processText(text):
#    
#    return
#
#def TopWords(fileName):
#    f = open(fileName)
#    
#    
#    
#    return

#parallel -j 3 -- < myFileWithCommands.txt
def main(fileName):
#    cur_dir= os.getcwd()    
    content = open(fileName).read().splitlines()
    Total = Counter()
    NY = Counter()
    LA = Counter()
    
    for lines in content:
    
        NYFileName = 'NY/' + lines
        LAFileName = 'LA/' + lines
        TotalFileName = 'Total/' + lines
    
        NYFile = open(NYFileName, 'r')
        NYCounts = pickle.load(NYFile)
        NY = NY + NYCounts
        NYFile.close()    
    
        LAFile = open(LAFileName, 'r')
        LACounts = pickle.load(LAFile)
        LA = LACounts + LA
        LAFile.close()    
    
        TotalFile = open(TotalFileName, 'r')
        TotalCounts = pickle.load(TotalFile)
        Total= Total + TotalCounts
        TotalFile.close()
    
    
    NYFile = open('NYTotal.txt', 'w+')
    pickle.dump(NY, NYFile)
    NYFile.close()    
    
    LAFile = open('LATotal.txt', 'w+')
    pickle.dump(LA, LAFile)
    LAFile.close()    
    
    TotalFile = open('Total.txt', 'w+')
    pickle.dump(Total, TotalFile)
    TotalFile.close()
    

    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
