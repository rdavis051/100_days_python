#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

# The OLD WAY of getting CSV files ^^^^^^^^^
# Pandas is better - quicker to code and better formatted.
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# old way
avg_temp = sum(temp_list) / len(temp_list)
# new way - with pandas
mean_temp = data["temp"].mean()
# get max number from list
max_temp = data["temp"].max()
print(avg_temp)
print(mean_temp)
print(max_temp)

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Challenge - display row with the max temperature
print(data[data.temp == data["temp"].max()])

# Create a dataframe from scratch
data_dict_2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_2 = pandas.DataFrame(data_dict_2)
print(data_2)

# create csv file
data_2.to_csv("new_data.csv")

# NYC Central Park Squirrel Data
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(squirrel_data_dict)

squirrel_data_2 = pandas.DataFrame(squirrel_data_dict)
print(squirrel_data_2)
squirrel_data_2.to_csv("squirrel_count.txt")