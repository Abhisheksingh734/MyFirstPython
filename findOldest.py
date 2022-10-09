age1= int(input("Age of first person: "))
age2= int(input("Age of second person: "))
age3= int(input("Age of thirs person: "))


if age1>age2 and age1>age3:
    print("First person is Oldeset")
    if age2>age3:
        print("Third person is Youngest")
    elif age3>age2:
        print("Second is youngest")
    else:
        print("SEcond and Third person have same age")
elif age2>age3 and age2>age1 :
    print("Second person is oldest")
    if age3>age1:
        print("First person is youngest")
    elif age1>age3:
        print("Third person is youngest")
    else:
        print("Third and first person have same age")
elif age3>age2 and age3>age1:
    print("Third person is oldest")
    if age2>age1:
        print("First person is youngest")
    elif age1>age2:
        print("Second person is youngest")
    else:
        print("First and second person have same age")
elif age1<age2:
    print("First person is youngest")
    print("Second and Third person have same age")
elif age2<age1:
    print("Second person person is youngest")
    print("First and Third person have same age")
elif age3<age2:
    print("Third person is youngest")
    print("Second and First person have same age")
else:
    print("Everyone have same age")





# Incomplte 