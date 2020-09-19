import csv
import os

path = os.path.join('Resources', 'election_data.csv')
   
votes = []
candidates = []
khan = []
li = []
otooley = []
correy = []

with open (path) as csvfile:
     reader = csv.reader(csvfile, delimiter= ',')
     for x in reader:
        votes.append((x[0]))
        candidates.append((x[2]))

total = (len(votes))

print("_______________________")
print("Election Results:")
print("-----------------------")
print(f"Total Votes: {total}")
print("-----------------------")

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

khans_percent = ((khans_votes/total) * 100)
otooleys_percent = ((otooleys_votes/total) * 100)
lis_percent = ((lis_votes/total) * 100)
correys_percent = ((correys_votes/total) * 100)

print(f"Khan's Votes: {khans_votes}, {khans_percent}%")
print(f"O'Tooley's Votes: {otooleys_votes}, {otooleys_percent}%")
print(f"Li's Votes: {lis_votes}, {lis_percent}%")
print(f"Correy's Votes: {correys_votes}, {correys_percent}%")

if khans_votes > max(lis_votes, otooleys_votes, correys_votes):
    winner = "Khan"
if lis_votes > max(khans_votes, otooleys_votes, correys_votes):
    winner = "Li"
if otooleys_votes > max(khans_votes, correys_votes, lis_votes):
    winner = "O'Tooley"
if correys_votes > max(khans_votes, otooleys_votes, lis_votes):
    winner = "Correy"


print("-----------------------")
print(f'Winner: {winner}')
print("_______________________")




