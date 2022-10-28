# email=input("Enter your email: ")
# x=email.split("@")

username=[]
domain=[]
n=(input("Enter email adress seperated by comma: ")).split(",")
print(n)
for i in n:
    x=i.split("@")
    username.append(x[0])
    domain.append(x[1])

print("Usernames ")
for i in range(len(username)):
    print(username[i],end="  ")

print("\nDOMAIN")
for i in range(len(domain)):
    print((domain[i]).upper(),end="  ")








