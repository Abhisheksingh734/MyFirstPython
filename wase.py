count={}
num=[34,56,32,45,43,76,85]

for i in num:
    if i not in count:
        count[i]=0
    count[i]+=1

from collections import defaultdict

counts=defaultdict(lambda: 0)
num=[34,56,32,45,43,76,85]

for i in num:
    counts[i]+=1

