import csv

csv_file = open('llc-chapters.csv')
csv_data = csv.DictReader(csv_file)

count = 0
for row in csv_data:
    count += 1

print("There are " + str(count) + " chapters")
