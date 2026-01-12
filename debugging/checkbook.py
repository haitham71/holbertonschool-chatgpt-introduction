class Checkbook:
    def __init__(self):
        """
        Function Description:
            Initializes a new Checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds the given amount to the checkbook balance.

        Parameters:
            amount (float): The amount of money to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Subtracts the given amount from the balance if sufficient funds exist.

        Parameters:
            amount (float): The amount of money to withdraw.

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
        Function Description:
            Displays the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
