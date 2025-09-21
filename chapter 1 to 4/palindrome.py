number = int(input("Enter a number "))
original = number
reversed = 0
while number != 0:
 reversed = reversed * 10 + number % 10
 number = number // 10
if reversed == original:
   print("True")
else:
   print("False")  