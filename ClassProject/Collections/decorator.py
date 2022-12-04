def div(a,b):
    return a//b

def new_div(func):
    def innerfunc(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return innerfunc

div=new_div(div)
print(div(4,2))

