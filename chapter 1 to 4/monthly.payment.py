principal_amount = int(input("Enter the principal amount "))
annual_interest = float(input("Enter annual interest "))
duration = float(input("Enter duration in years "))

PERCENTAGE = 100 
MONTHS_IN_YEAR = 12

monthly_rate = annual_interest / (PERCENTAGE  * MONTHS_IN_YEAR)
number_of_months_in_duration = duration * MONTHS_IN_YEAR 

numarator_calculation = monthly_rate  * (1 + monthly_rate ) ** number_of_months_in_duration 
dinomination_calculation = ((1 + monthly_rate ) ** number_of_months_in_duration)- 1
monthly_payment = principal_amount * (numarator_calculation / dinomination_calculation) 

print("Monthly Payment is $",monthly_payment )
