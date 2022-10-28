import random


score =0
while True:
    #user input
    
    user=input("Guess the number : ")
    #comp choice 
    comp=random.randint(1,6)

    #deciding winner
    if user=="exit" or user=="":
        break
    elif user==comp:
        print(f"Rolling Dice...-> {comp}")
        print("You guessed right!!")
        score+=1
        print(f"Your score is : {score}")
    elif user!=comp:
        print(f"Rolling Dice...-> {comp}")
        print("You lose...")
        print(f"Your score is: {score} ")
