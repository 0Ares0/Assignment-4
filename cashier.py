class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
