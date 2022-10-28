import random

#user inputs
lowerRange=int(input("Enter the lower range: "))
upperRange=int(input("Enter the upper range: "))
comp=random.randint(lowerRange,upperRange)



chance=2
score=30
while chance>0:
    user=int(input("Guess the number: "))
    if user>comp:
        print("Your guess was high -10 pinits, \"have one more try\"")
        chance-=1
        score-=10
    elif user<comp:
        print("Your guess was low -10 points,\"have one more chance\"")
        chance-=1
        score-=10
    elif user==comp:
        print("Congrat's","Your score is",score)
        break

user=int(input("Guess the number: "))
if user==comp:
    print("Congrat's","Your score is",score)
else:
    print("Better luck next time")