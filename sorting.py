import csv
from csv import writer
import os

file = open("billion_elements.csv")
csvreader = csv.reader(file)
age_dict = {}
for row in range(200):
    iter_list = list(next(csvreader))

    for i in iter_list:
        if i in age_dict:
            age_dict[i] += 1
        else:
            age_dict[i] = 1

    del iter_list

print(age_dict)
file.close()

with open('sorted_billion_elements.csv', 'a') as f_object:
    writer_object = writer(f_object)
    for key in sorted(age_dict):
        writer_object.writerow([key] * age_dict[key])

size = os.path.getsize('sorted_billion_elements.csv')

print(f"Size is {size} bytes")
