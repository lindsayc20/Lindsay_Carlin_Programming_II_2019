# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("/Users/lindsaycarlin/Desktop/Programming/Programming II 2019/Notes/data/Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)
print(data)
print(data[0][6])

schools_list = []
square_footage = []
ghg_emissions = []
ghg_intensity = []
for i in range(len(data)):
    if data[i][6] == 'K-12 School':
        try:
            square_feet = float(data[i][7])
            emissions = float(data[i][20])
            intensity = float(data[i][21])
            schools_list.append(data[i][2])
            square_footage.append(square_feet)
            ghg_emissions.append(emissions)
            ghg_intensity.append(intensity)
        except ValueError:
            print("Could not convert values to floats")

print(schools_list)
print(square_footage)
print(ghg_emissions)

ghg_intensity = [[schools_list[x], ghg_intensity[x]] for x in range(len(ghg_intensity))]

for cur_pos in range(len(ghg_intensity)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(ghg_intensity)):
        if ghg_intensity[scan_pos][1] < ghg_intensity[min_pos][1]:
            min_pos = scan_pos
    ghg_intensity[cur_pos], ghg_intensity[min_pos] = ghg_intensity[min_pos], ghg_intensity[cur_pos]

plt.figure(1, figsize=(12, 6))
plt.scatter(square_footage, ghg_emissions, s=10)
plt.title("Square Footage vs. Greenhouse Gas Emissions in Chicago's K-12 Schools")
plt.xlabel("Square footage")
plt.ylabel("Greenhouse gas emissions")

for i in range(3):
    intensity = ghg_intensity[i]
    print(intensity)
    school_data = schools_list.index(intensity[0])
    plt.scatter(square_footage[school_data], ghg_emissions[school_data], s=10, color="green")
    plt.annotate(ghg_intensity[i][0], xy=(square_footage[school_data], ghg_emissions[school_data]), rotation=315)

for i in range(1212, 1215):
    intensity = ghg_intensity[i]
    print(intensity)
    school_data = schools_list.index(intensity[0])
    plt.scatter(square_footage[school_data], ghg_emissions[school_data], s=10, color="red")
    plt.annotate(ghg_intensity[i][0], xy=(square_footage[school_data], ghg_emissions[school_data]), rotation=315)

francis_parker = schools_list.index('Francis W Parker School')
print(schools_list[francis_parker])
plt.scatter(square_footage[francis_parker], ghg_emissions[francis_parker], s=10, color="black")
plt.annotate(schools_list[francis_parker], xy=(square_footage[francis_parker], ghg_emissions[francis_parker]), rotation=315)
# create a best fit line

m, b = np.polyfit(square_footage, ghg_emissions, 1)
fit_x = [0, 700000]
fit_y = [b, 16000]
plt.plot(fit_x, fit_y, color="black")

plt.show()
