class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print("Your current balance is: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("Your current balance is: ", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Your current balance is: ", self.balance)
        else:
            print("Insufficient balance")

    def choice(self):
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")


atm = ATM(1000)
while True:
    atm.choice()
    option = int(input("Enter your choice: "))
    if option == 1:
        atm.check_balance()
    elif option == 2:
        amount = float(input("Enter amount to be Deposited: "))
        atm.deposit(amount)
    elif option == 3:
        amount = float(input("Enter amount to be Withdrawn: "))
        atm.withdraw(amount)
    elif option == 4:
        print("Thanks for using our ATM")
        break
    else:
        print("Invalid option")
