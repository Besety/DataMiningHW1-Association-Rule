import fp_growth
from apriori import Apriori
from collections import defaultdict
import re
import csv
import time


class Mingration(object):
	def __init__(self):
		pass


def Run_Apriori(dataset,minsup,minconf):
	ap = Apriori(dataset, minsup, minconf)
	# run algorithm
	ap.run()
	# print out frequent itemset
	ap.print_frequent_itemset()
	# print out rules
	ap.print_rule()

def Run_FP_Growth(input,minsup,minconf):
	fp_growth.FPGrowth(input, minsup, minconf)


'''

inputfile = "data.ntrans_0.1.tlen_40.nitems_0.5"

#IBM dataset convert to the format

IBM = open( inputfile+".txt",'r')
lines=IBM.readlines()
#print(lines)
L1 =[]
for line in lines:
	# print(line)
	T=line.split()[1]
	item=line.split()[2]
	L1.append([T,item])
	#print(T,item)
	
	pass
IBM.close()
#print(L1)

trans = defaultdict(list)
for key,value in L1:
	trans[key].append(value)

pass
#print (trans.items())

dataset = list(trans.values())
print(dataset)


f = open( inputfile+"DAT.txt",'w')
for itemset in dataset:
	for item in itemset:
		f.write(str(item)+',')
	f.write('\n')
f.close()

'''

#Migration dataset conver to the format

Mig =  open("Migdataset.txt",'r')
lines=Mig.readlines()
L2 =[]
for line in lines:
	T=line.split('\t')[0]
	item=line.split('\t')[1].strip()
	L2.append([T,item])
	pass
Mig.close()


trans = defaultdict(list)
for key,value in L2:
	trans[key].append(value)

pass
#print (trans.items())


dataset = list(trans.values())
#print(dataset)


f = open("MigDAT.txt",'w')
for itemset in dataset:
	for item in itemset:
		f.write(str(item)+',')
	f.write('\n')
f.close()




#DATASET1 IBM generator -FP_GROWTH ALGO
tStart = time.time()
print('\nFP_Growth algorithm')
Run_FP_Growth('MigDAT.txt',0.9,0.9)
tEnd = time.time()
print ("%f sec" % (tEnd - tStart))



#DATASET1 IBM generator -APRIORI ALGO
tStart = time.time()
print('\nApriori algorithm')
Run_Apriori(dataset,0.9,0.9)
tEnd = time.time()
print ("%f sec" % (tEnd - tStart))

