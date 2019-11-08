import os
import csv

#poll is used to store candidate name and vote count
#creates list used to store candidates, vote counts, vote percent, and winner list
#Set variable for total votes as a counter, starting at 0
poll = {}
candidates = []
number_votes = []
vote_percent = []
winner_list = []
total_votes = 0

#create path for file
file = os.path.join('resources', 'election_data.csv')

#open csv file
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread)

    #using the file, column 3 is stored as a key and each name is used once
    #counts votes for each candidate
    #add 1 to total vote count for each loop equivalent to each row
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#keys and values are stored into the lists for poll.items
#append candidates key and number votes value
for key, value in poll.items():
    candidates.append(key)
    number_votes.append(value)

#append vote percent
for n in number_votes:
    vote_percent.append(round(n/total_votes*100, 1))

#zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, number_votes, vote_percent))

#append winner list
for name in clean_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])

#makes winner_list as a string with the first entry
winner = winner_list[0]

#when there is a tie, additional winners are added into a string that is separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_file = os.path.join('..','Output', 'election_results.txt')

with open(output_file, 'w') as text:
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write('Total Votes: ' + str(total_votes) + '\n')
    text.write('-------------------------\n')
    for entry in clean_data:
        text.write(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    text.write('------------------------- \n')
    text.write('Winner: ' + winner + '\n')
    text.write('-------------------------')

#prints file to as read file
with open(output_file, 'r') as readfile:
    print(readfile.read())