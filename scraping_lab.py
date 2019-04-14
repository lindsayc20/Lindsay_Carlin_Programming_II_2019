# SCRAPING LAB 
# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days by grabbing each of the following:
# Day, date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

# Note: Although it is possible to pull a description of the weather which includes much of this data, that is not the intent.
# However, if you can do it and add the additional info, that works for me.

from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

days = []
day = soup.findAll(class_="date-time")
for day in day:
    days.append(day.text)

dates = []
date = soup.findAll(class_="day-detail clearfix")
for date in date:
    dates.append(date.text)

descriptions = []
titles = []
description = soup.findAll(class_="description")
for description in description[1:]:
    descriptions.append(description)
for i in range(len(descriptions)):
    title = descriptions[i].get("title")
    titles.append(title)

temperatures = []
temperature = soup.findAll(class_="temp")
for temperature in temperature[1:]:
    temperatures.append(temperature.text)

chance_of_precipitation = []
precip = soup.findAll(class_="precip")
for precip in precip[1:]:
    chance_of_precipitation.append(precip.text)

winds = []
wind = soup.findAll(class_="wind")
for wind in wind[1:]:
    winds.append(wind.text)

humidities = []
humidity = soup.findAll(class_="humidity")
for humidity in humidity[1:]:
    humidities.append(humidity.text)

for i in range(10):
    print(days[i] + ",", dates[i] + ":", titles[i], "High temperature of", temperatures[i][0:3] + "F.", "Low temperature of", temperatures[i][3:] + "F.", chance_of_precipitation[i], "chance of rain. Winds to the",  winds[i][0:3], "at" + winds[i][3:-1] + ". " + humidities[i], "humidity.")


# day
# date
# description
# high and low
# chance of rain
# wind
# sentence

