import os

os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv>>mean_temp.txt")

temps = open('mean_temp.txt', 'a+')
temps.write('Rio de Janeiro,Brazil,30.0,18.0\n')
temps.seek(0)
headings = temps.readline()
theadings = headings.split(',')
city_temp = temps.readline().split(',')

while city_temp:
        print(headings[2], 'for', city_temp[0], 'is', city_temp[2])
        if city_temp[0] == 'Rio de Janeiro':
                break
        else:
                city_temp = temps.readline().split(',')	


