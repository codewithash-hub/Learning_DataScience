import numpy as np

temps = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]

mean = np.mean(temps)
l = []

for temp in temps:
    s = (temp - mean) **2
    l.append(s)
    
    
a = np.mean(l)

std = np.sqrt(a)

print(std)

