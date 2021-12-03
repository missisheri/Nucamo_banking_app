from banking_pkg.account import logout, show_balance, deposit, withdraw, check_name


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


balance = 0
print("\t=== Automated Teller Machine ===")
name = input("Enter name to register: ")

while True:
    if len(name) in range(1, 11):
        break
    elif len(name) < 1:
        print("You must enter a name")
        name = input("Enter name to register: ")
    elif len(name) > 10:
        print("The maximum name length is 10 characters")
        name = input("Enter name to register: ")

pin = input("Enter PIN: ")
print(name, "has been registered with a starting balance of $0")

while True:
    print("\n\t=== Automated Teller Machine ===")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid Credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)  #why do we need an assignment here? Isn't running deposit(balance) enough?
        show_balance(balance)
    elif option == "3":
        balance = withdraw(balance)
        show_balance(balance)
    elif option == "4":
        logout(name)
        break
