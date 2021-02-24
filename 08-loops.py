people = ['Ami', 'Inae', 'Kideok', 'Marina']

#Simple loop
# for person in people:
    # print(f'Current person: {person}')

#Break
'''
for person in people:
    if person == 'Kideok':
        break
    print(f'Current person: {person}')
'''

#Continue
'''
for person in people:
    if person == 'Inae':
        continue
'''

#Range
for i in range(len(people)):
    print(people[i])

for i in range(0,11):
    print(f'Numbers: {i}')

#While loops

count = 0
while count < 10:
    print(f'Count: {count}')
    count+=1