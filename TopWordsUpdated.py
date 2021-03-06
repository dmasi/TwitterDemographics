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
    f = open(fileName)
    NY = Counter()
    LA = Counter()
    Total = Counter()
    
    for lines in f:
        
        parts  = lines.split('\t')
        geoinfo = json.loads(parts[0])

        if geoinfo['country_iso3'] != 'USA':
            continue
        tweet = json.loads(parts[1])
        
        temp = tokenizeRawTweetText(tweet['text'])
        
        #Boundary box for LA
        if -119 < geoinfo['lonlat'][0] < -117.5 and 33.5 < geoinfo['lonlat'][1] < 34.5:
            LA += Counter(temp)
        #Boundary box for NY            
        elif -74 < geoinfo['lonlat'][0] < -73.5 and 40.5 < geoinfo['lonlat'][1] < 41:
            NY += Counter(temp)
        else:
            Total += Counter(temp)
            
            
    f.close()
    
    
#    if len(tokensNY) > 10:   
#        pprint(Counter(tokensNY).most_common(10))
#    if len(tokensLA) > 10:
#        pprint(Counter(tokensNY).most_common(10))
#    pprint(len(tokensNY))
#    pprint(len(tokensLA))
    

    

    

#    dir = os.path.dirname(NYFileName)
#    try:
#        os.stat(dir)
#    except:
#        os.mkdir(dir)  
        
#    dir_path = os.path.join(self.feed, self.address)  # will return 'feed/address'
#    os.makedirs(dir_path)                             # create directory [current_path]/feed/address
#    output = open(os.path.join(dir_path, file_name), 'wb')
    
    path = os.path.split(fileName)
#    tweetData = path[1].split('.')[0]
    tweetData = path[1]
    
    NYCounts = Counter(tokensNY)
    LACounts = Counter(tokensLA)
    TotalCounts = Counter(tokensTotal) + NYCounts + LACounts
    
    NYFileName = 'NY/' + tweetData
    LAFileName = 'LA/' + tweetData
    TotalFileName = 'Total/' + tweetData
    
    
    if not os.path.exists(os.path.dirname(NYFileName)):
        os.makedirs(os.path.dirname(NYFileName)) 
    NYFile = open(NYFileName, 'w+')
    pickle.dump(NYCounts, NYFile)
    NYFile.close()
    
    if not os.path.exists(os.path.dirname(LAFileName)):
        os.makedirs(os.path.dirname(LAFileName)) 
    LAFile = open(LAFileName, 'w+')
    pickle.dump(LACounts, LAFile)
    LAFile.close()    
    
    if not os.path.exists(os.path.dirname(TotalFileName)):
        os.makedirs(os.path.dirname(TotalFileName))     
    TotalFile = open(TotalFileName, 'w+')
    pickle.dump(TotalCounts, TotalFile)
    TotalFile.close()
    
#    NYFile = open(NYFileName, 'r')
#    c = pickle.load(NYFile)
#    NYFile.close()
#    
#    if len(c) > 5:   
#        pprint(c.most_common(5))
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))