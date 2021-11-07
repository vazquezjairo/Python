class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        self.User = None
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    def display_account_info(self):
        print("Balance:",self.balance)
    def yield_interest(self):
        if BankAccount.can_yield(self.balance):
            self.balance += (self.balance * self.int_rate)
        else:
            pass
        return self
    def can_yield(balance):
        if balance < 0:
            return False
        else:
            return True


class User:
    def __init__(self, name):
        self.name = name 
        self.account = BankAccount(0.02,0)
    def make_deposit(self,amount):
        self.account.deposit(amount)
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    def display_user_balance(self,name,balance):
        print(f"User: {name}, Balance: {balance}")

account1 = BankAccount(.01,100)
account2 = BankAccount(.05,100)

guido = User("Guido")
jairo = User("Jairo")

account1.user = guido
account2.user = jairo

guido.make_deposit(100)
guido.make_deposit(50)
guido.make_deposit(200)
guido.make_withdrawal(100)

print(account1.user.account)