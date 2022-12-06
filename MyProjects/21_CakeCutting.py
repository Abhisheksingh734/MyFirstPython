#CUt the cake into N equal parts


N=int(input("Number of cuts: "))

horizontal_cuts=N//2
vertical_cuts=(N- horizontal_cuts)

number_of_equal_parts=(horizontal_cuts+1)*(vertical_cuts+1)

print(number_of_equal_parts)
