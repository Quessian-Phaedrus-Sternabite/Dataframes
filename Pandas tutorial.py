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
