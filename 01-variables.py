#This is a single line comment

'''
This is a multiline comment
or docstring - used for defining a function's purpose
'''

"""
This is also a multiline comment
VARIABLE RULES
    - variable names are case sensitive eg, name is not equal NAME
    - must start with a letter or an underscore
    - can have numbers but can not start with one
"""

# x = 1           #int
# y = 2.5         #float
# name = 'John'   #str
# is_cool = False  #bool

#Multiple assignment
x, y, name, is_cool = (1,2.5,'John',True)

#Basic math
a = x + y

print(x,y,name,is_cool,a)
print(type(x))

#Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)