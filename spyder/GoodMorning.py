name=input("Enter Your Name : ")
print("Good Morning",name)

tablenumber = int(input("Enter The Number Do You Want to Table : "))
for i in range(1,11):
    print(f"{tablenumber} X {i} = {tablenumber*i}")

age = int(input("Enter Yout Age : "))
print("You Age Eligible for Watching Animal Movie ") if(age>=18) else print("You Can't Watch Any Movie ")