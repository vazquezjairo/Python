class User:
    def __init__(self, name):
        self.name = name 
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self,name = "Guido",amount = 250):
        print(f"User: {name}, Balance: {amount}")
        return self

guido = User("Guido")
monty = User("Monty")
jairo = User("Jairo")

guido.make_deposit(100).make_deposit(50).make_deposit(200).make_withdrawal(100)

guido.display_user_balance()

monty.make_deposit(50).make_deposit(25).make_withdrawal(200).make_withdrawal(500)

monty.display_user_balance(monty.name,monty.account_balance)

jairo.make_deposit(1000).make_withdrawal(10).make_withdrawal(20).make_withdrawal(50)

jairo.display_user_balance(jairo.name,jairo.account_balance)