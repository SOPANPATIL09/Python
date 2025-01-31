subject={}
print(type(subject))
x=int(input("Enter chemistry marks :"))

subject.update({"chemistry":x})

x=int(input("Enter physics marks :"))

subject.update({"physics":x})

x=int(input("Enter biology marks :"))

subject.update({"biology":x})

print(subject)
