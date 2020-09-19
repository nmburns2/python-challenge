import csv
import os

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')



print(output)


