import pandas as panda

from constant.core import PROJECT_DIRECTORY

dataset = panda.read_csv(str(PROJECT_DIRECTORY) + '/src/resources/data/survey-mental-health-tech.csv');

"""
    This file is all about getting query of on csv within
"""

# get_sorted_data_by_age
# This function will return dataset of survey-mental-health-tech.csv by its age
def get_sorted_data_by_age(asc = True):
    return dataset.sort_values(by = 'Age', ascending = asc);

"""
get_raw_data_frame
This function meant to be return the dataset raw in DataFrame data type.
"""
def get_raw_data_frame():
    return dataset