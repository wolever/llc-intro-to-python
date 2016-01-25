weather_file = open("big_weather.csv")

for line in weather_file:
    line_data = line.split(",")
    print("Line data: " + str(line_data))
    
weather_file.close()
