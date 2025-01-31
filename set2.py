"""
 figure out a way to store 9 and 9.0 as a separate value in set 
"""
"""two ways to store this type of value in a set
1) value={9,"9.0"}
2)value={("int",9),("float",9.0)}
"""

value1={9,"9.0"}
value2={("int",9),("float",9.0)}

print(value1)
print(value2)
