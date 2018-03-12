#!/usr/bin/python

import sys

# Loop around the data

print "Sector ", "\t", "Number of queries"
print "============================"

def count_first(transactions):
    adict = {}
    for t in transactions:
        for item in t:
            if item in adict:
                adict[item] += 1
            else:
                adict[item] = 1                
    return adict 

def getSeasonCount(transactions):
    for t in transactions:
        print "{0}\t{1}".format(t,transactions[t])	

transactions = []
no_of_lines=0 

for line in sys.stdin:
    split_line = line.strip().split("\t")
    if len(split_line )!=2:
	continue
    transactions.append(split_line[0:1])

C1 = count_first(transactions)
getSeasonCount(C1)

