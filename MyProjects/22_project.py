names=["sd","dsf","sdf"]
marks=[23,45,67]
updates=[0,1,2]

x=[[j for j in range(3)] for i in range(3)]
for i in range(3):
    x[0][i]=names[i]
    x[1][i]=marks[i]+updates[i]
    x[2]=i+1
print(x)