import csv
import numpy as np
import os


with open('billion_elements.csv', 'w') as file_:
    writer = csv.writer(file_)
    for i in range(200):
        writer.writerow(np.random.randint(low=1, high=120, size=5000000))


size = os.path.getsize('billion_elements.csv')

print(f'Size is : {size} byte')

