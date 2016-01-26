weather_file = open('big_weather.csv')
month_counts = {}
for line in weather_file:
    month = line.strip().split(',')[1]
    if month in month_counts:
        month_counts[month] += 1
    else:
        month_counts[month] = 1
print month_counts