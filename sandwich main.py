import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            for item, amount in resources.items():
                print(f"{item.capitalize()}: {amount}")

        elif choice in recipes:
            order = recipes[choice]
            if sandwich_maker_instance.check_resources(order["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, order["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, order["ingredients"])
        else:
            print("Invalid option. Please choose small, medium, large, report, or off.")


if __name__ == "__main__":
    main()
