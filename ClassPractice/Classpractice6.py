# import random

# num1=random.randint(1,50)
# num2=random.randint(1,50)

# print("numbers are",num1,num2)
# print("their sum",num1+num2)
# print("their subtraction",num1-num2)
# print("their division",num1/num2)
# print("their multiplication",num1*num2)

num1=int(input())
num2=int(input())
operator=input("enter operator: ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
else:
    print("operator not found")