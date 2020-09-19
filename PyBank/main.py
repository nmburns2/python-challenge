import csv
import os

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')


#total month needs to be set to 0 so I can count 
totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]


#I need to loop through the data to collect the answers
   for row in reader:
           totalMonth = totalMonth + 1
           totalRevenue = totalRevenue + int(row["Revenue"])

#changes of revenue calculations
           revenue_change = int(row["Revenue"]) - previousRevenue
           previousRevenue = int(row["Revenue"])
           month_of_change = month_of_change + [row["Date"]]

           #Greatest Increase value
           if (revenue_change > greatestIncrease[1]):
               greatestIncrease[1] = revenue_change
               greatestIncrease[0] = row["Date"]

           if (revenue_change < greatestDecrease[1]):
               greatestDecrease[0] = row["Date"]
               greatestDecrease[1] = revenue_change
        
# calculate the average revenue outside of the loop
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


#print the outcomes
output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
)

print(output)

#Write to the text path
