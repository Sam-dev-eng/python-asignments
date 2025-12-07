


class Fuel:
    def __init__(self,name, price_per_unit, initial_quantity):
        self.available_quantity = None
        self.name = name
        self.price_per_unit = price_per_unit
        self.available_quantity += initial_quantity

    def dispense_by_amount(self, amount):
        if amount >= self.available_quantity:
            cost = self.get_cost_by_amount(amount)
            return cost - self.available_quantity
        return None

    def dispense_by_liters(self, amount):
        if amount >= self.available_quantity:
            amount = amount -  self.available_quantity
            return amount
        return None

    def get_cost_by_liters(self, quantity):
        cost = quantity * self.price_per_unit
        return cost

    def get_cost_by_amount(self, amount):
        cost = amount / self.price_per_unit
        return cost

    def update_price(self, new_price):
        if new_price >= 10:
           self.price_per_unit = new_price

    def restock(self,amount):
        if amount >= 100:
            self.available_quantity = amount


