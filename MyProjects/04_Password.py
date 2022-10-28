import random

#should include
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
lower="qwertyuiopasdfghjklzxcvbnm"
special="@#?!%&*"
num="1234567890"

#All case
sample=upper+lower+special+num

#user input
lenpswd=int(input("Enter password length: "))





pswd=""
count=1

upperlist=""
lowerlist=""
speciallist=""
numlist=""


while count<=lenpswd: #lenpswd is user input 
    n=random.randrange(len(sample))
    pswd+=sample[n]    #appending the random charchters in pswd
    count+=1


#calculating number of different types of charchters

for i in pswd:
    if i in upper:
        upperlist+=i
    elif i in lower:
        lowerlist+=i
    elif i in special:
        speciallist+=i
    elif i in num:
        numlist+=i

# checking pswd strenght

if len(pswd)<12:
    print("This password is short",pswd)

elif len(upperlist)==0:
    print("Your password should contain an Uppercase letter,",pswd)
elif len(lowerlist)==0:
    print("Your password should contain a lowercase letter,",pswd)
elif len(speciallist)==0:
    print("Your password should contain a special charachter,",pswd)
elif len(numlist)==0:
    print("Your password should contain a number,",pswd)
else:
    print("pswd set",pswd)