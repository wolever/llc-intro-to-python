weather_file = open("../exercises/big_weather.csv")

for line in weather_file:
    line_data = line.split(",")
    temperature = float(line_data[3])
    if temperature >= 25:
        print(line + "Go to the beach!")
    elif temperature < 25 and temperature > 15:
        print(line + "Still warm enough for ice cream!")
    else:
        print(line + "Wear a sweater and dream of beaches.")    
    
weather_file.close()
