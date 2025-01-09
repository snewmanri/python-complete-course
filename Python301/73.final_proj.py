class Bank:
    def __init__(self,initial_amount=0.00):
        self.balance = initial_amount
    
    def log_transaction(self,transaction_string):
        with open("transactions.txt","a") as file:
            file.write(f"{transaction_string} \t\tnew balance is {self.balance} \n")
    
    def withdraw(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"withdrew {amount}")
    
    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"deposited {amount}")

account = Bank(51.50)
while True:
    try:
        action = input("what kind of action to take?: ")
    except KeyboardInterrupt:
        print("\ngoodbye\n")
        break
    if action in {"withdrawal", "deposit"}:
        if action == "withdrawal":
            amount = input("how much to withdraw?: ")
            account.withdraw(amount)
        else:
            amount = input("how much to deposit?: ")
            account.deposit(amount)
    
        print("your balance is ", account.balance)
    else:
        print("invalid action, try again")