
# # function that filters vowels
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
  
  
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# filtered = filter(fun, sequence)
  
# print('The filtered letters are:')
# for s in filtered:
#     print(s)
# print(list(filtered))


# x= lambda a: a%2

# list1=[3,2,8,16,11,34,17]
# def fun(num):
#     if num%2==0:
#         return num
#     else:
#         return num
# even=list(filter(lambda a:a>15,list1))
# print(even)

# even1=list(map(lambda i:i**(2),list1))
# print(even1)



# list2=[2,3,4,2,4]

import functools

# print(functools.reduce(lambda a,b:a+b,list2))

list1=[10,20,30,40,50]
print(list(map(lambda a:a*3,list1)))

list2=[34,88,30,22,10,15,18]
print(list(filter(lambda a:a%5==0,list2)))



