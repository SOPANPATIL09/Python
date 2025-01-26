#conditional statement
#if_elif_else(syntax)

age =int( input("enter a age :"))

if(age >=18):
    print("can vote and apply for license")

elif(age>13 & 13<18):
    print("minor")
    
else:
    print("child")
    
