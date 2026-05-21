# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)



"""
Reading CSV data in Python
"""

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
print(type(data)) # every table/sheet/ in pandas is pandas.DataFrame
print(type(data["temp"])) # every single column in pandas is pandas.Series- which is a list

data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()
print(temp_list)


# calculating the average temp of the csv file we do have.
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

print(data["temp"].mean())
print(data["temp"].median())
print(data["temp"].mode())
print(data["temp"].max())
print(data.temp)#column name exactly the same as in csv column
print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp)
# monday_temp = monday.temp[0]
monday_temp = monday.temp
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


#Create a DataFrame from scratch
data_dicts = {
    "student": ["Rajani", "Naman", "Aman"],
    "scores": [76, 56, 65]
}

#Creating a csv file from dataframe
data_panda = pandas.DataFrame(data_dicts)
print(data_panda)
data_panda.to_csv("new_test_data.csv")



