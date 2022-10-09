age1= int(input("Age of first person: "))
age2= int(input("Age of second person: "))
age3= int(input("Age of thirs person: "))

if (age1>age2 or age1==age2) and (age1>age3 or age1==age3):
    if age1==age3:
        print("Age of First and Third person are equal")
        print("First/Third person is oldest")
    elif age1==age2:
        print("Age of First and Second person are equal")
        print("First/Second person is oldest")
    else:
        print("First person is Oldest")
    
    if age2<age3:
        print("Second person is smallest")
    else:
        if age2==age3:
            print("Second and third person have same age")
        else:
            print("Third person is youngest")


elif ((age2>age1 or age2==age1) and (age2>age3 or age2==age3)):
    if age2==age1:
        print("First and Second person have same age")
        print("First/second person are oldest")
    elif age2==age3:
        print("Second person and Third person have same age")
        print("Second/Third person are oldest")
    else:
        print("Second person is oldest")
    if age1<age3:
        print("First person is Youngest")
    else:
        if age1==age3:
            print("First and Third person have same age")
        else:
            print("Third person is Youngest")


else:
    if age3==age1:
        print("First and Third person have same age")
        print("First/Third person is oldest")
    elif age3==age2:
        print("Third and Second person have same age")
        print("third/second person is oldest")
    else:
        print("third person is oldest")
    
    if age1<age2:
        print("First person is youngest")
    else:
        if age1==age2:
            print("First and Second person have same age")
        else:
            print("Second person is youngest")

