# def detail(name,age):
#     print(name)
#     print(age)
# detail("Abhishek",19)




# def name(firstName="Abhishek"):
#     print("My name is " , firstName)
# name()




# def num(*args):
#     for i in args:
#         print(i)

# num(3,4,5,6,7)



# def Employee(name,salary=10000):
#     print(f"Name of employee is {name} and his salary is {salary}")

# Employee("Ben",9000)
# Employee("mike",15000)
# Employee("Bob")




# def student(name,**data):
#     print(name)
#     for i,j in data.items():

#         print(i,j)

# student("abhishek",age=19,place="jalandhar",Pno="425342342")



# a=5
# def example():
#     global a  #--->   #to access the global variable
#     a=10
#     print(a)

# print(a)
# example()






# list=[32,21,64,100,13]
# Odd=0
# Even=0

# def OddEven(list):
#     global Odd
#     global Even
#     for i in list:
#         if i%2==0:
#             Odd+=1
#         else:
#             Even+=1

#     return Odd,Even

# Odd,Even=OddEven(list)
# print(Odd)
# print("Number of Odds are: ",OddEven(list)[0],"\n"+"Number of evens are: ",OddEven(list)[1])






names=["Atul","Shubham","Anurag","Rahul","Dev","Roy"]
def MoreThanFive(list):
    count=0
    new=[]
    for i in list:
        if len(i)>5:
            new.append(i)
            count+=1
    return count,new

count,new=MoreThanFive(names)

print(count)
for i in new:
    print(i)

