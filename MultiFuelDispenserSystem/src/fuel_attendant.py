from src.Dispenser_machine import DispenserMachine
from src.fuel import Fuel

class FuelAttendant:
    DispenserMachine = DispenserMachine()
    def __init__(self,name):
        self.name = name

    def update_fuel_price(self,machine,fuel_name,new_price):
        DispenserMachine.update_fuel_price(machine,fuel_name,new_price)

    def add_new_fuel(self,fuel_name,price_per_uit,initial_quantity):
       fuel = Fuel(fuel_name,price_per_uit,initial_quantity)

