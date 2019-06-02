# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
#2  Plot bus usage for the same years as a second line on your graph. (5pts)
#3  Plot bus and rail usage together on a third line on your graph. (5pts)
#4  Add a title and label your axes. (5pts)
#5  Add a legend to show data represented by each of the three lines. (5pts)

plt.figure(1)

with open("/Users/lindsaycarlin/Desktop/Programming/Programming II 2019/Notes/data/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)
print(data)

years = [int(x[0]) for x in data[20:]]
rail_usage = [int(x[3]) for x in data[20:]]
bus_usage = [int(x[1]) for x in data[20:]]
total_ridership = [int(bus_usage[x]) + int(rail_usage[x]) for x in range(len(bus_usage))]
print(rail_usage)
print(bus_usage)
print(total_ridership)

graph = plt.figure(1, tight_layout=True)

plt.plot(years, rail_usage, label = "Rail")
plt.plot(years, bus_usage, label = "Bus")
plt.plot(years, total_ridership, label = "Total")

plt.xlabel('Year')
plt.ylabel('Number of riders')
plt.title('CTA Ridership 2008-2017: Bus, Rail, Total')
plt.legend()
plt.axis([2008, 2017, 0, 550000000])

plt.show()

#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)

# I see an overall increase in rail usage, a decrease in bus usage, and a decrease in total ridership.
# Possible explanation for increase in rail usage: more traffic causing people to abandon bus, rideshare, driving and take the train, which faces delays but no traffic
# Possible explanation for decrease in bus usage: more people buying cars or using rideshare such as Uber and Lyft, or taking the train
