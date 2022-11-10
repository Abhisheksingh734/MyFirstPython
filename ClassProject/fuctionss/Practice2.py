# def fibo(num):
#     sum=sum +num
#     if num==0:
#         return sum
#     else:
#         sum=num+fibo(num-1)
#         return sum
# print(fibo(5))








# def sq(num):
    # return num**2

# x=lambda a: a*a
# num=x(5)

# y=lambda x,y: x+y
# sum=y(6,5)


# print(sum)

# print(num)






def name(x):
    return lambda a: a-x


num=name(10)
print(num(7))

