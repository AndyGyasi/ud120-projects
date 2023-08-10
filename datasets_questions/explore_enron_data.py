#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

#with open("../final_project/final_project_dataset_unix.pkl", "rb") as filename:
#   enron_data = joblib.load(filename)

enron_data = joblib.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

# finding the size of the dataset
print(len(enron_data))
print(enron_data.items())

# finding the number of features
for first in enron_data.values():
    print(len(first))
    break

# finding the number of persons of interest 
count = 0
for person, value in enron_data.items():
    if value["poi"] == True:
        count += 1
print(count)

with open("../final_project/poi_names.txt", "rb") as filename:
    enron_poi = filename.read()

print(enron_poi)
