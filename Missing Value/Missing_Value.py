# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 10:48:29 2015

@author: Leonspirit
"""
 
import numpy as np
import pandas as pd
import copy
 
if __name__=="__main__":
  #1. Load data, perhatikan setiap kolom apa tipe datanya
  data_missing1=pd.read_csv('Horse-Colic-Missing.csv')
  data_missing2=copy.deepcopy(data_missing1)  
  data_missing1.info()
  #print data_missing1.columns#columns used
  #print data_missing1.head(5)
  
  #sortin data
  data_missing1 = data_missing1.sort('outcome', ascending='True')  
  #print data_missing1.head(10)
  
  out=[0,0,0,0]
  for idx, record in data_missing1.iterrows():
      out[int(record.outcome)] = out[int(record.outcome)] + 1
 
  data_miss1 = data_missing1[0:out[1]]
  data_miss2 = data_missing1[out[1]:out[1]+out[2]]
  data_miss3 = data_missing1[out[1]+out[2]:out[1]+out[2]+out[3]]
  
  #2. Cari disetiap kolom index dari yang isinya null / tidak sesuai dengan tipe data masing-masing kolom (Nan)
  #index dengan nama  
  #index_Nan_surgery = data_missing1['surgery'].index[data_missing1['surgery'].apply(np.isnan)]
  #print index_Nan_surgery  
 
  #index tanpa label nama
    
  #modus_kolom.ix[:,2] #memanggil kolom tanpa nama object kolom
  mean1 = data_miss1.mean(axis=0, skipna=True)
  mean2 = data_miss2.mean(axis=0, skipna=True)
  mean3 = data_miss3.mean(axis=0, skipna=True)
  
  median1 = data_miss1.median(axis=0, skipna=True)
  median2 = data_miss2.median(axis=0, skipna=True)
  median3 = data_miss3.median(axis=0, skipna=True)
  
  modus1 = data_miss1.mode(axis=0, numeric_only=True)
  modus2 = data_miss2.mode(axis=0, numeric_only=True)
  modus3 = data_miss3.mode(axis=0, numeric_only=True)
  
  modus1 = modus1.ix[0]
  modus2 = modus2.ix[0]
  modus3 = modus3.ix[0]

  data_full1 = copy.deepcopy(data_miss1)
  data_full2 = copy.deepcopy(data_miss2)
  data_full3 = copy.deepcopy(data_miss3)  
  
  modus_fill=[1,5]
  for t in range (len(modus_fill)):   
      data_full1.ix[:,modus_fill[t]] = data_full1.ix[:,modus_fill[t]].fillna(value=modus1[modus_fill[t]], axis=0)
      data_full2.ix[:,modus_fill[t]] = data_full2.ix[:,modus_fill[t]].fillna(value=modus2[modus_fill[t]], axis=0)
      data_full3.ix[:,modus_fill[t]] = data_full3.ix[:,modus_fill[t]].fillna(value=modus3[modus_fill[t]], axis=0)
  
  median_fill = [2,3,4,6,7,8]
  for t in range (len(median_fill)):
      data_full1.ix[:,median_fill[t]] = data_full1.ix[:,median_fill[t]].fillna(value=median1[median_fill[t]], axis=0)
      data_full2.ix[:,median_fill[t]] = data_full2.ix[:,median_fill[t]].fillna(value=median2[median_fill[t]], axis=0)
      data_full3.ix[:,median_fill[t]] = data_full3.ix[:,median_fill[t]].fillna(value=median3[median_fill[t]], axis=0)
      
  #data_full1.ix[:,1] = data_full1.ix[:,1].fillna(value="dumb", axis=0)
  #print data_full3
  #print modus1[1], median1[2]
  print data_full2
  
  '''  
  index_Nan=[]
  index=[]
  for j in range(len(data_missing1.columns)):
      index_i = data_missing1.ix[:,j].index[data_missing1.ix[:,j].apply(np.isnan)]
      print index_i
      index_Nan.append(index_i)
      #del index_i
  
  #4. Mulai Imputasi klasik
  mean_kolom = data_missing1.mean(axis=0, skipna=True)
  median_kolom = data_missing1.median(axis=0, skipna=True)
  #modus ada perlakuan khusus
  #data_missing2 = data_missing1.fillna(value="NaN", axis=0)
  modus_kolom = data_missing1.mode(axis=0, numeric_only=True) 
  print mean_kolom
  print median_kolom
  modus_kolom = modus_kolom.ix[0] #ambil yang NaN nggak ikut2an
  print modus_kolom  
  
  
  #4.a.  Degan menggunakan mean
  modus_fill=[1,5]
  for t in range(len(modus_fill)):
      print data_missing1.ix[:,modus_fill[t]]
      for i in range(len(index_Nan[modus_fill[t]])):
          data_missing1.ix[:,modus_fill[t]][index_Nan[modus_fill[t]][i]]=modus_kolom[modus_fill[t]]
      print data_missing1.ix[:,modus_fill[t]]
   
  #4.b. Dengan menggunakan median  
  median_fill=[2,3,4,6,7,8]
  for t in range(len(median_fill)):
      print data_missing1.ix[:,median_fill[t]]
      for i in range(len(index_Nan[median_fill[t]])):
          data_missing1.ix[:,median_fill[t]][index_Nan[median_fill[t]][i]]=median_kolom[median_fill[t]]
      print data_missing1.ix[:,median_fill[t]]
  print data_missing1.head(5)
  '''