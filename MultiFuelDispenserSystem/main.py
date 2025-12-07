from src.Dispenser_machine import DispenserMachine


def main():
    dispenser = DispenserMachine()
    user = input("""
            1-> Add a new fuel 
            2-> Get available fuels
            3-> Update fuel price
            4-> Restock fuel
            5-> Dispence fuel by amount
            6-> Dispense fuel by litters
            7-> Show all transactions 
            """)

    match user:
                case "1": addFuel(dispenser)
                case "2": getAvailableFuels()
                case "3": updateAvailableFuel(user)
                case "4": restockFuel(user)
                case "5": dispence_by_amount(user)
                case "6": dispence_by_litters(user)
                case "7": show_all_transactions(user)


def addFuel(dispenser):
    dispenser.
