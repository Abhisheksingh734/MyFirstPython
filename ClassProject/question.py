str="abcbcb"
print(str.count("bcb"))

for i in range(len(str)):
    for j in range(i+1):
        print(str[i],end=" ")
    print("\n")