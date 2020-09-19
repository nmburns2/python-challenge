import csv
import os

path = os.path.join('Resources', 'election_data.csv')
   
votes = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

with open (path) as csvfile:
     reader = csv.reader(csvfile, delimiter= ',', lineterminator = '/n')
     for x in reader:
        votes.append((x[0]))
        county.append((x[1]))
        candidates.append((x[2]))

total = (len(votes))

print(total)