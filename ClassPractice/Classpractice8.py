#take user input string
#if len of input > 3char add ing

string=input("enter the word: ")
if len(string)>3:
    print(string+"ing")
else:
    print(string)
