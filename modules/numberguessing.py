import random
x = random.randrange(1,101)
print(x)

y = int(input("enter a number: "))
if y>x:
    print("computer no: ", x)
    print("your no is greater")
elif y<x:
    print("computer no: ", x)
    print("your no is smaller")
else:
    print("computer no: ", x)
    print("your no is equal to computer no")
