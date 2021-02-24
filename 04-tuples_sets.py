#A collection of ordered and unchangeable values. Allows duplicate members

#TUPLE
#Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
print(fruits)

#Using a construtor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
print(fruits2)

#Get a value
print(fruits[1])

#Can't change value
# fruits[0] = 'Pears'
# print(fruits)

#Delete tuple
del fruits2
# print(fruits2)

#Get length
print(len(fruits))

#SET - unordered and unindexed. No duplicate members

#Create set
fruits_set = {'Apples', 'Oranges', 'Bananas'}
print(fruits_set)

#Check if in set
print('Eggs' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

# Add duplicate
fruits_set.add('Apples')
print(fruits_set)

#Clear set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set

print(fruits_set)