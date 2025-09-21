import factorials
num = 0
for numbers in range(1 , 10):
 num += 1 / factorials.factorial(numbers)
print(num + 1)