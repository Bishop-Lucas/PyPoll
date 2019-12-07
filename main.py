# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:55:07 2019

@author: halbe
"""
# Import dependencies
import pandas as pd
import os

# Creating the path
data = "PyPoll/Resources/election_data.csv"

output = open("PyPoll/Resources/PyPoll_output.txt", "a")
data_pd =pd.read_csv(data)

#Calculate total votes
total_votes = data_pd["Voter ID"].count()
#Get list of candidates
candidates = data_pd["Candidate"].unique()
#Get total number of candidates
num_candidates = len(candidates)
#Get election winner
win = data_pd["Candidate"].mode()
wins = list(win)
winner = wins.pop()
l = "Total Votes: " + str(total_votes)
#Print out the Election results and total votes lines
print("Election Results")
print ("------------------------------")
print (l)
print ("------------------------------")
output.write("Election Results")
output.write('\n')
output.write("------------------------------")
output.write('\n')
output.write(l)
output.write('\n')
output.write("------------------------------")
output.write('\n')
#Loop for determining total votes per candidate
for candidate in candidates:
    votes = 0
    
    #Creates a filter for the Canditate column to get the total votes for each candidate
    candidate_filter = data_pd.Candidate == candidate
    
    filtered = data_pd[candidate_filter]
    #Get total votes for each candidate
    votes = filtered["Voter ID"].count()
    #Get percentage of votes and round it to the nearest 3 decimals
    percent = (votes/total_votes)*100
    percent = round(percent,3)
    #Print and output the results for each candidate
    k = candidate + ':' + str(percent) + '% (' + str(votes) + ')'
    print(k)
    output.write('\n')
    output.write(k)
    output.write('\n')


#Print out the winner
print("-----------------------------")
print("Winner: "+ str(winner))
print("-----------------------------")
output.write("-----------------------------")
output.write('\n')
output.write("Winner: ")
output.write(winner)
output.write('\n')
output.write("-----------------------------")