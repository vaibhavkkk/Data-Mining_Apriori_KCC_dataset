#!/usr/bin/python

import sys

# Loop around the data

print "Pairings ", "\t", "Number of queries"
print "============================"

A={}
B={}
C={}
for line in sys.stdin:
##    print (line)
    split_line = line.strip().split("**")
#    print (split_line)
    if len(split_line) == 1 :
        for x in split_line:
            x=x[0:len(x)]
	    x=x[1:]
	    x=x[:-1]	
#            print (x)
            S=x.split(",")
            if S[0] in A:
                A[S[0]]+=1
            else:
                A[S[0]]=1  
    if len(split_line)==2:
        for x in split_line:
       	    x=x[0:len(x)]
            x=x[1:]
	    x=x[:-1]	
#            print (x)
            j=x.split(" ")
            if j[0] in B:
                B[j[0]]+=1
            else:
                B[j[0]]=1	 
    if len(split_line)==3:
        for x in split_line:
            x=x[0:len(x)]
            x=x[1:]
	    x=x[:-1]	
#            print (x)
            j=x.split(" ")
            if j[0] in C:
                C[j[0]]+=1
            else:
                C[j[0]]=1

x=0
s=""
for k in C:
    z=k.split(",")
#    print (z)
    s="["+z[0]+"]"
    print "{0}\t{1}".format(s,str(C[k]))

x=0
s=""
for k in B:
    z=k.split(",")
#    print (z)
    s="["+z[0]+"]"
    print "{0}\t{1}".format(s,str(B[k]))

x=0
s=""
for k in A:
    s="["+k+"]"
    print "{0}\t{1}".format(s,str(A[k]))

