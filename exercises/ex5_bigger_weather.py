weather_file = open("big_weather.csv")

for line in weather_file:
    line_data = line.split(",")
    print line_data[0], line_data[1], line_data[2]
    
weather_file.close()