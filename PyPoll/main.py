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
print("-----------------")

for y in candidates:
    if y == "Khan":
        khan.append(candidates)
    if y == "O'Tooley":
        otooley.append(candidates)
    if y == 'Li':
        li.append(candidates)
    if y == 'Correy':
        correy.append(candidates)

khans_votes = len(khan)
otooleys_votes = len(otooley)
lis_votes = len(li)
correys_votes = len (correy)

print(khans_votes)
print("-----------------")
print(lis_votes)
print("-----------------")
print (otooleys_votes)
print("-----------------")
print(correys_votes)

