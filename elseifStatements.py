from pickletools import markobject


MarksObtained = int(input("Enter your marks out of 100: "))

if MarksObtained >90 and MarksObtained<=100:
    print("Your Grade is A")
elif MarksObtained > 100:
    print("Enter your marks out of 100")
elif MarksObtained <= 90 and MarksObtained > 80:
    print("Your Grade is B")
elif MarksObtained <=80 and MarksObtained> 70:
    print("Your grade is C")
else:
    print("Your grade is D")