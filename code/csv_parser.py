"""
- How many people attended events in your city in 2014?
- How many people attended youth events in 2014?
- How many people attended a python or ruby workshop in 2014?
- How many people were volunteers/mentors in 2014?
"""

import csv


def attendees_in_city(city, reader):
    attendee_count = 0
    for row in reader:
        if row['Event Name'].find(city) > 0:
            attendee_count += 1

    print("%d people attended events in %s in 2014" % (attendee_count, city))


def youth_event_attendees(reader):
    attendee_count = 0
    for row in reader:
        name = row['Event Name']
        if name.find('Kid') > 0 or name.find('Girl') > 0:
            attendee_count += 1

    print("%d people attended youth events in 2014" % attendee_count)


def py_ruby_workshops(reader):
    python_count = 0
    ruby_count = 0
    for row in reader:
        name = row['Event Name']
        if name.find('Python') > 0:
            python_count += 1
        elif name.find('Ruby') > 0:
            ruby_count += 1

    print("Ruby got %d attendees while Python got %d" % (ruby_count, python_count))


def volunteers(reader):
    volunteer_count = 0
    Volunteer_count = 0

    for row in reader:
        ticket_type = row['Ticket Type']
        if ticket_type.find('mentor') > 0 or ticket_type.find('volunteer') > 0:
            volunteer_count += 1
        elif ticket_type.find('Mentor') > 0 or ticket_type.find('Volunteer') > 0:
            Volunteer_count += 1

    print("There were %d volunteers or mentors, but %d Volunteers or Mentors. Wait, what??" % (volunteer_count, Volunteer_count))


def main(filename):
    workshop_file = open(filename)

    reader = csv.DictReader(workshop_file)

    attendees_in_city("Vancouver", reader)

    workshop_file.seek(0)
    youth_event_attendees(reader)

    workshop_file.seek(0)
    py_ruby_workshops(reader)

    workshop_file.seek(0)
    volunteers(reader)

    workshop_file.close()

if __name__ == '__main__':
    main('llc-workshop-data.csv')
