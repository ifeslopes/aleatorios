import random

a=[31,33,34,36]
d=[42,41,43,44]
c=random.randrange(31,37)
b=random.randrange(1,5)
print(c, b)
print("\033[%d;%dmCOR\033[m"%(c,b))