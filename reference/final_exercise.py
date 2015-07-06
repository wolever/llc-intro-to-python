import csv

workshops_file = open('../exercises/llc-workshop-data.csv')
workshops_data = csv.DictReader(workshops_file)

# Initialise our counts
learn_code_count = 0
year_youth_count = 0
youth_learn_code_count = 0
for participant in workshops_data:
    event_name = participant['Event Name']
    if event_name.find('National Learn to Code Day') >= 0:
        # Count participants with "National Learn to Code Day" in the 'Event Name'
        learn_code_count += 1
        if event_name.find('Kids Learning Code') >= 0 or event_name.find('Girls Learning Code') >= 0:
            # Total number of people registered for youth events at "National Learn to Code Day"
            youth_learn_code_count += 1

    # Total number people registered for "Kids Learning Code" or "Girls Learning Code" events throughout the year
    if event_name.find('Kids Learning Code') >= 0 or event_name.find('Girls Learning Code') >= 0:
        year_youth_count += 1

# Print the numbers as part of a friendly message (cast to string)
print(str(learn_code_count) + " attended National Learn to Code Day")
print(str(year_youth_count) + " attended Kids or Girls Learning Code events")
print(str(youth_learn_code_count) + " attended Kids or Girls Learning Code events at National Learn to Code Day")
