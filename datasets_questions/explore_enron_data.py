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

# finding the first value
for first in enron_data.values():
    print(first)
    break

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

# finding the stock value of James Prentice
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

# finding the number of email messages from Wesley Colwell to persons of interest
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# finding the stock options of Jeffrey K Skilling
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# finding the maximum total payments
payments = {}
for person, value in enron_data.items():
    payment = value["total_payments"]
    name = person
    if payment == 'NaN':
        payment = 0
    payments[name] = payment

for payment in payments.values():
    if payment == max(payments.values()):
        print(payment)

# finding quantified salaries
count_salary = 0
count_no_salary = 0
for value in enron_data.values():
    salary = value["salary"]
    if salary == 'NaN':
        count_no_salary =+ 1
    else:
        count_salary += 1

print(count_salary, count_no_salary)

# finding quantified salaries
count_email = 0
count_no_email = 0
for value in enron_data.values():
    email = value["email_address"]
    if email == 'NaN':
        count_no_email =+ 1
    else:
        count_email += 1

# function is not working
"""
print(count_email, count_no_email)
def quantified_value(values_dict, value_key):
    count_value = 0
    count_no_value = 0
    for values in values_dict:
        value = values[value_key]
        if value == 'Nan':
            count_no_value += 1
        else:
            count_value += 1
    return count_value, count_no_value

quantified_value(enron_data.values(), "salary")    
"""


