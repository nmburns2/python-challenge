import csv
import os

month = []
revenue = []
revenue_change = []
total_revenue = 0

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x in reader:
        month.append(x[0])
        revenue.append(x[1])

total_months = len(month) - 1
print(f"Total months: {total_months}")

total_revenue = (total_revenue + int(x[1]))

print(f'Total Revenue: {total_revenue}')

avg_change = (total_revenue / total_months)
print(f'Average Change: {avg_change}')

greatest_increase = max(revenue)
greatest_decrease = min(revenue)

print(f'Greatest Increase: {greatest_increase}')
print(f"Greatest Decrease: {greatest_decrease}")