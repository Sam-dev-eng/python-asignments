import unittest 
import temperature_measurement



class TestTemperatureValue(unittest.TestCase):

  def test_if_the_function_exists(self):
    temperature_measurement.temperature_value(0,0,0)

  def test_if_the_conversion_to_F_is_working(self):
    result = temperature_measurement.temperature_value(30,"C",0)
    self.assertEqual(result ,86)

  def test_if_the_conversion_to_C_is_working(self):
    result = temperature_measurement.temperature_value(30,"F",0)
    self.assertEqual(result ,-1.1111111111111112)

  def test_if_the_default_is_working(self):
     result = temperature_measurement.temperature_value(30, "",0)
     self.assertEqual(result ,86)

  def test_if_the_upper_case_is_working(self):
     result = temperature_measurement.temperature_value(30, "f",0)
     self.assertEqual(result ,-1.1111111111111112)

  def test_if_the_ValueError_is_working(self):
     self.assertRaises(ValueError, temperature_measurement.temperature_value, 30,"p",0)
 
  def test_if_the_threshold_value_returns_Heat_allert(self):
     result = temperature_measurement.temperature_value(30, "c",20)
     self.assertEqual(result ,86,"Heat allert")

  def test_if_the_threshold_value_returns_Cold_advisory(self):
     result = temperature_measurement.temperature_value(30, "f",10)
     self.assertEqual(result ,-1.1111111111111112,"Cold advisory")





class TestPromotion(unittest.TestCase):

   def test_if_the_function_exists(self):
      temperature_measurement.promotion_function("n",0,0)


   def test_if_the_function_is_returning_10_percent_discount(self):
     result = temperature_measurement.promotion_function("n",1000,"SAVE10")
     self.assertEqual(result, 900)
 

   def test_if_the_function_is_returning_50_percent_discount(self):
     result = temperature_measurement.promotion_function("n",1000,"HALFOFF")
     self.assertEqual(result, 500)
 
   def test_for_when_theres_no_valid_code(self):
     result = temperature_measurement.promotion_function("n",1000,"ANOTHERDAY")
     self.assertEqual(result, "No discount")
 
   def test_for_valueError_validation(self):
     self.assertRaises(ValueError, temperature_measurement.promotion_function, "","","")


class TestPalindrom(unittest.TestCase):
     def test_if_the_function_exists(self):
       temperature_measurement.palindrome(0)
     
     def test_if_number_is_revesed(self):
       result =  temperature_measurement.palindrome(121)
       self.assertEqual(result , True)

class TestPrimeNumbers(unittest.TestCase):
     
     def test_if_the_function_exists(self):
        temperature_measurement.primeNumbers(0) 

     def test_if_two_is_a_prime_number(self):
        result = temperature_measurement.primeNumbers(2)
        self.assertEqual(result, True) 
     
     def test_if_decimal_numbrs_are_prime_numbers(self):
        result = temperature_measurement.primeNumbers(0.1)
        self.assertEqual(result, False) 
     
     def test_if_999_is_a_prime_number(self):
        result = temperature_measurement.primeNumbers(999)
        self.assertEqual(result, False) 
     

class TestBothPrimeAndPalindrome(unittest.TestCase):

    def test_if_the_function_exists(self):
        temperature_measurement.main(0)

    def test_if_the_both_functions_returns_true(self):
        result = temperature_measurement.main(131)
        self.assertEqual(result , True)

    def test_function_for_ValueError(self):
       self.assertRaises(ValueError, temperature_measurement.main, "") 

    def test_if_the_function_returns_false_when_not_true(self):
       result = temperature_measurement.main(121)
       self.assertEqual(result , False)
      
    def test_for_decimals(self):
       result = temperature_measurement.main(12.1)
       self.assertEqual(result , False)
      


