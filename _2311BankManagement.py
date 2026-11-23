# class Bank:
#     def __init__(self,name):
#         self.name = name
#         self.balance = 1000
#     def balanceAmount(self):
#         print(f"{self.name} has balance of {self.balance}")
#     def withdraw(self,amount):
#         if self.balance - amount <= 0:
#             print(f"{self.name} has no sufficient money left")
#         else:
#             self.balance -=amount
#             print(f"{self.name} withdraw an amount of {amount} from bank")
#             self.balanceAmount()
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"{self.name} Deposit an amount of {amount} to bank")
#         self.balanceAmount()

# print("Bank Management System")
# name = input("Enter name of customer: ")
# customer1 = Bank(name)
# while True:
#     choice = input("Enter an option \n1.WithDraw\n2.Deposit\n3.Balance\n4.Exit\n")
#     if choice == "1":
#         amount = int(input("Enter the amount to Withdraw: "))
#         customer1.withdraw(amount)
#     elif choice == "2":
#         amount = int(input("Enter the amount to Deposit: "))
#         customer1.deposit(amount)
#     elif choice == "3":
#         customer1.balanceAmount()
#     elif choice == "4":
#         break
#     else:
#         print("Wrong Choice Enter correct choice")
#         continue












class Bank:
    def __init__(self,name):
        self.name = name
        self.balance = 1000.0
    def balanceAmount(self):
        print(f"{self.name} has balance of {self.balance:.2f}")
    def withdraw(self,amount):
        if self.balance - amount <= 0:
            print(f"{self.name} has no sufficient money left")
        else:
            self.balance -=amount
            print(f"{self.name} withdraw an amount of {amount} from bank")
            self.balanceAmount()
    def deposit(self,amount):
        self.balance += amount
        print(f"{self.name} Deposit an amount of {amount} to bank")
        self.balanceAmount()

print("Bank Management System")
name = input("Enter name of customer: ")
customer1 = Bank(name)
while True:
    choice = input("Enter an option \n1.WithDraw\n2.Deposit\n3.Balance\n4.Exit\n")
    if choice == "1":
        amount = float(input("Enter the amount to Withdraw: "))
        customer1.withdraw(amount)
    elif choice == "2":
        amount = float(input("Enter the amount to Deposit: "))
        customer1.deposit(amount)
    elif choice == "3":
        customer1.balanceAmount()
    elif choice == "4":
        break
    else:
        print("Wrong Choice Enter correct choice")
        continue
