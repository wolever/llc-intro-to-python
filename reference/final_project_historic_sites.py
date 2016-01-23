data_file = open("../datasets/historic_sites.csv")

# first line is just headers
data_file.next()

province_counts = {}

for line in data_file:
    data = line.split(",")
    province = data[6]
    if province in province_counts:
        province_counts[province] += 1
    else:
        province_counts[province] = 1

# some of this data is messy, so ignoring anything with count of 5 or less
for province in province_counts:
    if province_counts[province] > 5:
        print(province + ": " + str(province_counts[province]))
        
data_file.close()
    