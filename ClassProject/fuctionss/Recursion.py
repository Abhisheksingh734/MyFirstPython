
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print(f"Factorial of {n} is",factorial(n))
