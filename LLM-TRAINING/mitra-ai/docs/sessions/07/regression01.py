import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model

# Load the dataset
#df = pd.read_csv('homes.csv')

"""
# Plot the data
plt.xlabel('Area in sqft')
plt.ylabel('Price in USD')
plt.scatter(df.area, df.price, color='red', marker='+')

# Display the plot
plt.show()

"""


df = pd.read_csv('homes.csv')
new_df = df.drop('price', axis='columns')  # Dropping the 'price' column

area = df[['area']]  # Correct way to extract 'area' column as a DataFrame
print(type(area))  # Check the type of 'area'
price = df.price
print(price)

reg = linear_model.LinearRegression()
print(reg.fit(area,price))

print(reg.predict([[3300]]))

print(reg.predict([[1240]]))

