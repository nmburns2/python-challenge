# import os and csv
import csv
import os

# establish variables
month = []
revenue = []
revenue_change = []
total_revenue = 0

# set path
csv_path = os.path.join('Resources', 'budget_data.csv')

# open file and skip header
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    x = next(reader, None)
    for x in reader:
        month.append(x[0])
        revenue.append(x[1])

# calculate total months
total_months = len(month)
print(f"Total months: {total_months}")

# calculate total revenue
total_revenue = (total_revenue + int(x[1]))
print(f'Total Revenue: {total_revenue}')

# calculate average change
avg_change = (total_revenue / total_months)
print(f'Average Change: {avg_change}')

# calculate increases
greatest_increase = max(revenue)
greatest_decrease = min(revenue)
print(f'Greatest Increase: {greatest_increase}')
print(f"Greatest Decrease: {greatest_decrease}")

# set path
out = os.path.join('Analysis', 'Bank_Analysis')

# write text file
with open (out, 'w') as txt:
    txt.write(f"Total months: {total_months}")
    txt.write(f'Total Revenue: {total_revenue}')
    txt.write(f'Average Change: {avg_change}')
    txt.write(f'Greatest Increase: {greatest_increase}')
    txt.write(f"Greatest Decrease: {greatest_decrease}")
