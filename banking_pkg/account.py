
def show_balance(balance: float) -> None:
    """Display the current account balance."""
    print("Current Balance: $" + str(balance))


def deposit(balance: float) -> float:
    """Update account balance after the deposit."""
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    return balance


def withdraw(balance: float) -> float:
    """Update account balance after the withdrawal."""
    amount = float(input("Enter amount to withdraw: "))
    balance -= amount
    return balance


def logout(name: str) -> None:
    """Logout from the ATM."""
    print("Goodbye", name + "!")


def validate_name(name: str) -> str:
    """
    Validate the user's name.

    Args:
        name (str): The user's name.

    Returns:
        str: The validated user name.
    """
    while True:
        if 1 <= len(name) <= 10:
            return name
        elif len(name) < 1:
            print("You must enter a name")
        elif len(name) > 10:
            print("The maximum name length is 10 characters")
        name = input("Enter name to register: ")
