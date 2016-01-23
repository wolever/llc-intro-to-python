weather_file = open("simple_weather.csv")

for line in weather_file:
    print(line)
    
weather_file.close()