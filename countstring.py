
# def count_substring(string, sub_string):
#     a=string.count(sub_string)
#     return a 





string = input().strip()
sub_string = input().strip()
    
# count = count_substring(string, sub_string)
# print(count)

for i in range(0, len(string)):
    for j in range(i+1):
        print(string[j],end=",")