# data = []
# with open ("./23.weather_data.csv") as weather_data:
#     add_data = weather_data.readlines()
#     data.append(add_data)

# print(data)

# import csv
# with open ("./23.weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperarure = []
#     for row in data:
#         if row[1] != "temp":
#             temperarure.append(int(row[1]))

#     print(temperarure)

import pandas
total = 0
data = pandas.read_csv("23.weather_data.csv")
# print(data)
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
# print(temp_list)
# for ele in range(0, len(temp_list)):
#     total = total+temp_list[ele]

# average = sum(temp_list)/len(temp_list)

# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.condition)
print(data[data.temp == data.temp.max()])
monday  = data[data.day == "Monday"]
print(monday.condition)

# with open("file.txt", "w") as wri:
#     wri.write(str(data_dict))


