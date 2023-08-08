#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

from sklearn.svm import SVC
# clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000.0)

#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data

# reducing the dataset to speed up algorithm, trade off between speed and accuracy
features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]

t0 = time()
clf = clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

#### store your predictions in a list named pred
t0 = time()
pred = list(clf.predict(features_test))
print("Predicting Time:", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

# finding data points
answer_10 = pred[10]
answer_26 = pred[26]
answer_50 = pred[50]

print(acc, answer_10, answer_26, answer_50)


