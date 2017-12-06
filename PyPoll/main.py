import csv
from collections import Counter

voter_ids1 = []
candidates1 = []

voter_ids2 = []
candidates2 = []

voter_ids = []
candidates = []

total_percentage = []

# First, we deal with the election_data_1
with open("data/election_data_1.csv", newline='') as csvfile1:
    readcsv1 = csv.reader(csvfile1, delimiter = ",")
    # what is readcsv?
    # readcsv = next(readcsv)
    next(readcsv1, None)
    votes1 = list(readcsv1)
    count_vote1 = len(votes1)
    #print(count_vote1)
    #print(votes)

with open("data/election_data_1.csv", newline='') as csvfile1:
    readcsv1 = csv.reader(csvfile1, delimiter = ",")
    next(readcsv1, None)
    for x in readcsv1:
        voter_id1 = x[0]
        candidate1 = x[2]
        voter_ids1.append(voter_id1)
        candidates1.append(candidate1)
    #print(voter_ids)
    #print(counties)
    #print(candidates)
    counts1 = Counter(candidates1)
    #print(counts1)
    condidate1 = list(counts1.keys())
    vote1 = list(counts1.values())
    #print(condidate1)
    #print(vote1)

# Second, we deal with the election_data_2
with open("data/election_data_2.csv", newline='') as csvfile2:
    readcsv2 = csv.reader(csvfile2, delimiter = ",")
    # what is readcsv?
    # readcsv = next(readcsv)
    next(readcsv2, None)
    votes2 = list(readcsv2)
    count_vote2 = len(votes2)
    #print(count_vote2)
    #print(votes)

with open("data/election_data_2.csv", newline='') as csvfile2:
    readcsv2 = csv.reader(csvfile2, delimiter = ",")
    next(readcsv2, None)
    for x in readcsv2:
        voter_id2 = x[0]
        candidate2 = x[2]
        voter_ids2.append(voter_id2)
        candidates2.append(candidate2)
    #print(voter_ids)
    #print(counties)
    #print(candidates)
    counts2 = Counter(candidates2)
    #print(counts2)
    condidate2 = list(counts2.keys())
    vote2 = list(counts2.values())
    #print(condidate2)
    #print(vote2)

# Now we combine two parties
total_counts = count_vote1 + count_vote2
#print(total_counts)
total_condidates = condidate1 + condidate2
#print(total_condidates)
total_votes = vote1 + vote2
#print(total_votes)
total_percentage1 = [x/total_counts for x in total_votes]
for x in total_percentage1:
    total_percentage2 = "{:.2%}".format(x)
    total_percentage.append(total_percentage2)
#print(total_percentage)

# Let's find the winner
max_votes = max(total_votes)
index_max_votes = total_votes.index(max_votes)
#print(index_max_votes)

# Analysis Results
print('Election Results')
print('-----------------------')
print('Total Votes: ' + str(total_counts))
print('-----------------------')
for i in range(len(total_condidates)):
    print(str(total_condidates[i]) + ' : ' + str(total_percentage[i])
         + '(' + str(total_votes[i]) + ')' )
print('-----------------------')
print('Winner: ' + str(total_condidates[index_max_votes]))
print('-----------------------')

