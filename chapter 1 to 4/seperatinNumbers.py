user_input = int(input("Enter a number"))
number = 0
rever = 0
while user_input != 0:
   rever = rever * 10 
   number = user_input % 10
   user_input= user_input // 10
   
   print(number)




