#read the csv file named precipitation_mean_Spain.csv and print the contents
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('precipitation_mean_Spain.csv')
print(df)

# Plot time serie of precipitation in Spain along the years
df.plot(x='time', y='precipitation')
# add title and labels
plt.title('Precipitation in Spain')
plt.xlabel('Year')
plt.ylabel('Accumulated Precipitation (mm)')

plt.show()