product = 1
largest = 0
smallest = 0
count = 0
sum = 0
product = 1
while count != 4:
	user_input = int(input("Enter a number"))
	count += 1 
	sum = sum + user_input
	product *= user_input 
	if user_input > largest:
		largest = user_input
	if user_input < largest:
		smallest = user_input
print(smallest, largest, sum, product)







