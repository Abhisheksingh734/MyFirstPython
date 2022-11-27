import numpy as np

l=[3,4,5,6,7]
m=[4,5,6,7,7]
print(l)
print(m)
a=np.array([l,m])
print(a)

# shape of the matrix
print(a.shape)

# data type stored 
print(a.dtype)

# size of each element stored
print(a.itemsize)

#cant change size of an array


#adding in every element
a=a+1
print(a)

