a=5

print(a,type(a))

b=5.8
print(b,  type(b))

c=a+b+5j
print(c, type(c))


#type conversions
x=float(a)
print(x, type(x))

y=int(b)
print(y,type(y))

z=complex(b)
print(z,type(z))

##Random Number

import random
print(random.randrange(1,10))