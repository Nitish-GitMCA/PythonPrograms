for a in range(1,11):
    print(5*a)

print()

for n in range(1,11):
    print("15 *",n,"=", 15*n)



for n in range(10,-1,-2):
    print(n)

fruits = ["apple", "banana","cherry"]
for x in fruits:
    print(x)

for x in "banana":
  print(x)


#break with banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#break without banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#continue : do not print banana
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
