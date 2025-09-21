def temperature_value(temp, unit_of_measurement = "C", threshold_value = 0):
    unit = unit_of_measurement.upper() if unit_of_measurement else "C" 
    if unit == "C":
      result = temp * (9/5) + 32 
    elif unit == "F":
      result = (temp - 32) * (5 / 9)
    else:
      raise ValueError
    return result
    if result < threshold_value:
          return "Cold advisory"
    elif result >= threshold_value:
          return "Heat allert" 


def promotion_function(name , original_price , promo_code):
   
   if type(name) == int or type(original_price) == str:
     raise ValueError

   if promo_code == "SAVE10":
     return original_price - (10/100 * original_price)  

   elif promo_code == "HALFOFF":
     return original_price - (50/100 * original_price)  
   else:
      return "No discount"





def palindrome(number):
    main_number = number
    reverse_num = 0
    while number != 0:
       reverse_num = reverse_num * 10 + number % 10
       number = number // 10
    return reverse_num == main_number
    

def primeNumbers(number):
    import math
   
    if number == 2:
      return True 
    if number <= 1:
      return False
    if number % 2 == 0:
      return False
    
    for numbers in range(3 , int(math.sqrt(number)) + 1 , 2):
      if number % numbers == 0:
        return False

    return True 


def main(number):
    if type(number) == str:
      raise ValueError
 
    palindrom = palindrome(number)
    prime = primeNumbers(number)
    
    if palindrom == True and prime == True:  
        return True
    else:
        return False
     


     









