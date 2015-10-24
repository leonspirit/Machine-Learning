# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:41:41 2015

@author: Leonspirit
"""

import numpy as np
import time
import pandas as pd
from sklearn import svm, ensemble

loc_train="IrisTrain.txt"
loc_test="IrisTest.txt"
loc_submission="answer.txt"

df_train = pd.read_csv(loc_train)
df_test = pd.read_csv(loc_test)

feature_cols = [col for col in df_train.columns if col not in ['class'] ]

X_train = df_train[feature_cols]
X_test = df_test[feature_cols]
y = df_train['class']
test_ids = df_test['class']

clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

start_time = time.time()
clf.fit(X_train, y)

train_time = time.time() - start_time

correct=0.0
alldata=0.0
with open(loc_submission, "wb") as outfile:
    outfile.write("ID, Class\n")
    for e, val in enumerate(list(clf.predict(X_test))):
        alldata = alldata+1
        if test_ids[e]==val :
            correct = correct+1
        outfile.write("%s, %s\n" % (test_ids[e],val))
    outfile.write("Accuracy : %.2lf%%\n" % ((correct/alldata)*100))
    outfile.write("Time Elapsed : %.4lf\n" % (train_time))
    