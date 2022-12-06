n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
o=input(f"write the operator add , sub ,div ,mul: ")


def solution(n1,n2,o):
    if o=="add":
        print(n1+n2)

    elif o=="sub":
        print(n1,n2)

    elif o=="div":
        print(n1/n2)

    elif o=="mul":
        print(n1*n2)

    else:
        print("invalid data")

solution(n1,n2,o)

# def add(n1,n2):
#     return n1+n2

# def sub(n1,n2):
#     return n1-n2

# def mul(n1,n2):
#     return n1*n2

# def div(n1,n2):
#     return n1/n2
