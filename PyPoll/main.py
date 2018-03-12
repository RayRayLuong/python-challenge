#Raymond Luong
import os
import csv

csvpath = os.path.join("election_data_2.csv")
f = open("PollResults.txt", "w+")
votes = {}
totalVotes = 0

#reading csv file, adding candidates to dictionary
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[2] in votes:
            votes[row[2]] += 1
        else:
            votes[row[2]] = 1
votes.pop("Candidate")

for c in votes:
    totalVotes += votes[c]

#Is there a way to print to terminal as well as a text file in the code rather than terminal?(py PyPoll.py >> test.txt)
f.write("Election Results\n")
f.write("-----------------------------\n")
f.write("Total Votes: " + str(totalVotes) + "\n")
f.write("-----------------------------\n")

print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(totalVotes))
print("-----------------------------")
for c in votes:
    percentOfVote = votes[c]/totalVotes * 100
    print(c +": " + format(percentOfVote, '.1f') + "% " + "(" + str(votes[c]) + ")")
    f.write(c +": " + format(percentOfVote, '.1f') + "% " + "(" + str(votes[c]) + ")\n")
print("-----------------------------")
print("Winner: " + max(votes, key=votes.get))

f.write("-----------------------------\n")
f.write("Winner: " + max(votes, key=votes.get))

