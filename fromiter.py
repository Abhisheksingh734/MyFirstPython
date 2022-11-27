#useful for creating non numeric sequence type array howeveer it cn=an create any type of array

import numpy as np

a={3:"d",6:"m",7:"t"}

y=np.fromiter(a,dtype=np.int32)
print(y)


b="ilovepython"

x=np.fromiter(b,dtype="U2",count=4)
print(x)
print(x.dtype)

