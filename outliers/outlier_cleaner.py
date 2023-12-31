#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).

        training =  90

    """
       
    cleaned_data = []

    ### your code goes here

    for prediction, age, net_worth in zip(predictions, ages, net_worths):
        error = net_worth - prediction
        clean_point = (age, net_worth, error)
        cleaned_data.append(clean_point)

    return cleaned_data


