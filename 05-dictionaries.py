# A collection of unordered, changeable and indexed. No duplicate members

#Create a dict
person = {
    'first_name': 'Ayumi',
    'last_name': 'Yamanouchi',
    'age': 81
}
print(person)

# Use constructor
# person2 = dict(first_name='Ami', last_name='Tanaka')
# print(person2)

#Get value
print(person['first_name'])
print(person.get('last_name'))

#Get dict keys
print(person.keys())

#Get dict items
print(person.items())

#Copy dict
person2 = person.copy()
print('Person2: ',person2)
person2['city'] = 'Gumma'
print('Person2: ',person2)

#Remove item
del(person['age'])
print(person)
# person.pop('phone') #throws an error for non-existing key
# print(person)

#Clear
person.clear()
print(person)

#Get length
print(len(person2))
# print(person2)

#List of dict
people = [
    {'name': 'Dan', 'age':50},
    {'name': 'Nico', 'age':165}
]

print(people[1]['age'])

