largest = 0
second_largest = 0


for numbers in range(10):
  User_input= int(input("Enter a number "))
  if User_input > largest:
    second_largest = largest
    largest = User_input
  elif User_input > second_largest and largest != User_input:
    second_largest = User_input 
print(largest)
print(second_largest) 