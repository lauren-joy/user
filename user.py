class User:
    def __init__ (self, name, email):
        self.name= name
        self.email= email
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

lauren = User("Lauren", "lau3@.com")
sarah = User ("Sarah", "sa87@g.com")
claire = User("Claire", "claire90@.com")

lauren.make_deposit(20)
lauren.make_deposit(40)
lauren.make_deposit(60)
lauren.make_withdrawal(5)
lauren.display_user_balance()

sarah.make_deposit(10)
sarah.make_deposit(60)
sarah.make_withdrawal(5)
sarah.make_withdrawal(15)
sarah.display_user_balance()

claire.make_deposit(2000)
claire.make_withdrawal(150)
claire.make_withdrawal(25)
claire.make_withdrawal(66)
claire.display_user_balance()

