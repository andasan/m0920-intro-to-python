#A list is a collection of ordered and changeable values. Allows duplicate members

#Create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Pears']

#Use a constructor
# numbers2 = list((1,2,3,4,5))
# print(numbers2)

print(numbers)

#Get a value
print(fruits[1])

#Get the last value
print(fruits[-1])

#Length
print(len(fruits))

#Append to list
fruits.append('Kiwis')
print(fruits)

#Remove from list
fruits.remove('Grapes')
print(fruits)

#Insert into positon
fruits.insert(2, 'Strawberries')
print(fruits)

#Change the value
fruits[0] = 'Blueberries'
print(fruits)

#Remove with pop
x = fruits.pop(2)
print(x)
print(fruits)

#Reverse sort
fruits.reverse()
print(fruits)

#Sort list
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)