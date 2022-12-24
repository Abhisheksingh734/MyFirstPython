# ------------------------------------CLASS NOTES----------------------------------------

# f = open("demo.txt","r")
# # print(f.read())
# # print(f.readline())
# # print(f.readline())

# f1 = open("demo1.txt", "w")
# f1.write("This is a new file\n")
# f1.write("This is a random text\n")

# for i in f:
#     f1.write(i)


# try:
#     f = open("demo.txt")
    #your code goes here
# finally:
#     f.close()
#This way we are making sure that file is closed properly even if exception is raised that cause the program flow to stop


# with open("demo.txt") as f:
#     f.read() #--> example
#     #your code goes here

# f = open("demo.txt", "r")
# print(f.read(10))
# print(f.tell())



# f = open("img.png", "rb")

# f1 = open("img_copy.png", "wb")

# # print(f.read())

# for i in f:
#     f1.write(i)


# import os

# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("File does not exist")

# ----------------------------------------------------CLass over-----------------------------------------

# with open("ClassProject\File Handling\class01.txt","r") as f:
#     data=f.read()
#     # data=f.readline()
# print(data)


# f=open("ClassProject\File Handling\class01.txt","r")
# # data=f.read()
# # print(data)


# f1=open("ClassProject\File Handling\Myself.txt","w")
# f1.write("wassup guys \nwelcome to my blog \ni am very excitied to share my day ")
# for  i in f:
#     f1.write(i)
# f1.close()

# data=f.read()
# print(data)

# with open("demo.txt") as f:
#     data=f.read()

# ---------------------------Try except -----------------------------------------------
# try:
#     with open("ClassProject\File Handling\Myself.txt") as f:
#         data=f.read(10)
#         print(data)
# except FileNotFoundError:
#     print("This is error")


with open("ClassProject\File Handling\img.jpg","rb") as f:
    with open("ClassProject\File Handling\imgcopy2.jpg","wb") as f1:
        for i in f:
            f1.write(i)


# for i in data:
#     with open("ClassProject\File Handling\img2.jpg","w") as f1:
#         f1.write(i)

# f=open("ClassProject\File Handling\img.jpg","rb")
# data=f.read()

# f1=open("ClassProject\File Handling\imgCopy2.jpg","wb")

# # for i in data:
# #     f1.write(i)
# import os

# # try:
# #     os.remove("ClassProject\File Handling\imgcopy2.jpg")
# # except FileNotFoundError:
# #     print("File not found")
# if os.path.exists("imgcopy2.jpg"):
#     os.remove("imgcopy2.jpg")
# else:
#     print("File do not exist")


# ------------------------------------------------EXCEPTION HANDLING----------------------------------------------------------

# try:
    #will run the code and throws the error
# except:
    #this will raise the error
# else:
    #this will execute if there are no errors
# finally:
    # this will execute regradless the result of try and except
# try:
#     print(2/5)
# except ZeroDivisionError:   
#     print("bhai ye error ayega tabhi chalunga")
# else:                # run only if no error raised
#     print("bhai jab error nhi hoga tab hi chalunga")
# finally:                     #run in both case either error or run
#     print("jo bhi ho mai toh chal rha bhai ")


# ------------------------------------------------Raising Errors--------------------------------------------
a=2
if a<3:
    raise Exception("Vales is less thtan 3")


