import random

part1=["The mouse ran over the lion’s back "]
part2=["The little mouse heard the lion roar"]
part3=["The hunters tied the lion to a tree"]
part4=["One week later, hunters caught the lion."]
part5=["The mouse saved the lion"]
part6=["Little friends can be great friends."]
part7=["The lion let the mouse go."]

a=random.randint(1,7)

count=0
while count<7:
    a=random.randint(1,7)
    if a==1:
        print(part1)
        count=+1
    elif a==2:
        print(part2)
        count=+1
    elif a==3:
        print(part3)
        count=+1
    elif a==4:
        print(part4)
        count=+1
    elif a==5:
        print(part5)
        count=+1
    elif a==6:
        print(part6)
        count=+1
    elif a==7:
        print(part7)
        count=+1

#INCOMPLETE 
