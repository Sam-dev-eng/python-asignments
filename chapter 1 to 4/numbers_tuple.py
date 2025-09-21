numbers = (1, 2, [3, 4], 5)
print("Initial result" , numbers[2])
numbers[2][1] = 99
print("final result",numbers[2])

print()
print()

tuple_of_strings = ("apple","bananna","cherry")
print("Turple of strings ", tuple_of_strings) 
new_list = list(tuple_of_strings)
print("Converted to list",new_list)
new_list.append("mango");
print("Added mango", new_list)
new_tuple = tuple(new_list)
print("Back to tuple", new_tuple)


a,b,*c = (10, 20,30, 40)
 
print("unpacked a as: ",a)
print("unpacked b as: ",b)
print("unpacked c as: " ,c)
print(type(c))


