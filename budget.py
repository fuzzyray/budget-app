class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.__balance = 0.0

    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate ledger description and amount to 23 and 7 characters respectively
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.__balance)
        return header + ledger + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.__balance += amount

    def withdraw(self, amount, description=""):
        if self.__balance - amount >= 0:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, "Transfer to {}".format(category_instance.description)):
            category_instance.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.__balance >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    return "spend_chart"
