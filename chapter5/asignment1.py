# whats wrong with the following codes ::

# 1a)
day, high_temperature, num = ('Monday', 87,65) #the last variable 65 has no variable that unpacked it

#1b)
numbers = [1, 2, 3, 4, 5]
numbers[10] # has no idex 10

#1c)
name = 'amanda'
name[0] = 'A' #name is not a list

# 1d)
numbers = [1, 2, 3, 4, 5]
numbers[3.4] # index does not exist

# 1e)
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
# Nothing is wrong with the code

# 1f)
num = ('Monday', 87, 65) + 'Tuesday'
# cannot concatenate string to tuple only turple to turple

# 1G)
'A' += ('B', 'C'))
# cannot assign to literal

x = 7
del x
print(x)
# X has been deleted

# 1i)
numbers = [1, 2, 3, 4, 5]
numbers.index(10)
# whats wrong with the following codes ::

# 1a)
day, high_temperature, num = ('Monday', 87,65) #the last variable 65 has no variable that unpacked it

#1b)
numbers = [1, 2, 3, 4, 5]
numbers[10] # has no idex 10

#1c)
name = 'amanda'
name[0] = 'A' #name is not a list

# 1d)
numbers = [1, 2, 3, 4, 5]
numbers[3.4] # index does not exist

# 1e)
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
# Nothing happened
#j)

numbers = [1, 2, 3, 4, 5]
numbers.extend(6, 7, 8)
# only allow iterables like list
#k)
numbers = [1, 2, 3, 4, 5]
numbers.remove(10)
# 10 does not exist
#l)
values = []
values.pop()
# no value to pop or remove