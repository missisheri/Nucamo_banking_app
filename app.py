from banking_pkg.account import logout, show_balance, deposit, withdraw, validate_name


def atm_menu(name: str) -> None:
    """Display the ATM menu."""

    print("\n\t=== Automated Teller Machine ===")
    print(f"User: {name}")
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

def main():
    print("\t=== Automated Teller Machine ===")
    name = input("Enter name to register: ")
    name = validate_name(name)

    pin = input("Enter PIN: ")
    print(f"{name} has been registered with a starting balance of $0")

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

    balance = 0

    while True:
        atm_menu(name)
        option = input("Choose an option: ")
        if option == "1":
            show_balance(balance)
        elif option == "2":
            balance = deposit(balance)
            show_balance(balance)
        elif option == "3":
            balance = withdraw(balance)
            show_balance(balance)
        elif option == "4":
            logout(name)
            break

if __name__ == "__main__":
    main()
