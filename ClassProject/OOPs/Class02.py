# class Laptop:
#     def config(self):
#         print("ASUS","i7","1TB")

# Laptop1=Laptop()
# Laptop1.config()

# class Person:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno



# person1=Person("Abhishek",19)
# person2=Person("Anurag",20)

# print(person1.name,id(person1),person1.rollno)
# print(person2.name,id(person2),person2.rollno)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def updateName(self):
#         self.name="manna"

#     def compareAge(self,other):
#         if self.age==other.age:
#             return True
#         else:
#             return False

# person1=Person("Abhishek singh",19)
# person2=Person("Anurag",19.8)

# if person1.compareAge(person2):
#     print("They are of same age")
# else:
#     print("They are of different age")








# class Car:
#     # static variable or class variable
#     wheels=4

#     def __init__(self,brand,mil) -> None:
#         self.brand=brand
#         self.mil=mil

# car1=Car("BMW",69)
# car2=Car("Ferrari",56)

# print(car1.brand,car1.mil,car1.wheels)
# print(car2.brand,car2.mil,car2.wheels)





class Student:
    n=2
    def __init__(self,marks1,marks2,marks3) -> None:
        self.web=marks1
        self.python=marks2
        self.math=marks3

    def avg(self):
        return (self.web+self.math+self.python)/3
    
    def get_math_marks(self):    
        return self.math                #Accessors
    
    def set_marks(self,marks):            #Mutators
        self.math=marks 
    
    @classmethod
    def classMethod(cls):
        return cls.n 

    @staticmethod
    def staticMethod():
        print("This is an static method")               

student1=Student(5,4,3)
student2=Student(7,8,9)
student3=Student(1,6,9)

#decorators are used to modify behaviour of a function 

print(student1.avg())
print(student2.avg())
print(student3.avg())

print(Student.classMethod())
Student.staticMethod()




