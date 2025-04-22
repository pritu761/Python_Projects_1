"""with open("weather_data.csv") as file:
    jio=file.read()
    print(jio)"""
"""import csv
temperatures=[]
with open("weather_data.csv") as file:
    jio = csv.reader(file)
    for row in jio:
        print(row)
        if row[1] != "temp":
            temperatures.append((row[1]))
    print(temperatures)"""
"""import pandas
data = pandas.read_csv("weather_data.csv")
print(data)"""
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240727.csv")
black_squirrel = data[data["Primary Fur Color"] == "Black"]
print(black_squirrel)


