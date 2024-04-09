s='hello'
r= "hello"
print(s)
print(r, type(r))

print("hello")
print('hello')

#multiline Strings

a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

a= "Hello, World"
print(a[6])

#looping through a string
for x in "banana":
    print(x)

#elength of a string
a="Hello, World!"
print(len(a))

#check string
txt="i am nitish kumar vishwakarma, a student a dhsgsu"
print("veer" not in txt)

#use it in an if statement
txt="the best thing in life are free!"
if "free" in txt:
    print("yes, 'free' is present.")



