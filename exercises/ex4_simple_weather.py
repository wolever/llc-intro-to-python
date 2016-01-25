weather_file = open("simple_weather.csv")

for line in weather_file:
    # TODO: only print the line if it's a warm month
    # (hint: use an if statement and the in operator)
    print(line)
    
weather_file.close()
