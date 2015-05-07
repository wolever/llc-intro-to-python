# -*- coding: utf-8 -*-

"""
Now that we know how to loop through files, let's start pulling out some insights about the LLC workshops in 2014

We want to know how many people attended 'National Learn to Code Day' in 2014.
Fortunately, each of those events those *exact* words in the title, so we can look for them (remember, computers are
painfully literal, so your search terms have to match exactly)

Once we know how many people attended last year, we can aim to increase that number in 2015!
"""

import csv

#
# Python strings have a `.find(…)` method that allow you to search for a sequence of characters within a string
# If it finds the string, it will return the 'index' (location) of your term within the whole string
#
learn = 'National Learn to Code Day'
print('CSS Fundamentals in Toronto on National Learn to Code Day'.find(learn))
# 31

print('National Learn to Code Day 2014 Intro to HTML & CSS: Building a Multi-Page Website (Halifax Edition)'.find(learn))
# 0

#
# If you can't find the term within your string, it will return -1
#
print('Kids Learning Code: Intro to Programming with Python'.find(learn))
# -1

workshop_file = open('../exercises/llc-workshop-data.csv')

reader = csv.DictReader(workshop_file)

#
# In the last exercise, we counted all the rows to get the total length.
# This time we only want to count the rows where the 'Event Name' contains 'National Learn to Code Day'
# Any time find has a value `>=` (greater than or equal to) 0 we can increment count, and get the number of attendees
#
count = 0
for row in reader:
    name = row['Event Name']
    if name.find(learn) >= 0:
        count += 1

print(count)
# 798

workshop_file.close()
