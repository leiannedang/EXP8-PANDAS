
"""
Created on Sat Nov 23 13:08:58 2019

@author: Angela Leenzae Edang
"""

import pandas as pd

''' PROBLEM 2:
Using dataframe cars in the previous problem, extract the following 
information:
    a) display the first five rows with odd-numbered columns of cars.
    b) Display the row that contains the 'Model' of 'Mazda RX4'.
    c) How many 'cyl' does the car model 'Camaro Z28' have?
    d) How many 'cyl' and what 'gear' type do the car models 'Mazda
        RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have. '''

# To display the first five rows with odd-numbered columns of cars
print('First five rows with odd-numbered columns of cars: \n')
print(df.iloc[0:5, [1,3,5,7,9,11]])
print('\n')

# To display the row that contains the 'Model' of 'Mazda RX4'
print('Information about Model: Mazda RX4 \n')
print(df[df['Model'] == 'Mazda RX4'])
print('\n')

# To display number of cylinders of Camaro Z28
print('Number of cylinders of Camaro Z28: \n')
print(df.loc[23, ['cyl']])
print('\n')

# To display the number of cylinders and gear type of Mazda RX4 Wag,
# Ford Pantera L, and Honda Civic
print('Number of cyclinders and Gear Type of 3 Car Models: \n')
print(df.loc[[1,18,28], ['Model', 'cyl', 'gear']])
print('\n')
