l=[1,2,3,[4,5,6]]
print(l[1:3])

#list iteration
l=[10,20,30,40,50]
t = len(l)
print(t)
for x in range(t):
    print(l[x])

print()
l=[10,20,30,40,50]
for a in l:
    print(a)


#delete or remove
l=[10,20,30,40,50]
#del l[2]
#print(l.pop(3))
#l.remove(50)
l.clear()
print(l)

#to update element from list:

l = [10,20,30,40,50]

l.insert(6,100)
print(l)


#count

l=[10,20,10,30,10,50]

#a = l.count(10)
m=max(l)
print(m)