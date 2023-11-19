import numpy as np

temps = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]

product = 1
num_items = len(temps)
print(num_items)
for i in temps:
    product *= i
print(product)
    
square_product = product**(1/num_items)
print(square_product)