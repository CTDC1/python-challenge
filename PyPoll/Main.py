#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:22:20 2023

@author: cameroncullen
"""

# import necessary modules for homework
import os
import csv

cwd = os. getcwd ()

# creating variables that will be used later
total_votes = 0 
cans = {}
winner = {}
winnervotes =0

#naming a variable, so we can later save the results in a text file 
my_report = open("analysis/final_report.txt", "w")

#calling from my computers documents to find the csv final we want to analysis
csvpath = os.path.join(cwd, "Resources/election_data.csv")

#once we have called the csv file, we have to put it in a format that is readable, as well as tell the code how the columns are divided
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#skip the first row of the csv file   
    next(csvreader)
    
# a for loop that loops though the csv, and reads the document. we know the votes are in column B and the candidates are in column 2
#we add 1 to total votes so we know how many rows to count
    for row in csvreader:
          total_votes += 1
          can = row[2]

#this if loop determins in the name of the candidate name is in the dictonary 
          if can not in cans.keys():
#if they are not the votes count in set to zero                
              cans[can] = 0
#this moves increase the row number by 1, allowing us to move through the csv document              
          cans[can] += 1
                   
         


# we have name our ouput data as "output" so we do not have to create multiple print statements   
# in line 61 we add on to the output statment. within that fstring, we are calculating the percentage of votes as well. 
# in line 67 we are calculating the winner, with a for loop. we look at the candidate and their votes. if the candidates votes were 
# larger than the previous, we change the name and the vote count.   
output = f"""\nElection Results

-------------------------
Total Votes: {total_votes}

-------------------------\n\n"""

for can in cans.keys():
    output += f"{can}: {cans[can]/total_votes * 100:.3f}% ({cans[can]})\n\n"


output += f"-------------------------\n\n"

for can, total_votes in cans.items():
    if total_votes > winnervotes:
        winner = can
        winnervotes = total_votes
        
output+= f"Winner: {winner}\n\n"

output += f"------------------------"

#we are printing our statement, as well as saving it in a text file on my computer
print(output)
my_report.write(output)