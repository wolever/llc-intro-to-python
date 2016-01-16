import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
          'September', 'October', 'November', 'December']

file = open('big_weather_data.txt', 'w')

for _ in range(1000):
    day = random.choice(days)
    month = random.choice(months)
    date = random.randint(1, 31)
    temp = random.randint(-20, 35)
    file.write(day + ',' + month + ',' + str(date) + ',' + str(temp) + '\n')
file.close