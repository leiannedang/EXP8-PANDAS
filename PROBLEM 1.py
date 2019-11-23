
"""
Created on Sat Nov 23 12:50:00 2019

@author: Angela Leenzae Edang
"""

''' PROBLEM 1:
a) Load the corresponding .csv file into a data frame named cars using pandas
b) Display the first five and last five rows of the resulting cars. '''

import pandas as pd

cars = pd.read_csv('cars.csv')
df = cars 

print('\n')

print('First five rows of "cars.csv": \n')
print(cars.head()) # displays the first five rows of cars
print('Last five rows of "cars.csv": \n')
print(cars.tail()) # displays the last five rows of cars
