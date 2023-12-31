#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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

from sklearn import tree

<<<<<<< HEAD
clf = tree.DecisionTreeClassifier(min_samples_split=40)

clf = clf.fit(features_train, labels_train)

### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)


from sklearn.metrics import accuracy_score
print(accuracy_score(pred, labels_test))

# finding the number of features (columns)
# print(len(features_train[0]))
=======
### create classifier
clf = tree.DecisionTreeClassifier(min_samples_split=2)

### fit the classifier on the training features and labels
t0 = time()
clf = clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print("Predicting Time:", round(time()-t0, 3), "s")


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(pred, labels_test)
print(accuracy)

>>>>>>> d5ec08e2594e7cfd1e320bae61608994049cc5b0


#########################################################


