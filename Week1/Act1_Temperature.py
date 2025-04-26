import numpy as np
temperatures = np.array([18.5, 19, 20, 25, 2, 30, 13.9])

# Print the average temperature
print("Average temperature:", round(np.mean(temperatures), 2))

# Find the highest and lowest temperature
print("Highest temperature:", np.max(temperatures))
print("Lowest temperature:", np.min(temperatures))

# Convert all temperatures to Fahrenheit
temperatures_f = (temperatures * 9/5) + 32
print("Temperatures in Fahrenheit:", temperatures_f)

# Identify the days (by index) with temperatures above 20 degrees Celsius
hot_days = np.where(temperatures > 20)[0]
print("Days with temperatures above 20 degrees Celsius:", hot_days)
