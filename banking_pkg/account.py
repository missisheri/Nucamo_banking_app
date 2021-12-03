
def show_balance(balance):
    print("Current Balance: $" + str(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    balance = balance + float(amount)
    return balance


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    balance = balance - float(amount)
    return balance


def logout(name):
    print("Goodbye", name + "!")


def check_name(name):
    while True:
        if len(name) in range(1, 11):
            break
        elif len(name) < 1:
            print("You must enter a name")
            name = input("Enter name to register: ")
        elif len(name) > 10:
            print("The maximum name length is 10 characters")
            name = input("Enter name to register: ")
    return name
