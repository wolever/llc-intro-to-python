import csv
import os

csv_file = open(os.path.join('..', 'llc-chapters.csv'))
csv_data = csv.DictReader(csv_file)

count = 0
for row in csv_data:
    count += 1

print("Il y a " + str(count) + " chapitres")
