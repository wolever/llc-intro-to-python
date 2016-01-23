weather_file = open("../exercises/big_weather.csv")

temp_list = []

for line in weather_file:
    line_data = line.split(",")
    temp = int(line_data[3])
    temp_list.append(temp)
    
# outside the for loop means we have read all the lines
average_temp = sum(temp_list) / len(temp_list)
print("The average temperature is " + str(average_temp))
     
    
weather_file.close()