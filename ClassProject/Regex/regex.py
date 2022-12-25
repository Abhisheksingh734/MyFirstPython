import random
import statistics
random_number = [random.uniform(0,1000) for i in range(1000)]

print(f"Minimum value of random numbers:{min(random_number)}")
print(f"Maximum value on random numbers:{max(random_number)}")
print(f"Mean of the random_numbers:{statistics.mean(random_number)}")
print(f"Median of the random_numbers:{statistics.median(random_number)}")
print(f"Standard deviation on mean:{statistics.pstdev(random_number)}")

bin = {'100':0,'200':0,'300':0,'400':0,'500':0,'600':0,'700':0,'800':0,'900':0,'1000':0}
for value in random_number:
    if value <= 100:
        bin['100']+=1
    elif value > 100 and value<=200:
        bin['200']+=1
    elif value > 200 and value<=300:
        bin['300']+=1
    elif value > 300 and value<=400:
        bin['400']+=1
    elif value > 400 and value<=500:
        bin['500']+=1
    elif value > 500 and value<=600:
        bin['600']+=1
    elif value > 600 and value<=700:
        bin['700']+=1
    elif value > 700 and value<=800:
        bin['800']+=1
    elif value > 800 and value<=900:
        bin['900']+=1
    elif value > 900 and value<=1000:
        bin['1000']+=1

print("Bin-range\tCount")
count=0
for key in bin:
    print(f"{int(key)-100}-{key}\t\t{bin[key]}")
    count+=bin[key]
print(f"Total\t\t{count}")