#:simple calculator.

print('''+ ADD
- SUBSTRACT
* MULTIPLY
/ DIVIDE''')

num1= int(input("enter the value 1:"))
num2= int(input("enter the value 2:"))
opr = input("enter the operator:")
if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid value") 


