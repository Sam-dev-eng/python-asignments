
def value_error_for_list(element):
   if type(element) != list:
      raise ValueError

def value_error_for_length(element):
   if len(element) == 0:
      raise ValueError

def value_error_for_tuple(element):
   if type(element) != tuple:
     raise ValueError

def value_error_for_int(element):
   if type(element) != int:
     raise ValueError

def value_error_for_string(element):
   if type(element) != str:
     raise ValueError





def adding_tuples(tuples_one , tuple_two):
 value_error_for_tuple(tuples_one)
 value_error_for_tuple(tuple_two)
 value_error_for_length(tuples_one) 
 value_error_for_length(tuple_two) 
 new_tuple = tuples_one + tuple_two 
 return new_tuple



def addition(num_one,num_two):
  return num_one + num_two

def sum_inner_list(two_dimensional_list):
  from functools import reduce
  value_error_for_list(two_dimensional_list)
  for index in two_dimensional_list:
   value_error_for_list(index)
  new_list = []
  for elements in two_dimensional_list:
    new_list.append(reduce(addition,elements))
    
  return new_list   
  

def is_even(numbers):
  return numbers % 2 == 0
def filters_even_numbers(list_of_numbers):
    value_error_for_list(list_of_numbers)
    return list(filter(is_even,list_of_numbers))






def lengths_than_five(words):
  return len(words) <= 5


def words_longer_than_five(list_words):
   value_error_for_list(list_words)
   for elements in list_words:
       value_error_for_string(elements)
   return list(filter(lengths_than_five, list_words))








def is_greater_than_two(numbers):
  for element in numbers:
     if type(element) == int and element >= 2:
       return True 
       

def turple_number_greater_than_two(list_of_tuples):
   value_error_for_length(list_of_tuples)
   value_error_for_list(list_of_tuples)
   for elements in list_of_tuples:
     value_error_for_tuple(elements)
     value_error_for_length(elements)
    
   return list(filter(is_greater_than_two,list_of_tuples)) 










def generate_numbers(start , stop):
  new_list = []
  for numbers in range(start , stop):
   new_list.append(numbers)
  return new_list


def is_three_and_five_divisibe(numbers):
   return numbers % 3 == 0 and numbers % 5 == 0


def three_and_five_divisible_numbers(numbers):
  value_error_for_list(numbers)
  value_error_for_length(numbers)
  for elements in numbers:
    value_error_for_int(elements)
  return list(filter(is_three_and_five_divisibe , generate_numbers(1,51))) 



def is_palindrome(words):
   lower_case = words.lower()
   return lower_case[::-1] == lower_case



def filter_palindrome(list_of_words):
   value_error_for_list(list_of_words)
   value_error_for_length(list_of_words)
   for elements in list_of_words:
    value_error_for_string(elements)
   return list(filter(is_palindrome , list_of_words))





def to_upper(words):
   return words.upper()


def text_to_upper(list_of_words):
  value_error_for_list(list_of_words)
  value_error_for_length(list_of_words)
  for elements in list_of_words:
    value_error_for_string(elements)
  return list(map(to_upper, list_of_words))



def sqare(number):
 return number ** 2

def squares_each_number(list_of_numbers):
  value_error_for_list(list_of_numbers)
  value_error_for_length(list_of_numbers)
  for elements in list_of_numbers:
    value_error_for_int(elements)
  return list(map(sqare , list_of_numbers))



  
def split_words(words):
  list_of_words = list(words)
  list_of_words[0] = words[0].upper() 
  return "".join(list_of_words)
   
def capitalize_first_letter(list_of_letters):
    value_error_for_list(list_of_letters)
    value_error_for_length(list_of_letters)
    for elements in list_of_letters:
      value_error_for_string(elements)
    return list(map(split_words,list_of_letters))




def is_ten_percent(number):
  percentage = 10 / 100 * number
  return percentage + number

def adding_ten_percent(prices):
   value_error_for_list(prices)
   value_error_for_length(prices)
   for elememts in prices:
    value_error_for_int(elememts) 
   return list(map(is_ten_percent , prices))



def add_number(number_one , number_two):
  return number_one + number_two


def numbers_sum(list_of_numbers):
   from functools import reduce
   value_error_for_list(list_of_numbers)
   value_error_for_length(list_of_numbers)
   for elements in list_of_numbers:
     value_error_for_int(elements)
   return reduce(add_number , list_of_numbers)


def is_max(number_one , number_two):
  max = number_one
  if number_two > max:
     max = number_two
  return max

def maximum_number(list_of_numbers):
   from functools import reduce
   value_error_for_list(list_of_numbers)
   value_error_for_length(list_of_numbers)
   for elements in list_of_numbers:
     value_error_for_int(elements)
   return reduce(is_max,list_of_numbers)




def list_to_str(word_one,word_two):
 return word_one +" "+ word_two

def concat_string_list(list_of_strings):
  from functools import reduce
  value_error_for_list(list_of_strings)
  value_error_for_length(list_of_strings)
  for elements in list_of_strings:
    value_error_for_string(elements)
  return reduce(list_to_str , list_of_strings)   



def square_num(numbers):
  return numbers**2 

def product_num(number_one,number_two):
  return number_one * number_two


def prodect_square(list_of_numbers):
   from functools import reduce
   value_error_for_list(list_of_numbers)
   value_error_for_length(list_of_numbers)
   for elements in list_of_numbers:
     value_error_for_int(elements)
   square_numbers = list(map(square_num,list_of_numbers))
   return reduce(product_num , square_numbers)
   
   




def is_greater_than_five(number):
   return number >= 5

def sum_element_greater_than_five(list_of_turple):
    from functools import reduce
    value_error_for_list(list_of_turple)
    value_error_for_length(list_of_turple)
    for elements in list_of_turple:
      value_error_for_tuple(elements)
      value_error_for_length(elements)
      for element in elements:
          value_error_for_int(element)

    new_list = []
    for elements in list_of_turple:
      new_list.append(reduce(add_number,elements))
    return list(filter(is_greater_than_five,new_list))
    

def is_non_numeric_string(string):
  if string.isdigit() == False:
    return True
  if string.isdigit() == True:
    return False


def is_numeric_string(string):
  return string.isdigit()

def ascii_of_words(words):
  sum = 0
  for char in words:
    sum += ord(char)
  return sum

def sum_non_numeric_and_numeric_strings(list_of_elements):
  from functools import reduce
  value_error_for_list(list_of_elements)
  for elements in list_of_elements:
   value_error_for_string(elements)

  list_of_words = list(filter(is_non_numeric_string,list_of_elements))
  sum_of_each_ascii_word = list(map(ascii_of_words,list_of_words))
  digits = list(filter(is_numeric_string,list_of_elements))
  concat_digits_to_int = list(map(int,digits)) 
  concat_to_one_list =   sum_of_each_ascii_word + concat_digits_to_int
  return reduce(add_number , concat_to_one_list) 









   















