#Create class

class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
        self._private = 1000

    def printMe(self):
        return f'{self.name}'
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def print_encap(self):
        print(self._private)

#extend class
class Customer(User):
    #constructor
    def __init__(self, name, email, age):
        User.__init__(self, name, email, age)
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    def set_balance(self, balance):
        self.balance = balance

koji = User('Koji Okajima', 'koji@okajima', 24)
print(koji.printMe())
print(koji.greeting())

koji.print_encap()
koji._private = 800
koji.print_encap()

ayumi = Customer('Ayumi Tanaka', 'ayumi@tanaka', 3)
ayumi.set_balance(500)
print(ayumi.greeting())
