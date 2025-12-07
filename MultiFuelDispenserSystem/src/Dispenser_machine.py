class DispenserMachine:
    FUELS = {}
    def __int__(self, fuels):
        self.fuel = fuels

    def get_available_fuels(self):
        return self.FUELS

    def dispense_fuel_by_amount(self, fuel_name, quantity):
        if fuel_name not in self.FUELS:
            raise NameError("Fuel name not found")
        self.FUELS[fuel_name].dipense(quantity)


    def add_fuel(self, fuel_name):
        if fuel_name not in self.FUELS:
            self.FUELS[fuel_name] = None

    def update_fuel_price(self,fuel_name,new_price):
        if fuel_name not in self.FUELS:
            raise NameError("Fuel name not found")
        self.FUELS[fuel_name].update(new_price)

    def restock(self,fuel_name,amount):
        if fuel_name not in self.FUELS:
            raise NameError("Fuel name not found")
        self.FUELS[fuel_name].restock(amount)

