#Create a function
def sayHello(name='Acchan'):
    print(f'Hello {name}')

sayHello('Johnny')
sayHello()

#Return values
def getSum(num1,num2):
    total = num1 + num2
    return total

print(getSum(5,4))

#lambda function - a small anonymouse function
#JS: getSum = (num1, num2) => num1 + num2
getSum = lambda num1, num2: num1 + num2
print('Lambda: ', getSum(10,5))