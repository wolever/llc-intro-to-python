weather_file = open("../exercises/simple_weather.csv")

for line in weather_file:
    if "warm" in line:
        print(line)
    
weather_file.close()