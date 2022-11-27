import numpy as np

x=np.arange(2,8,1,dtype=np.float32)
print(x)

y=np.linspace(1,2,2)  #3rd parameter gives how many parts you want to divide it into
print(y)

z=np.linspace(2,10,3,dtype=np.int32)
print(z)

u=np.arange(6)
u=u.reshape(2,3)
print(u)