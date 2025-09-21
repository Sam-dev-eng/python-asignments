side_one = 1
side_two = 1
hypo = 0
for numbers in range(1,21):
 hypo = numbers
 for numbers in range(1,21):
  side_one = numbers ** 2
 for numbers in range(1,21):
  side_two = numbers ** 2
 if side_one + side_two == hypo:
   print(side_one , side_two, hypo) 


  
    
