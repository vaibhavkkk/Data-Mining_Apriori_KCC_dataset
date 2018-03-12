#!/usr/bin/python

import sys

transactions = []
no_of_lines=0 
for line in sys.stdin:
    data = line.strip().split(',')
    if(len(data)==11):
        A,B,C,D,F,G,H,I,J,K,L = data
    transactions.append(data[0]+"\t"+data[2])
    no_of_lines = no_of_lines + 1 


for t in transactions:
    print "[{0}],\t{1}".format(t,1)
    
