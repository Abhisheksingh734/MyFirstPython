list=[12,75,150,180,145]

size=len(list)

revList=[]
for i in range(size-1,-1,-1):
    revList.append(list[i])
print(revList)