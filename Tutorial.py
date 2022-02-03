import time

import numpy as np

import pandas as pd

# define a Series, simply a list of numbers in this case
table = pd.Series([25, 12, 15, 14, 19, 23, 25, 29])

# display that same series
print(table)

# \n is the same thing as enter
print("\n")

# You can use a list instead, just a collection of values
list = [0, 1, 2, 3, 4, 5]

# The index begins at 0.
print(list[0])
print(list[3])

# This will output 0 and 3!

# This creates and prints the list
table_list = pd.Series(list)

print(table_list)

# To do a table, you need to make a dataframe

# Define and print a DataFrame, basically a table
df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23, 25, 29],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

print(df)

# The same list thing would work!
list1 = [1, 2, 3]
list2 = [3, 4, 5]

# Create and print another dataframe
df2 = pd.DataFrame({'list1': list1,
                    'list2': list2})

print(df2)

# Strings are just variables with text
String = str("Hello World")
print(String)

# Ints and floats are either integers - whole numbers - or decimals up to 10 places
Int = 1
Float = 8.675309
print(Int, Float)

# Input is simply input
a = input("Insert text here: ")
print(a)

# When putting ints or floats in a string use the 'f' syntax. Put f at the beginning, and variables in curly brackets
b = str(f'Int is: {Int} and float is: {Float}')

# In the github is an example of for loops. They work by looping through a condition

# in this case, i is your variable. First, i is one. Then, once it carries out all commands, it adds one to i. It will
# keep going until it reaches the end condition, 10 in this case.

for i in range(10):
    print(i)

    # time.sleep just waits 1 second

    time.sleep(1)

# You can also use this for things like lists and strings

for i in String:
    print(i)
    time.sleep(1)

for i in list:
    print(i)
    time.sleep(1)


# Alternatively, you can use a combination

for i in range(3):
    print(list[i])
    time.sleep(1)

# The other file in this github provides an example of these in action! 