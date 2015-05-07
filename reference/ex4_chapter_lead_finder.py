# Import the csv library
import csv

# Open the 'llc-chapters.csv' file
csv_file = open('../exercises/llc-chapters.csv')

# Convert it to a csv_data structure
csv_data = csv.DictReader(csv_file)

# Loop through each of the rows
for row in csv_data:
    # Compare the 'City' in the row with your city
    if (row['City'] == 'Vancouver'):
        # Print "Thank you [[Chapter Lead(s)]]!"
        print("Thank you " + row['Chapter Lead(s)'] + "!")
