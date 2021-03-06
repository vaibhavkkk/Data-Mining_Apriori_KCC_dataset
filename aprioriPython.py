minsup = 0.3
minconf = 0.8 
def count_first(transactions):
    adict = {}
    for t in transactions:
        for item in t:
            if item in adict:
                adict[item] += 1
            else:
                adict[item] = 1
    return adict 
def find_frequent(Candidate, minsup, no_of_lines):
    adict={}
    for key in Candidate:
        if ((float)(Candidate[key]/no_of_lines)) >= minsup:#minsup
            adict[key] = Candidate[key]   
    return adict 
def candidate_gen(keys):
    adict={}
    for i in keys:
        for j in keys:
            if i != j and (j,i) not in adict:
                adict[tuple([min(i,j),max(i,j)])] = 0
    return adict 
def add_frequency(Candidate, transactions):
    for key in Candidate:
        for t in transactions:
            if key[0] in t and key[1] in t:
                Candidate[key] += 1
    return Candidate

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
    for key in Candidate:
        for t in transactions:
            if key[0] in t and key[1] in t and key[2] in t:
                Candidate[key] +=1
    return Candidate

def get(Candidate):
    a='RABI'
    b='AGRICULTURE'
    c='Cereals'
    for key in Candidate:
        if a in key and b in key and c in key :
            return Candidate[key]




    
f = open("agri.txt","r")
transactions = []
no_of_lines=0 
for line in f:
    split_line = line.strip().split(',')
    transactions.append(split_line[0:3])
    no_of_lines = no_of_lines + 1 
print(no_of_lines)
print (transactions)
#First iteration
C1 = count_first(transactions)
print (C1)
#F1 = find_frequent(C1,minsup,no_of_lines)
#print (F1)
#Second iteration
C2 = candidate_gen(C1.keys())
print ("=================")
print (C2)
C2 = add_frequency(C2,transactions)
print ("=================Add Frequency============")
print (C2)
#F2 = find_frequent(C2,minsup,no_of_lines)
#print(F2)
#Third iteration

C3 = candidate_gen3(C1.keys())
print (C3)
F3 = add_frequency3(C3,transactions)
print ("===============3=========")
print (F3)

c=get(F3)
print ("Final Call Check")
print (c)
