class User:
    def __init__(self, name):
        self.name = name 
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self,name,amount):
        print(f"User: {name}, Balance: {amount}")

guido = User("Guido")
monty = User("Monty")
jairo = User("Jairo")

guido.make_deposit(100)
guido.make_deposit(50)
guido.make_deposit(200)
guido.make_withdrawal(100)

guido.display_user_balance(guido.name,guido.account_balance)

monty.make_deposit(50)
monty.make_deposit(25)
monty.make_withdrawal(200)
monty.make_withdrawal(500)

monty.display_user_balance(monty.name,monty.account_balance)

jairo.make_deposit(1000)
jairo.make_withdrawal(10)
jairo.make_withdrawal(20)
jairo.make_withdrawal(50)

jairo.display_user_balance(jairo.name,jairo.account_balance)