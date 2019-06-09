# declare dependencies
import csv
from collections import Counter
import os

election_data_csv = os.path.join('election_data.csv')
newfile = os.path.join('Election_Results.txt')

with open (election_data_csv, newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    csv_header = next(election_data, None)  # skip the headers

    #declare variables
    vote_count = Counter() 
    candidate = [] 
    percentage = [] 
    output = [] 

# loop to read csv file 
    for row in csvreader: 
        candidate.append(row[2])

# variable for count of total votes
    total_votes = len(candidate)

# loop to count number of times each candidate is in the list
    for name in candidate: 
        vote_count[name] += 1

# variables to declare the candidate name, votes and winner
    winner = max(zip(vote_count.values(), vote_count.keys())) 
    cand_names = tuple(vote_count.keys())
    cand_votes = tuple(vote_count.values())

# loop to get the percentage of votes for each candidate
    for x in cand_votes:
        percentage.append((int(x)/total_votes)*100) 

# append all information to the output list and print
    output.append('Election Results')
    output.append('-----------------------')
    output.append('Total Votes: ' + str(total_votes))
    output.append('-----------------------')
    for x in range(len(cand_names)):
        output.append(cand_names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(cand_votes[x]) + ')')
    output.append('-----------------------')
    output.append('Winner: ' + winner[1])
    output.append('-----------------------')

    print("\n".join((output)))

# write ouput to txt file
with open(newfile, 'w') as txtfile:
    txtfile.write('\n'.join(output))
