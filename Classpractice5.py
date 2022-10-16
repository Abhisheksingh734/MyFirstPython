side1=int(input("side1: "))
side2=int(input("side2: "))
side3=int(input("side3: "))

if (side1+side2)>side3 and (side2+side3)>side1 and (side3+side1)>side2:
    print("the triangle is possible")
else:
    print("triangle is not possible")
