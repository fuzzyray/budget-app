class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.__balance = 0

    def deposit(self, amount, description=""):
        pass

    def withdraw(self, amount, description=""):
        pass

    def get_balance(self):
        pass

    def transfer(self, amount, category_instance):
        pass

    def check_funds(self, amount):
        pass


def create_spend_chart(categories):
    pass
