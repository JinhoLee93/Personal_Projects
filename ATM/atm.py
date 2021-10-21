import sys

# ATM Framework
class ATM:
    def checkPin(self, card, pin):
        if card.pin == pin:

            return True

        return False

    def checkBalance(self, card):

        return card.balance

    def deposit(self, card, amount):
        bal = int(card.balance)
        bal += int(amount)
        card.balance = bal

    def withdtraw(self, card, amount):
        bal = int(card.balance)

        if int(amount) > bal:
            print("Not enough balance")

        else:
            bal -= int(amount)

        card.balance = bal

# Card
class Card:
    def __init__(self, pin=None, balance=0):
        self.pin = pin
        self.balance = int(balance)

def main():
    card = Card()
    print("Let's set up your card first.")
    # Set up PIN Number
    while True:
        pin = input("Choose your 4-digit PIN Number or enter Q to end: ")
        if pin == 'Q':
            print("Goodbye.")
            sys.exit()

        if not pin.isdigit() or len(pin) < 4 or len(pin) > 4:
            print("Your PIN Number is invalid")
            continue

        print("Your PIN Number is: ", pin)
        card.pin = pin
        break

    # Set up balance
    while True:
        balance = input("How much money would you like to have? (it will be rounded down to an integer)" +
                        "or enter Q to end: ")
        if balance == 'Q':
            print("Goodbye.")
            sys.exit()

        if not balance.isdigit():
            print("Your balance is invalid")
            continue

        print("Your balance is: ", balance)
        card.balance = balance
        break

    # PIN check
    atm = ATM()
    while True:
        entered = input("Enter your PIN Number to use the ATM " +
                        "Or enter Q to end: ")
        if entered == 'Q':
            print("Goodbye.")
            sys.exit()

        elif atm.checkPin(card, entered):
            break

        else:
            print("Wrong pin number")

    # Main menu
    while True:
        key = input("If you'd like to check balance, deposit, or withdraw, enter, C, D, or W " +
                    "or enter Q to end: ")

        if key == 'Q':
            print("Goodbye.")
            sys.exit()

        # Check balance
        elif key == 'C':
            print("Your current balance is: ", atm.checkBalance(card))

        # Deposit
        elif key == 'D':
            deposit = input("How much money would you like to deposit? " +
                            "If you'd like to go back to the previous menu, enter Q: ")

            if deposit == 'Q':
                continue

            elif not deposit.isdigit() or deposit == 0:
                print("Invalid deposit")

            else:
                atm.deposit(card, deposit)
                print("Your current balance is: ", atm.checkBalance(card))

        # Withdraw
        elif key == 'W':
            withdraw = input("How much money would you like to withdraw? " +
                             "If you'd like to go back to the previous menu, enter Q: ")

            if withdraw == 'Q':
                continue

            elif not withdraw.isdigit() or withdraw == 0:
                print("Invalid withdraw")

            else:
                atm.withdtraw(card, withdraw)
                print("Your current balance is: ", atm.checkBalance(card))
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()
