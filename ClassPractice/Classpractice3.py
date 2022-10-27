totalLectures = 125
attendedLectures = int(input("How many lectures you have attended:"))

attendancePercentage= (attendedLectures/totalLectures)*100
print("Your attendance percentage is: ",attendancePercentage,"%")

if attendancePercentage < 75:
    print("You are not eligible for examinations")
else:
    print("You are eligible for your examinations")
