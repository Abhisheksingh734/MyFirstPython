#Rock papers and Scissors
import random


yourscore=0
CPUscore=0
TotalMatch=1

while TotalMatch<6:
    
# users choice
    User= (input("Choose rock paper or scissors? ")).lower()

#CPU choice
    CPU=random.randint(1,3)
    if CPU==1:
        CPU="rock"
    elif CPU==2:
        CPU="paper"
    elif CPU==3:
        CPU="scissors"

    print("CPU choose :",CPU)

#deciding winner
    if User==CPU:
        print("Tie")
        yourscore+=1
        CPUscore+=1

    elif User=="rock":
        if CPU=="paper":
            print("You lose...paper covers Rock")
            CPUscore+=1
        elif CPU =="scissors":
            print("You Win! Rock smashes Scissors")
            yourscore+=1
    elif User=="paper":
        if CPU=="scissors":
            print("You lose...Scissors cuts paper")
            CPUscore+=1
        elif CPU =="rock":
            print("You Win! paper covers Rock")
            yourscore+=1
    elif User=="scissors":
        if CPU=="rock":
            print("You lose...rock smashes scissors")
            CPUscore+=1
        elif CPU =="paper":
            print("You Win! Scissors cuts paper")
            yourscore+=1
    else:
        print("Wrong value entered")
        break
    


    print(f"Final Scores: CPU: {CPUscore} User: {yourscore}")
    print(f"Matches left {5-TotalMatch}")

    TotalMatch+=1

if CPUscore>yourscore:
    print("You loose the match \n Better luck next time")
elif yourscore>CPUscore:
    print("You won!\n You are the MASTER of rock paper and scissors game ")
else:
    print("The match was a tie")



    
    




