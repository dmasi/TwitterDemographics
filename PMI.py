# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 08:55:46 2014

@author: dmasi
"""
import pickle

def findNYPMI(word):
    h = open('/home/dmasi/TopWords/Code/daily10kDone/NYTotal.txt')
    topNY = pickle.load(h)
    j = open('/home/dmasi/TopWords/Code/daily10kDone/Total.txt')
    Total = pickle.load(j)

    return topNY[word]/Total[word]

def findLAPMI(word):
    h = open('/home/dmasi/TopWords/Code/daily10kDone/LATotal.txt')
    topLA = pickle.load(h)
    j = open('/home/dmasi/TopWords/Code/daily10kDone/Total.txt')
    Total = pickle.load(j)
    return topLA[word]/Total[word]
    
def findNYLAPMI(word):
    num = findNYPMI(word)
    den = findLAPMI(word)
    
    return num/den

def findLANYPMI(word):
    num = findNYPMI(word)
    den = findLAPMI(word)
    
    return num/den