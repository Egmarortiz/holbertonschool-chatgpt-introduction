#!/usr/bin/python3
import sys

class Checkbook:
    """
    Description:
        A simple checkbook class to manage deposits, withdrawals, and balance.
    """
    def __init__(self):
        """
        Description:
            Initialize a new checkbook with zero balance.
        Parameters:
            None
        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Description:
            Add a positive amount to the balance.
        Parameters:
            amount (float): The amount to deposit; must be >= 0.0.
        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Description:
            Subtract a positive amount from the balance if funds allow.
        Parameters:
            amount (float): The amount to withdraw; must be >= 0.0.
        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Description:
            Print the current account balance.
        Parameters:
            None
        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Description:
        Command-line interface for the Checkbook class.
    Parameters:
        None
    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        if action not in ('deposit', 'withdraw', 'balance'):
            print("Invalid command. Please try again.")
            continue

        if action in ('deposit', 'withdraw'):
            # Prompt for amount until a valid non-negative float is entered
            while True:
                amt_str = input(
                    f"Enter the amount to {action}: $"
                ).strip()
                try:
                    amount = float(amt_str)
                    if amount < 0:
                        print("Amount must be non-negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")

            if action == 'deposit':
                cb.deposit(amount)
            else:
                cb.withdraw(amount)

        else:  # balance
            cb.get_balance()


if __name__ == "__main__":
    main()

