# -*- coding: utf-8 -*-

"""
As we saw in the previous exercise, the DictReader gives us a dict for each row when you call `.next()`

The `for` loop automatically picks up on the `.next()` (an iterable) so you can inspect each row in the file
until it reaches the end

We can use a variable to count the number of loops, and that will give us the total number of rows in the file
"""

import csv

chapters_file = open('../exercises/llc-chapters.csv')

reader = csv.DictReader(chapters_file)

count = 0
for row in reader:
    print(row)
    #
    # += is the same are writing `count = count + 1`
    #
    count += 1

print(count)
# 16

chapters_file.close()
