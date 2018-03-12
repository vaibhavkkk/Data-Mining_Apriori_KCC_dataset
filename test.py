#!/usr/bin/python

import sys

def count_first(transactions):
    adict = {}
    for t in transactions:
        for item in t:
            if item in adict:
                adict[item] += 1
#                print (item, 1)
            else:
                adict[item] = 1
#               print (item, 1)
                
    return adict 

def candidate_gen(keys):
    adict={}
    for i in keys:
        for j in keys:
            if i != j and (min(i,j),max(i,j)) not in adict:
                adict[tuple([min(i,j),max(i,j)])] = 0
#                print "{0}\t{1}".format(i,j)
    return adict

def add_frequency(Candidate, transactions):
    s=""
    v=0
    for key in Candidate:
        for t in transactions:
            if key[0] in t and key[1] in t:
                if(v!=0):
                    s=s+"^"
                s=s+"["+key[0]+" "+key[1]+","+str(1)+"]"
                v=v+1
                Candidate[key] += 1
#	        print "{0}\t{1}\t{2}".format(key[0],key[1],1)
#                print (key[0],key[1],1)
    		
    return s

def candidate_gen3(keys):
    adict={}
    for i in keys:
        for j in keys:
            for k in keys:
                if i!=j and j!=k and i!=k and (k,j,i) not in adict:
                    a=min(i,j,k)
                    b=max(i,j,k)
                    if i!=a and i!=b:
                        c=i
                    if j!=a and j!=b:
                        c=j
                    if k!=a and k!=b:
                        c=k
                    #min(i,j,k),max(i,j,k)
                    adict[tuple([a,c,b])] = 0
    return adict;

def add_frequency3(Candidate, transactions):
    s=""
    v=0
    for key in Candidate:
        for t in transactions:
            if key[0] in t and key[1] in t and key[2] in t:
                Candidate[key] +=1
                if(v!=0):
                    s=s+","
                s=s+"["+key[0]+" "+key[1]+" "+key[2]+","+str(1)+"]"
                v=v+1
                Candidate[key] += 1
#	        print "{0}\t{1}\t{2}".format(key[0],key[1],1)
#                print (key[0],key[1],1)
    return s

transactions = []
no_of_lines=0
for line in sys.stdin:	
    data = line.strip().split(',')
    transactions = []
    transactions.append(data[0:4])
#    print(transactions)
#    print("****************")
    C=count_first(transactions)
    s=""
    x=0
    for k in C:
        if(x!=0):
            s=s+"**"
        s+="["+k+"," + str(C[k]) +"]"
        x=x+1
    print (s)                 
    CD=candidate_gen(C.keys())
    A=add_frequency(CD,transactions)
    print (A)
    no_of_lines = no_of_lines + 1 
    C3 = candidate_gen3(C.keys())
#    print (C3)
    F3 = add_frequency3(C3,transactions)
#    print ("===============3=========")
    print (F3)


