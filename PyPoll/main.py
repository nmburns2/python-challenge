# import os and csv
import csv
import os

# set path
path = os.path.join('Resources', 'election_data.csv')

# establish variables   
votes = []
candidates = []
khan = []
li = []
otooley = []
correy = []

# open file
with open (path) as csvfile:
     reader = csv.reader(csvfile, delimiter= ',')
     for x in reader:
        votes.append((x[0]))
        candidates.append((x[2]))

# calculate total votes
total = (len(votes))

print("_______________________")
print("Election Results:")
print("-----------------------")
print(f"Total Votes: {total}")
print("-----------------------")

# calculate votes for each candidate
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

# calculate percentage of votes for each candidate
khans_percent = ((khans_votes/total) * 100)
otooleys_percent = ((otooleys_votes/total) * 100)
lis_percent = ((lis_votes/total) * 100)
correys_percent = ((correys_votes/total) * 100)

print(f"Khan's Votes: {khans_votes}, {khans_percent}%")
print(f"O'Tooley's Votes: {otooleys_votes}, {otooleys_percent}%")
print(f"Li's Votes: {lis_votes}, {lis_percent}%")
print(f"Correy's Votes: {correys_votes}, {correys_percent}%")

# establish winner
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

# set path
out = os.path.join("Analysis", "Election_Analysis.txt")

# write text file
with open (out, 'w') as txt:
   txt.write("_______________________")
   txt.write("Election Results:")
   txt.write("-----------------------")
   txt.write(f"Total Votes: {total}")
   txt.write("-----------------------") 
   txt.write(f"Khan's Votes: {khans_votes}, {khans_percent}%")
   txt.write(f"O'Tooley's Votes: {otooleys_votes}, {otooleys_percent}%")
   txt.write(f"Li's Votes: {lis_votes}, {lis_percent}%")
   txt.write(f"Correy's Votes: {correys_votes}, {correys_percent}%")
   txt.write("-----------------------")
   txt.write(f'Winner: {winner}')
   txt.write("_______________________")






