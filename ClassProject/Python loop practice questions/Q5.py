# find factorial of a number using recursion 

n=int(input("Enter the number you want factorial of: "))
F=1
def fact(n):
    global F
    if n==1:
        return 1
    else:
        F*=n
        fact(n-1)
        return F

print(f"factorial of {n} is ",fact(n))