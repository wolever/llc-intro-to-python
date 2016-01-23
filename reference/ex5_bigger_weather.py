weather_file = open("../exercises/big_weather.csv")

for line in weather_file:
    line_data = line.split(",")
    weather = int(line_data[3])
    if weather >= 25:
        print(line + "Go to the beach!")
    elif weather < 25 and weather > 15:
        print(line + "Still warm enough for ice cream!")
    else:
        print(line + "Wear a sweater and dream of beaches.")    
    
weather_file.close()