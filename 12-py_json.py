import json

#sample JSON
userJSON = '{"first_name":"Nicolette", "last_name":"Tesla", "age": 5}'

#Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Toyota', 'model': 'Soara', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)