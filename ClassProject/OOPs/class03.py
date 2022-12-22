# class A:
#     def method1(self):
#         print("This is method one")
# class B(A):     #----------------------This means----------------->>> B is a Child of A
#     def method2(self):
#         print("This is method two")
# class C(B):     #=======================This means ===============>>> C is child of B which is also child of A
#     def method3(self):
#         print("This is method three")

# obj1=A()
# obj2=B()
# obj3=C()

# obj1.method1()
# obj2.method2()


# ---------------------------------------------------------LOOP--------------------------------------------------------------

# class A:
#     def __init__(self):
#         print("This is init of A")
#     def method1(self):
#         print("This is method 1")
# class B(A):
#     def __init__(self):
#         super().__init__() #-------------------------------------This is used to get both init i.e parent and child both
#         print("THis is init of B")
#     # def __init__(self):   #--------------------only child init will work if both parent and child have init method
#     #     print("This is init of B")
#     def method2(self):
#         print("Thisis method 2")

# # obja=A()
# objb=B()


#==============================================================================================================================================>>


# class A:
#     def __init__(self):
#         print("This is init of method A")

#     def method1(self):
#         print("This is method 1")

# class B:
#     def __init__(self):
#         # super().__init__()
#         print("This is init of method B")

#     def method2(self):
#         print("This is method  2")

# class C(B,A):             #------------multiple inheritence
#     def __init__(self):
#         super().__init__()
#         print("This is init of method 3")

#     def method3(self):
#         print("This is method 3")

# objC = C()


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# rect = Rectangle(length=5, width=10)

# print(rect.area()) 



# class Rec:
#     def calculateArea(self,length,breath=None):
#         return length*breath
#     def calculateArea(self,length):
#         return length *length
# rec =Rec()

# print(rec.calculateArea(2))
# print(rec.calculateArea(2,3))



# class Birds:
#     def category(self):
#         print("This is a category of bird")
#     def fly(self):
#         print("I can fly")

# class Sparrow(Birds):
#     def size(self):
#         print("I am small in size")
#     pass
# class Crow(Birds):
#     pass
# class Ostrich(Birds):
#     def fly(self):
#         print("I cannot fly")
#     pass


# objbird=Birds()
# objSparrow=Sparrow()
# objCrow=Crow()
# objOstrich=Ostrich()

# objbird.category()
# objCrow.category()
# objSparrow.size()
# objOstrich.fly()
# objSparrow.fly()


# class Vehicle:
#     def seatingCap(self):
#         print("It has 4 seating capacity")


# class Car1(Vehicle):
#     pass

# class Car2(Vehicle):
#     pass

# class Bus(Vehicle):
#     def seatingCap(self):
#         print("It has 20 seating capacity")

# objcar1=Car1()
# objcar2=Car2()
# objbus=Bus()

# objcar1.seatingCap()
# objcar2.seatingCap()
# objbus.seatingCap()


# class Vehicle:
#     def __init__(self, seating_capacity):
#         self.seating_capacity = seating_capacity

#     def seatingCap(self):
#         print(f"It has {self.seating_capacity} seating capacity")

# class Car1(Vehicle):
#     pass

# class Car2(Vehicle):
#     pass

# class Bus(Vehicle):
#     pass

# objcar1 = Car1(4)
# objcar2 = Car2(4)
# objbus = Bus(20)

# objcar1.seatingCap()
# objcar2.seatingCap()
# objbus.seatingCap()





# class Person:
#     def __init__(self,name,age):
#         self.__name =name
#         self.__age= age

#     def getName(self):
#         return self.__name
#     def getAge(self):
#         return self.__age

# person1 =Person("Abhishek",19)
# print(person1.getName())
# print(person1.getAge())


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

person1 = Person("Abhishek", 19)
print(person1.getName())
print(person1.getAge())

person1.setName("John")
person1.setAge(20)
print(person1.getName())
print(person1.getAge())

person1._Person__name = "Abhi" #----------------how to change
print(person1._Person__name)