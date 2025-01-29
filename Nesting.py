#Nesting in python
age=int(input("Enter your age :"))

if(age>=18):
    if(age>=80):
        print("you cannot drive")
    else:
        print("you can drive")
else:
    print("you cannot drive ")
