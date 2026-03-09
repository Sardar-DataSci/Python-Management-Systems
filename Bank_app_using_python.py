# Bank App using Python (OOP)

class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited Rs.{amount}")
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawn Rs.{amount}")
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: Rs.{self.balance}")

    def show_history(self):
        print("---------- Transaction History ----------")
        if not self.history:
            print("No transactions yet.")
        else:
            for t in self.history:
                print(t)


# ---------------- MAIN PROGRAM ----------------

print("             -----------------------------------")
print("                  Welcome To Python Bank App")
print("             -----------------------------------")

name = input("Enter name: ").strip()

while True:
    pin = input("Set 4-digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        pin = int(pin)
        break
    else:
        print("PIN must be exactly 4 digits.")

print("PIN set successfully.")

loginpin = int(input("Enter login PIN: "))
account = BankAccount(name, pin)

if loginpin != pin:
    print("Wrong PIN. Access denied.")
    exit()

while True:
    print("\n------------------------")
    print("        Main Menu")
    print("------------------------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show History")
    print("4. Show Balance")
    print("5. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        account.deposit(int(input("Enter amount: ")))

    elif choice == 2:
        account.withdrawal(int(input("Enter amount: ")))

    elif choice == 3:
        account.show_history()

    elif choice == 4:
        account.show_balance()

    elif choice == 5:
        print("Thank you for using Python Bank App 👋")
        break

    else:
        print("Invalid choice. Try again.")
