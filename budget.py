class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.__balance = 0.0

    def __repr__(self):
        header = self.category.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            ledger += "{:<23}{:>7.2f}\n".format(item["description"][:23], item["amount"])
        total = "Total: {:.2f}".format(self.__balance)
        return "{}{}{}".format(header, ledger, total)

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
        if self.withdraw(amount, "Transfer to {}".format(category_instance.category)):
            category_instance.deposit(amount, "Transfer from {}".format(self.category))
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
