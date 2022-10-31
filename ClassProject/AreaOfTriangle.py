a=int(input("enter length of side a: "))
b=int(input("enter length of side b: "))
c=int(input("enter the length of side c: "))

#finding area of triangle by herons formulae
S = (a+b+c)/2 # S = semiperimeter

Area = (S*(S-a)*(S-b)*(S-c))**0.5

print("Area of the triangle with sides",a,",",b,",",c,"is",Area)