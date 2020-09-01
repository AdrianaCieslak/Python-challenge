import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

#Variables
votes = 0
candidates = {}
percentage = []
votes_per_candidate = []
winner = ""
winning_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    next(csvreader)

    for row in csvreader:
        #Total votes
        candidate_name = row[2]
        if candidate_name not in candidates.keys():
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1
        votes += 1
    #Candidates percentage
    for x in candidates:
        print(100 * candidates[x] / votes) 
        print(x)
    
        if candidates[x] > winning_votes:
            winner = x
            winning_votes = candidates[x]
        
    print(candidates)
    print(votes)
    print(winner)
    print(winning_votes)

#Output
print_string = "Election Results\n" \
"...................................\n" \
f"Total Votes: {votes}\n" \
".....................\n" \
f"{candidates}{100 * candidates[x] / votes:.2f} %{x}\n" \
".........................\n" \
f"Winner: {winner}\n" 







#Create txt file
with open(os.path.join("..", "Analysis_2", "output.txt"), "w") as file:
    file.write(print_string)
