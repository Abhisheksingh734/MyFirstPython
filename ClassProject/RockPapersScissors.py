import random

user=input("choose rock, paper or scissors: ")

comp=random.randint(1,3)
if comp==1:
    comp="rock"
elif comp==2:
    comp="paper"
elif comp==3:
    comp="scissors"


print("computer choose :",comp)


if comp==user:
    print("The match was a tie")
elif comp=="rock":
    if user=="paper":
        print("You Win! paper covers rock")
    elif user=="scissors":
        print("You lose.. Rock smashes scissors")
    else:
        print("you entered wrong data Choose from rock paper and scissors")
elif comp=="paper":
    if user=="scissors":
        print("You Win! scissors cuts paper")
    elif user=="rock":
        print("You lose.. paper cover rocks")
    else:
        print("you entered wrong data Choose from rock paper and scissors")
elif comp=="scissors":
    if user=="paper":
        print("You lose.. scissors cuts paper")
    elif user=="rock":
        print("You win! rock smashes scissors")
    else:
        print("You entered wrong data Choose from rock paper and scissors")

        