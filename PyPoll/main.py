import csv
import os

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

votes = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

for x in csvreader:
    votes.append(int(x[0]))
    county.append(int(x[1]))
    candidates.append(int(x[2]))

total = (len(votes))

print(total)