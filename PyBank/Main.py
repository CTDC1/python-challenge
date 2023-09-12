#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:22:20 2023

@author: cameroncullen
"""

import os
import csv

# Path to collect data from the Resources folder
# You need to specify the path to your CSV file here#


# The total number of months included in the dataset
cwd = os. getcwd ()

#naming a variable, so we can later save the results in a text file 
my_report = open("analysis/final_report.txt", "w")

#calling from my computers documents to find the csv final we want to analysis
csvpath = os.path.join(cwd, "Resources/budget_data.csv")

#naming the variables
found = False
months = 0
total = 0
total_ch = 0
pre_pl = 0
inc = ["", 0]
dec = ["", 0]

#once we have called the csv file, we have to put it in a format that is readable, as well as tell the code how the columns are divided
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip the first line of the csv file 
    next(csvreader)
    
#we are counting the amount of months there are on the csv file and adding them to a variable 'months'
    for row in csvreader:
            months += 1
            
            
 #we are summing up the total amount of value changes in the months by adding up the interger of the cells in column B
            pl = int(row[1])
            total += pl
          
#we are comparing the change between different months by comparing the cell we are in to the last cell
# if the cell we are in is larger than the largest, then change the total_ch to the new change
            change = pl - pre_pl
            if pre_pl == 0:
                change = 0
            total_ch += change
            
#The greatest increase in profits (date and amount) over the entire period
# if the change is larger than the last increase, then change the string to the month, and the value 
            if change > inc[1]:
                inc[0] = row[0]
                inc[1] = change
                
                
#The greatest decrease in profits (date and amount) over the entire period
# if the change is largest than the largest decrease, then change the string to the month, and the value 

            if change < dec[1]:
                dec[0] = row[0]
                dec[1] = change
                
            pre_pl = pl



# we have created an f string or our dataprint. this is easier than writing multiple print lines
# For Avgerage, Greatest Increase, Greatest Decrease, we are using string formatting solution to print the numerical number in the format that the question asked for
# We also calcuate the Average Change in the print statement so we don't have to create an additional variable, and write extra lines of code

output = f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})"""

# print statement for output
print(output)

#creating a text document for our results 
my_report.write(output)