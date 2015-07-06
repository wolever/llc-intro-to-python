#
# The DictWriter allows you to write the contents of a *dict* as a *row* in a new CSV file
# When you initialise the DictWriter, you pass the fieldnames you want written to the file so that you can filter out
# unneeded data from the rows. This also means you will always have the right number of columns in your file (remember
# you need the headers to match the order of the data exactly)
#

import csv

# By default, open assumes you're reading a file
workshops_file = open('../exercises/llc-workshop-data.csv')
workshops_data = csv.DictReader(workshops_file)

# open takes a second 'mode' argument that allows you to get a file ready to 'write in binary mode' so we can output
filtered_file = open('filtered.csv', 'wb')
# Note: We're reading the fieldnames from the llc-workshop-data.csv so the DictWriter knows what to write to the file
filtered_writer = csv.DictWriter(filtered_file, workshops_data.fieldnames)

# Write the headers first so we know what data we're putting into the filtered.csv
filtered_writer.writeheader()

for participant in workshops_data:
    event_name = participant['Event Name']
    if event_name.find('National Learn to Code Day') >= 0:
        # We're writing only the National Learn to Code Day participants to the new filtered file
        filtered_writer.writerow(participant)

filtered_file.close()
workshops_file.close()
