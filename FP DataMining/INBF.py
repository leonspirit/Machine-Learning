# -*- coding: utf-8 -*-
"""
Created on Mon May 09 08:27:39 2016

@author: Leonspirit
"""

import csv
import random
import numpy as np

def myInt(myList):
    return map(int, myList)
    
def comparator(myItem):
    return myItem[0]


global field, record, offset, itr, alpha, cancerData, vecW, vecU, vecFS, vecFC, L, K
itr = 100
alpha = 0.6
field = 32
record = 569
offset = 2
L = 5
K = 5

#vector weight (W), inisialisasi random
vecW = np.random.uniform(low=0.0, high=1.0, size=field-2 )

with open('wdbc.csv','rb') as csvfile:
    cancerData = csv.reader(csvfile, delimiter=',')
    cancerData = list(cancerData)

'''
li = [(1,2), (3,4), (5,6)]
li[0][0]=4
print li
'''

global maks
#preprocess normalisasi data
for j in range(offset,field):
    maks = -99999
    mins = 99999
    for i in range(1,record+1):
        cancerData[i][j] = float(cancerData[i][j])
        maks = max(maks, cancerData[i][j])
        mins = min(mins, cancerData[i][j])
    
    #normalisasi data agar data pada range 0..1
    for i in range(1,record+1):
        cancerData[i][j] = (cancerData[i][j] - mins) / (maks - mins)
    
#feature selection IBNF
for t in range(itr):
    #pick random instance
    selectedRecord = random.randint(1,record)
    dist = [(0,0) for x in range(record+1)] 
    
    #calculate distance using vector W
    for i in range(1,record+1):        
        temp = dist[i]
        temp = list(temp)
        temp[1] = i
        temp = tuple(temp)
        dist[i] = temp
        
        for j in range(offset, field):
            jarak = cancerData[selectedRecord][j] - cancerData[i][j]
            jarak = jarak * jarak
            
            temp = dist[i]
            temp = list(temp)
            temp[0] = temp[0] + (jarak * vecW[j - offset])
            temp = tuple(temp)
            dist[i] = temp
        
    #sort the distance to find K nearest neighbour and L farthest neighbour
    dist[1:record] = sorted(dist[1:record], key=comparator)
    vecFC = [0 for x in range(field-2)]
    vecFS = [0 for x in range(field-2)]
    vecU = [0 for x in range(field-2)]
    
    #calculate vector U
    for i in range(offset,field):
        
        #Feature Compactness for feature i
        for j in range(offset, K+offset):
            neighbour = int(dist[j][1])
            cost = cancerData[selectedRecord][i]-cancerData[neighbour][i]
            cost = abs(cost)
            vecFC[i-offset] = vecFC[i-offset] + cost
        vecFC[i-offset] = vecFC[i-offset]*-1
        vecFC[i-offset] = vecFC[i-offset]/K
        
        #Feature Separability for feature i
        for j in range(record-L+1, record):
            neighbour = int(dist[j][1])
            cost = cancerData[selectedRecord][i]-cancerData[neighbour][i]
            cost = abs(cost)
            vecFS[i-offset] = vecFS[i-offset] + cost
        vecFS[i-offset] = vecFS[i-offset]/L
        
        #calculate vector U, and update vector W
        vecU[i-offset] = vecFC[i-offset] + vecFS[i-offset]
        vecW[i-offset] = vecW[i-offset] + (alpha * (vecU[i-offset] - vecW[i-offset]) )
    
    #decrease learning rate for each iteration
    alpha = alpha * 0.9
 
#uncomment to print weight vector (W)   
#print vecW
featureSelection = [(0,0) for x in range(field-2)]

for i in range(len(vecW)):
    temp = featureSelection[i]
    temp = list(temp)
    
    temp[0] = vecW[i]
    temp[1] = i+1
    temp = tuple(temp)
    
    featureSelection[i] = temp
    
featureSelection = sorted(featureSelection, key=comparator, reverse=True)

#uncomment to print sorted weight vector and the attributes
#print featureSelection

features = 10
for i in range(features):
    idx = featureSelection[i][1]
    print "Weight : %f, Attribute : %s" % (featureSelection[i][0], cancerData[0][idx+offset-1])
    
    