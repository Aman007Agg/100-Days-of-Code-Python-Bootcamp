import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_counts = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_counts = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_counts = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels)
print(grey_squirrels_counts)
print(red_squirrels_counts)
print(black_squirrels_counts)

data_dict = {
    " Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_counts, red_squirrels_counts, black_squirrels_counts]
}

# print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")