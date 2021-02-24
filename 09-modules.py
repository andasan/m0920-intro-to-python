#Core modules
import datetime
from datetime import date
import time
from time import time

#PIP
from camelcase import CamelCase

#Custom module
import validator
from validator import validate_email

today = date.today()
print(today)
timestamp = time()
print(timestamp)


#PIP modules <--- includes Django
c = CamelCase()
print(c.hump('hello there ami'))


#Custom modules
email = 'test$mail.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')
