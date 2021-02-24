name = 'Koji'
age = 37

#Concatenate
# print('Hello, my name is ' + name + ' and I am ' + age)
print('Hello, my name is ' + name + ' and I am ' + str(age))

#String formatting
#---Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#---F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

#String methods
s = 'hello world'
s2 = 'HELLO WORLD'
s3 = 'HELLO world'
s4 = 'helloworld'

#Capitalize string
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lower
print(s2.lower())

#Swap case
print(s3.swapcase())

#Get length
print(len(s))

#Replace
print(s.replace('world', 'kitty'))

#Count
sub = 'o'
print(s.count(sub))

#Starts with
print(s.startswith('henlo'))

#Ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find positon
print(s.find('o'))

#is all alphanumeric
print(s4.isalnum())

#is all alphabetic
print(s4.isalpha())

#is all numeric
print(s4.isnumeric())