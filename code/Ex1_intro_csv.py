# -*- coding: utf-8 -*-
"""
Python is said to come with 'batteries included' – a number of utility libraries available with the standard installation

In this exercise, we'll open a CSV file with one of the built-in utilities and read some data from a row.
"""

import csv

#
# In order to read a CSV file. First, we need to open the file (the reader needs file input)
#
chapters_file = open('./llc-chapters.csv')

#
# Then we use the DictReader to parse that file. It will read the first row, and expose each subsequent row as a
# dictionary where the column header is the key for the corresponding value in that row.
#
reader = csv.DictReader(chapters_file)

#
# As long as there are rows left to read, you can call `.next()` and get a dictionary for that row
#
row1 = reader.next()
print(row1)
# {'City': 'Vancouver', ' Chapter Lead(s)': ' Meghan', ' Province': ' BC'}

row2 = reader.next()
print(row2)
# {'City': 'Calgary', ' Chapter Lead(s)': ' Darcie ', ' Province': ' AB'}

#
# Since we've got a dictionary, we can print out the value by accessing it with a valid key
#
print(row1['City'])
# Vancouver

#
# When you're done with a file, it's best to close it
#
chapters_file.close()
