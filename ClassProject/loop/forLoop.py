list=[12,75,150,180,145]

for i in list:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)