import csv

csv_file = open('../exercises/llc-chapters.csv')
csv_data = csv.DictReader(csv_file)

count = 0
for row in csv_data:
    if row['Chapter Lead(s)'].find("&") >= 0:
        count += 1
        print(row['City'])

print(str(count) + " cities have co-leads")
