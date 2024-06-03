# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readline()
#     print(data)


# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

#data = pandas.read_csv('weather_data.csv')
# print(data["temp"])
#
# data_dict = data.to_dict()
# #print(data_dict)
#
# tamp_list = data["temp"].to_list()
# print(tamp_list)
# # avg_temp = round(sum(tamp_list)/len(tamp_list),2)
# # print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Gat data in column
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(monday.temp * 9 /5 +32)


#create a data from scratch
# data_dict = {
#     "students": ["addy", "baddy", "caddy"],
#     "scores": [76, 85, 65]
# }
# dataa = pandas.DataFrame(data_dict)
# dataa.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data["Primary Fur Color"])
grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Data.csv")