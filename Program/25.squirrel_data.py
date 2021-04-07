import pandas
data = pandas.read_csv("25.Squirrel_Data.csv")
# print(data)
gray_squrl_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squrl_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrl_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squrl_count)
print(red_squrl_count)
print(black_squrl_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squrl_count, red_squrl_count, black_squrl_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("25.Squirrel_count.csv")