import code_leveling
import unittest


class TestForTupleOfNumbers(unittest.TestCase):
   
    def test_if_the_function_exists(self):
         code_leveling.adding_tuples((4,5),(9,47))

    def test_if_the_function_is_accurate(self):
         result = code_leveling.adding_tuples((1,4,6,43,4),(36,4,8,6,44,7))
         self.assertEqual(result , (1,4,6,43,4,36,4,8,6,44,7))

    def test_for_value_errors_in_the_function(self):
         self.assertRaises(ValueError , code_leveling.adding_tuples, "","")

    def test_when_the_length_is_zero(self):
         self.assertRaises(ValueError , code_leveling.adding_tuples,(),() )
 



class TestForInnerListSummation(unittest.TestCase):

     def test_if_the_function_exists(self):
        code_leveling.sum_inner_list([[2],[3],[7]])        


     def test_if_the_function_is_accurate(self):
       result = code_leveling.sum_inner_list([[1,3,4],[5,3,6],[4,6,9]]) 
       self.assertEqual(result , [8,14,19])       


     def test_raise_value_error_if_the_user_inputs_only_one(self):
        self.assertRaises(ValueError , code_leveling.sum_inner_list, [1,4,6]) 
        

     def test_raise_value_error_if_the_inputs_are_in_strings_or_int(self):
        self.assertRaises(ValueError , code_leveling.sum_inner_list, "4") 
        


class TestForEvenNumbers(unittest.TestCase):

     def test_if_the_function_exist(self):
         code_leveling.filters_even_numbers([0])


     def test_if_the_function_is_correct(self):
         result =  code_leveling.filters_even_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) 
         self.assertEqual(result ,[2,4,6,8,10,12,14,16,18,20])

     def test_for_value_errors_if_its_a_non_list_input(self):
         self.assertRaises(ValueError , code_leveling.filters_even_numbers , "")


    

class TestWordsLongerThanFive(unittest.TestCase):
   
     def test_if_the_function_exists(self):
       code_leveling.words_longer_than_five(["mango"])  


     def test_if_the_function_is_correct(self):
       result = code_leveling.words_longer_than_five(["mango", "cat","elephant", "tiger", "lion"])  
       self.assertEqual(result ,["mango","cat","tiger","lion"])

     def test_if_the_function_raises_value_errors(self):
        self.assertRaises(ValueError , code_leveling.words_longer_than_five , "")

     def test_if_the_function_raises_value_error_when_list_of_int_is_passed(self):
        self.assertRaises(ValueError , code_leveling.words_longer_than_five , [67])
 


class TestTupleNumbrsGreaterThanTwo(unittest.TestCase):
     def test_if_the_function_exist(self):
       code_leveling.turple_number_greater_than_two([(2,"a"),(3,"d")])


     def test_if_the_function_is_correct(self):
       result = code_leveling.turple_number_greater_than_two([(1, "A"), (4, "B"),(2, "C")])
       self.assertEqual(result , [(4,"B"),(2,"C")])

     def test_if_the_function_raises_value_error(self):
       self.assertRaises(ValueError , code_leveling.turple_number_greater_than_two, "")

     def test_if_the_function_raises_value_error_for_empty_list(self):
       self.assertRaises(ValueError , code_leveling.turple_number_greater_than_two, [])
    
     def test_if_the_function_raises_value_error_for_empty_turple(self):
       self.assertRaises(ValueError , code_leveling.turple_number_greater_than_two, [()])



class TestNumbersDivisibleByThreeAndFive(unittest.TestCase):
   
     def test_if_the_function_exist(self):
        code_leveling.three_and_five_divisible_numbers([1,2])

     def test_if_the_function_performes_well(self):
        result = code_leveling.three_and_five_divisible_numbers(code_leveling.generate_numbers(1,51))
        self.assertEqual(result , [15, 30, 45])

     def test_for_value_error_when_strings_pass_in(self):
       self.assertRaises(ValueError , code_leveling.three_and_five_divisible_numbers , "")
        
     def test_if_someone_puts_an_empty_array(self):
       self.assertRaises(ValueError , code_leveling.three_and_five_divisible_numbers , [])
        
     def test_if_user_inputs_string_in_a_list(self):
       self.assertRaises(ValueError , code_leveling.three_and_five_divisible_numbers , [677,887,"mango"])


class TestForPalindromNumbers(unittest.TestCase):
    def test_if_the_number_exist(self):
       code_leveling.filter_palindrome(["madam"]) 

    def test_if_the_function_is_correct(self):
       result = code_leveling.filter_palindrome(["level","world","madam", "python"]) 
       self.assertEqual(result , ["level","madam"])

    def test_for_upper_and_lower_cases(self):
      result = code_leveling.filter_palindrome(["Level","World","Madam","Python"]) 
      self.assertEqual(result , ["Level","Madam"])

    def test_for_value_error_when_non_list_is_inputed(self):
       self.assertRaises(ValueError , code_leveling.filter_palindrome, "" )

    def test_if_the_function_raises_value_error_with_array_of_int(self):
      self.assertRaises(ValueError , code_leveling.filter_palindrome, [78])

    def test_for_an_empty_list(self):
      self.assertRaises(ValueError , code_leveling.filter_palindrome, [])




class TestForUpperCase(unittest.TestCase):

   def test_if_the_function_exist(self):
     code_leveling.text_to_upper(["samuel"]) 

   def test_if_the_function_is_accurate(self):
     result = code_leveling.text_to_upper(["python", "java", "c++"]) 
     self.assertEqual(result , ["PYTHON", "JAVA", "C++"])

   def test_if_the_function_raises_value_error(self):
     self.assertRaises(ValueError , code_leveling.text_to_upper, "")
   
   def test_for_list_of_int_as_input(self):
     self.assertRaises(ValueError , code_leveling.text_to_upper, [23])
   
   def test_if_its_an_empty_list(self):
     self.assertRaises(ValueError , code_leveling.text_to_upper, [])

   
   
class TestForSquarNumbers(unittest.TestCase):
     
   def test_if_the_number_exist(self):
      code_leveling.squares_each_number([1,23,3])
      
   def test_if_the_function_is_correct(self):
      result = code_leveling.squares_each_number(code_leveling.generate_numbers(1,11))
      self.assertEqual(result , [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])      

   def test_if_the_function_raises_value_error(self):
      self.assertRaises(ValueError , code_leveling.squares_each_number , "") 

   def test_for_int_input_in_list(self):
      self.assertRaises(ValueError , code_leveling.squares_each_number , [""]) 

   def test_for_empty_list(self):
     self.assertRaises(ValueError , code_leveling.squares_each_number , []) 



  


class TestCapitalFirstLetter(unittest.TestCase):
    def test_if_the_function_exist(self):
       code_leveling.capitalize_first_letter(["john"])
     
    def test_if_the_function_is_working(self):
       result =  code_leveling.capitalize_first_letter( ["john", "mary","steve"])
       self.assertEqual(result , ["John", "Mary","Steve"])
     
    def test_if_the_function_raises_value_error(self):
       self.assertRaises(ValueError , code_leveling.capitalize_first_letter, "") 

    def test_if_function_raises_value_error_for_int_in_list(self):
       self.assertRaises(ValueError , code_leveling.capitalize_first_letter, [23]) 
  
    def test_for_empty_list(self):
       self.assertRaises(ValueError , code_leveling.capitalize_first_letter, []) 
  



class TestForAddingPercentage(unittest.TestCase):

   def test_if_the_function_exists(self):
      code_leveling.adding_ten_percent([100])

   def test_the_function_is_accurate(self):
      result =  code_leveling.adding_ten_percent([100,200,300])
      self.assertEqual(result , [110.00,220.00,330.00])
 
   def test_for_value_error(self):
       self.assertRaises(ValueError , code_leveling.adding_ten_percent,"")

   def test_for_list_of_string(self):
       self.assertRaises(ValueError , code_leveling.adding_ten_percent,["a"])

   def test_for_empty_list(self):
       self.assertRaises(ValueError , code_leveling.adding_ten_percent,[])






class TestForSumOfNumbers(unittest.TestCase):

   def test_if_the_function_exist(self):
    code_leveling.numbers_sum([20,30])
  
   def test_the_function_is_accurate(self):
     result =  code_leveling.numbers_sum(code_leveling.generate_numbers(1,51))
     self.assertEqual(result ,  1275)

   def test_for_value_error_for_non_list(self):
       self.assertRaises(ValueError , code_leveling.numbers_sum,"")

   def test_for_list_of_string_in_a_list(self):
       self.assertRaises(ValueError , code_leveling.numbers_sum,["a"])

   def test_for_empty_list_of_list(self):
       self.assertRaises(ValueError , code_leveling.adding_ten_percent,[])
 
 



class TestForMaximumNumber(unittest.TestCase):
    
    def test_if_the_function_exist(self):
       code_leveling.maximum_number([8,9])


    def test_if_the_function_is_accurate(self):
       result =  code_leveling.maximum_number([8,9,10,6,4,12,78])
       self.assertEqual(result , 78)

    def test_for_value_error_for_string_input(self):
     self.assertRaises(ValueError, code_leveling.maximum_number, "" )

    def test_for_value_error_for_wrong_list_input(self):
      self.assertRaises(ValueError, code_leveling.maximum_number, ["s"])

    def test_for_value_error_for_empty_list(self):
       self.assertRaises(ValueError, code_leveling.maximum_number, [])




class TestForConcat_function(unittest.TestCase):
 
    def test_if_the_function_exist(self):
       code_leveling.concat_string_list(["programing"])
    
    def test_if_the_function_is_accurate(self):
       result = code_leveling.concat_string_list(["I", "love", "Python"])
       self.assertEqual(result , "I love Python")
    
    def test_for_value_error_for_non_list_input(self):
       self.assertRaises(ValueError , code_leveling.concat_string_list, "") 


    def test_for_value_error_for_empty_list(self):
       self.assertRaises(ValueError , code_leveling.concat_string_list, []) 

    def test_for_value_error_for_wrong_list_input(self):
       self.assertRaises(ValueError , code_leveling.concat_string_list, [789]) 






class TestForProductSquare(unittest.TestCase):
   
    def test_if_the_function_exist(self):
        code_leveling.prodect_square([1,2,4])

    def test_if_the_function_is_correct(self):
        result = code_leveling.prodect_square([1,2,4,5,6])
        self.assertEqual(result, 57600)

    def test_if_the_function_raises_value_error_for_str_input(self):
       self.assertRaises(ValueError, code_leveling.prodect_square, "")
    
    def test_for_value_error_for_str_in_a_list(self):
        self.assertRaises(ValueError, code_leveling.prodect_square, ["g"])
    

    def test_for_empty_list_input(self):
        self.assertRaises(ValueError, code_leveling.prodect_square, [])
    


class TestForSumOfElementsGreaterThanFive(unittest.TestCase):
     
      def test_if_the_function_exists(self):
        code_leveling.sum_element_greater_than_five([(1,2),(1,2)])

      def test_for_accuracy_in_the_function(self):
        result = code_leveling.sum_element_greater_than_five([(1,2),(3,4),(5,6)])
        self.assertEqual(result,[7,11]) 

      def test_for_value_error_if_its_not_a_list(self):
        self.assertRaises(ValueError , code_leveling.sum_element_greater_than_five, "")

  
      def test_for_value_error_when_the_list_is_empty(self):
        self.assertRaises(ValueError , code_leveling.sum_element_greater_than_five, [])

      def test_for_value_error_when_the_list_doesnt_contain_a_turple(self):
        self.assertRaises(ValueError , code_leveling.sum_element_greater_than_five, [23])
    
      def test_for_value_error_when_the_turple_is_empty(self):
        self.assertRaises(ValueError , code_leveling.sum_element_greater_than_five, [()])

      def test_for_value_error_when_the_turple_is_not_an_int(self):
        self.assertRaises(ValueError , code_leveling.sum_element_greater_than_five, [("")])




class TestForSumOfNonNumericAndNumericSrings(unittest.TestCase):
   
    def test_if_the_function_exists(self):
       code_leveling.sum_non_numeric_and_numeric_strings(["abc","123"])
     

    def test_if_the_function_is_accurate(self):
     result = code_leveling.sum_non_numeric_and_numeric_strings(['123', '456', '789','abc', 'def'])
     self.assertEqual(result , 1965)   
     

    def test_for_value_error_if_list_of_int_is_added(self):
      self.assertRaises(ValueError , code_leveling.sum_non_numeric_and_numeric_strings, [123])

    def test_for_non_list_input(self):
      self.assertRaises(ValueError , code_leveling.sum_non_numeric_and_numeric_strings, "ijoie")























