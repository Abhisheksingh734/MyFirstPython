#time spent in company                       Bonus
#  less than 10 years                        10%
#greater than 6 lessthan equal to 10         8%
#less than 6                                  5%

salary= int(input("enter your salary: "))
time= int(input("Time spent: "))

if time<6 and time>0:
    print("your bonus is",salary+salary*0.05)
elif time>=6 and time<=10:
    print("your bonus is",salary+(salary)*0.08)
elif time<0:
    print("invalid data")
else:
    print("your bonus is",salary+salary*0.1)


