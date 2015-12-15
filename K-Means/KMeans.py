# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:58:09 2015

@author: Leonspirit
"""

import numpy as np
import pandas as pd
import scipy
import copy
import random

cluster = 2
epoch = 20
loc_train="DataTrain.txt"

df_train = pd.read_csv(loc_train)

init_centroid = np.zeros(0)

attr=0
for col in df_train:
    attr=attr+1

for x in range (cluster):
    while 1:
        idx = random.randint(0,len(df_train)-1)
        
        g=0
        for y in range (len(init_centroid)):
            if init_centroid[y]==idx:
                g=1
        
        if g==0:
            init_centroid = np.append(init_centroid,idx)
            break
'''
init_centroid = np.append(init_centroid,1)
init_centroid = np.append(init_centroid,3)
'''
centroids = np.zeros((cluster,attr))

for x in range (cluster):
    #centroids[x] = df_train.ix[init_centroid[x]]
    centroids[x] = df_train.ix[int(init_centroid[x])]

assign = np.zeros(len(df_train))

for x in range (epoch):
    
    subcluster = [[] for _ in range(cluster)]
    #subcluster = np.asarray(subcluster)
    for y in range (len(df_train)):
        maxs = 999999
        for z in range (cluster):
            tmp = np.linalg.norm(df_train.ix[y]-centroids[z])
            if tmp < maxs:
                maxs = tmp
                assign[y] = z
        subcluster[int(assign[y])].append(df_train.ix[y].tolist())
    
    subcluster = np.asarray(subcluster)
    
    for y in range (cluster):
        centroids[y] = np.mean(subcluster[y],axis=0)
    
#print centroids

for x in range (len(df_train)):
    maxs = 99999
    clust = -1
    for y in range (cluster):
        tmp = np.linalg.norm(df_train.ix[x]-centroids[y])
        if tmp<maxs:
            maxs = tmp
            clust = y
    print 'Data ke-%d masuk cluster %d' % (x+1,clust+1)
    
    