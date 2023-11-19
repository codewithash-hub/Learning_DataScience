import numpy as np

temperature = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]

sorted_temp = sorted(temperature)

# Median
median = np.median(sorted_temp)
print(median)

# Mean
mean = np.mean(sorted_temp)
print(mean)
# or
mean2 = sum(sorted_temp) / len(sorted_temp)
print(mean2)
