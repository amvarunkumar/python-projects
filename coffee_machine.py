class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 30.0},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 50.0},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 60.0},
        }
        self.profit = 0

    def check_resources(self, choice):
        for item in self.menu[choice]:
            if item != "cost" and self.menu[choice][item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_payment(self, cost):
        amount = float(input(f"Please insert money (in rupees): ₹"))
        if amount >= cost:
            change = round(amount - cost, 2)
            print(f"Here is ₹{change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_coffee(self, choice):
        for item in self.menu[choice]:
            if item != "cost":
                self.resources[item] -= self.menu[choice][item]
        self.profit += self.menu[choice]["cost"]
        print(f"Here is your {choice}. Enjoy!")

    def start(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                break
            elif choice == "report":
                print(f"Water: {self.resources['water']}ml")
                print(f"Milk: {self.resources['milk']}ml")
                print(f"Coffee: {self.resources['coffee']}g")
                print(f"Money: ₹{self.profit}")
            elif choice in self.menu:
                if self.check_resources(choice):
                    if self.process_payment(self.menu[choice]["cost"]):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please choose again.")

# Create an instance of the CoffeeMachine and start it
coffee_machine = CoffeeMachine()
coffee_machine.start()
