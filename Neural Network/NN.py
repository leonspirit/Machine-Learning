# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:07:00 2015

@author: Leonspirit
"""

import random
import numpy as np
import pandas as pd

def rand2D(arr):
    now=0.01
    for i in range (arr.shape[0]):
        for j in range (arr.shape[1]):
            #arr[i][j]=random.uniform(-0.1,0.1)
            arr[i][j]=now 
            now=now+0.001
            
def rand3D(arr):
    now=0.01
    for i in range (arr.shape[0]):
        for j in range (arr.shape[1]):
            for k in range (arr.shape[2]):
                #arr[i][j][k]=random.uniform(-0.1,0.1)
                arr[i][j][k]=now
                now=now+0.001


kelas = {'Iris-setosa':np.array([1,0,0]), 'Iris-versicolor':np.array([0,1,0]), 'Iris-virginica':np.array([0,0,1])}
#print kelas['Iris-versicolor']
#print np.mat(a) * np.mat(b)

loc_train="IrisTrain.txt"
loc_test="IrisTest.txt"
loc_submission="answer.txt"

df_train = pd.read_csv(loc_train)
df_test = pd.read_csv(loc_test)

hlayer=1
hunit=5
epoch=30
classes=3
learn_rate = 0.01

feature_cols = [col for col in df_train.columns if col not in ['class'] ]

X_train = df_train[feature_cols]
X_test = df_test[feature_cols]
y_train = df_train['class']
y_test = df_test['class']

attr=0
for col in X_train:
    attr=attr+1

wi = np.zeros((attr+1,hunit))
wh = np.zeros((hlayer-1,hunit+1,hunit))
wo = np.zeros((hunit+1,3))

#randomizing initial weight
rand2D(wi)
rand3D(wh)
rand2D(wo)

a =np.array([[3,0,2],[2,0,1],[1,0,1]])
b =np.array([5.0,1.0,3.0])

for x in range (epoch):
    
    for idx, record in X_train.iterrows():                  
    
        #delta weight
        di = np.zeros((attr+1,hunit))   
        dh = np.zeros((hlayer-1,hunit+1,hunit))
        do = np.zeros((hunit+1,classes))    
    
        #input data
        curr_data = np.zeros((attr+1,1))
        curr_data[0]=1
        
        for y in range(attr):
            curr_data[y+1]=record[y]
        
        #output for hidden + output layer
        oh = np.zeros((hlayer,hunit))
        oo = np.zeros((classes,1))
    
        tmp = np.dot(wi.transpose(),curr_data)
        oh[0] = tmp[:,0]
        
        for y in range(hlayer-1):
            curr_output = np.zeros((hunit,1))
            curr_output[:,0] = oh[y]
            curr_output=np.insert(curr_output,0,1,axis=0)
            
            tmp = np.dot(wh[y].transpose(),curr_output)
            oh[y+1] = tmp[:,0]
        
        curr_output = np.zeros((hunit,1))
        curr_output[:,0] = oh[hlayer-1]
        curr_output = np.insert(curr_output,0,1,axis=0)
        
        tmp = np.dot(wo.transpose(),curr_output)
        oo[:,0] = tmp[:,0]
        
        #print oo, kelas[y_train[idx]]
        #error for output + hidden layer
        errh = np.zeros((hlayer,hunit))
        erro = np.zeros((classes,1))
        
        actual_class = np.zeros((classes,1))
        actual_class[:,0]=kelas[y_train[idx]]        
        
        #print actual_class
        #compute error output
        erro = oo*(1-oo)*(actual_class-oo)
        #erro = actual_class-oo
        #print erro
        
        #print oh[hlayer-1]
        #compute error hidden
        tmp = wo[1:,:]
        errh[hlayer-1] = oh[hlayer-1]*(1-oh[hlayer-1])*(np.reshape(np.dot(tmp,erro),hunit))
        
        idlayer = hlayer-2
        for y in range(hlayer-1):
            tmp = wh[idlayer,1:,:]
            errh[idlayer] = oh[idlayer]*(1-oh[idlayer])*(np.reshape(np.dot(tmp,errh[idlayer+1]),hunit))
            idlayer = idlayer-1
            
        #print errh[0]
        #compute delta weight input
        tmp2 = np.zeros((hunit,1))
        tmp2[:,0] = errh[0]
        di = di + (learn_rate * np.dot(curr_data,tmp2.transpose()))
        
        #compute delta weight output
        tmp = np.zeros((hunit,1))
        tmp[:,0]=oh[hlayer-1]
        tmp=np.insert(tmp,0,1,axis=0)
        tmp2 = np.zeros((classes,1))
        tmp2 = erro
        do = do + (learn_rate * np.dot(tmp,tmp2.transpose()))
        
        er = sum(erro)
        #print er
        for y in range(hlayer-1):
            tmp = np.zeros((hunit,1))
            tmp[:,0] = oh[y]
            tmp = np.insert(tmp,0,1,axis=0)
            tmp2 = np.zeros((hunit,1))
            tmp2[:,0] = errh[y+1]
            dh[y] = dh[y] + (learn_rate * np.dot(tmp,tmp2.transpose()))
        
        #update weight value
        wi = wi+di
        wh = wh+dh
        wo = wo+do
        
with open(loc_submission, "wb") as outfile:
    outfile.write("ID, Predicted Class\n")
    for idx, record in X_test.iterrows():
        curr_data = np.zeros((attr+1,1))
        curr_data[0]=1
        
        for y in range(attr):
            curr_data[y+1]=record[y]
        
        oh = np.zeros((hlayer,hunit))
        oo = np.zeros((classes,1))
    
        tmp = np.dot(wi.transpose(),curr_data)
        oh[0] = tmp[:,0]
        
        for y in range(hlayer-1):
            curr_output = np.zeros((hunit,1))
            curr_output[:,0] = oh[y]
            curr_output=np.insert(curr_output,0,1,axis=0)
            
            tmp = np.dot(wh[y].transpose(),curr_output)
            oh[y+1] = tmp[:,0]
        
        curr_output = np.zeros((hunit,1))
        curr_output[:,0] = oh[hlayer-1]
        curr_output = np.insert(curr_output,0,1,axis=0)
        
        tmp = np.dot(wo.transpose(),curr_output)
        oo[:,0] = tmp[:,0]
        
        ans = ' '
        if oo[0]>oo[1] and oo[0]>oo[2]:
            ans='Iris Setosa'
        elif oo[1]>oo[0] and oo[1]>oo[2]:
            ans='Iris Virginica'
        else:
            ans='Iris Versicolor'
        
        outfile.write("%s, %s\n" % (y_test[idx],ans))
        