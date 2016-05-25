# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:43:49 2016

@author: Leonspirit
"""
import csv
import numpy as np

def subList(x1, y1, x2, y2, grid):
    return [item[x1:x2] for item in grid[y1:y2]]

with open('wdbc.csv','rb') as csvfile:
    cancerData = csv.reader(csvfile, delimiter=',')
    cancerData = list(cancerData)
    
rows = len(cancerData)
fields = len(cancerData[0])

cancerData = np.array(cancerData)

for i in range (2,fields):
    print cancerData[0][i]
    temp = cancerData[1:rows, i:i+1].astype(float)
    print "Max : %f" % (np.max(temp))
    print "Min : %f" % (np.min(temp))
    print "Mean : %f" % (np.mean(temp))
    print "Stdev : %f" % (np.std(temp))
   