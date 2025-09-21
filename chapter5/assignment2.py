import re
def mystery(sequence):
    return sequence == sorted(sequence)
 # the following code returns a boolean value True or False when the input is being sorted

number = [(x,x * 0.0254) for x in [69, 77, 54]]
print(list(map(lambda x: (x, x * 0.0254) , [69, 77, 54])))
print(number)


list_of_numbers = [["mango","orange"],
                   ["pawpaw", "pineapple"],
                   ["Guava","water melon"]
]

for items in list_of_numbers:
    print(items[0],end= "    ")
print()
count = 0
# for items in list_of_numbers:
#     # print(items[1], end="    ")


# (5.5)---
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[0:13:]) # a|
print(alphabet[:13:]) # b|
print(alphabet[13:27:]) # c|
print(alphabet[:-14:-1]) # d|
print(alphabet[::2])# E|
print(alphabet[::-1])# F|
print(alphabet[::-3])# G|


def function(args_one, args_two, args_three):
    return args_three , args_one , args_two


a = "Daug"
b = 22
c = 1984
print(function(a, b, c))


def unique_values(list_of_numbers):
    new_list = []
    for items in list_of_numbers:
        if type(items) == int and items not in new_list:
            new_list.append(items)
    return sorted(new_list)

values = ["orange","fruits",6,7,39,8,30,2,2,39,2,7,"mango"]
numbers = unique_values(values)
print(numbers)

def is_palindrome(input_letters):
    word = input_letters.lower()
    pattern = r"\b\w+\b"
    sorted_letters = "".join(re.findall(pattern, word))
    return sorted_letters == sorted_letters[::-1]


letters = "radar"
print(is_palindrome(letters))
