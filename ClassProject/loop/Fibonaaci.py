num1=0
num2=1
sum=0
print(num1,end=" ")
print(num2,end=" ")

for i in range(0,10):
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum,end=" ")
