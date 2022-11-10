n=int(input())
num1=0
num2=1
def fibo(n):
    global num1
    global num2
    global temps
    if num2==n:
        print(num2)
        fibo(n-1)
    else:
        temps=num2
        num1=num2
        num2=temps+num1
        print(num2)
fibo(n)





