x = 21
y = 20
z = 5

#Comparison operator (==, !=, >, <, >=, <=)

#Simple if
if x > y:
    print(f'{x} is greater than {y}')

#if/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

#elif
if x > y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

#nested if
if z > 2:
    if z <= 10:
        print(f'{z} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not)
#and

if z > 2 and z <= 10:
    print(f'{z} is greater than 2 and less than or equal to 10')

#or
if z > 2 or y <= 10:
    print(f'{z} is greater than 2 or less than or equal to 10')

#not
if not(x==y):
    print(f'{x} is not equal to {y}')

#membership operators (not, not in)

numbers = [1,2,3,4,5]

#in
if x in numbers:
    print('IN: ', x in numbers)

#not in
if x not in numbers:
    print('NOT IN: ', x not in numbers)

#identity operators (is, is not)

#is
if x is y:
    print('IS: ', x is y)

#is not
if x is not y:
    print('IS NOT: ', x is not y)