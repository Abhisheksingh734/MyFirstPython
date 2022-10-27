name=input("enter your name: ")
# print("first letter is",name[0],"last letter is",name[-1])

if len(name)%2==0:
    print("middle cahrc is: ",name[(len(name)+1)//2])
else:
    print("middle charc is: ",name[(len(name)//2)])

