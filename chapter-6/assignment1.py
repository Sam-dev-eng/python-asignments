
# a) add  | no such method as add
# b) keys | prints the keys in the dictionary
# c) values | prints the values of the dictionary
# d) items | prints bot the values and the keys in the dictionary

from collections import Counter
text = 'to be or not to be that is the question'
counter = Counter(text.split())
print(counter)
sorted_count = sorted(counter)
for word, count in enumerate(sorted_count):
 print(f'{word:<12}{count}')

temperatures = {
 'Monday': [66, 70, 74],
 'Tuesday': [50, 56, 64],
 'Wednesday': [75, 80, 83],
 'Thursday': [67, 74, 81]
}
for k, v in temperatures.items():
 print(f'{k}: {sum(v)/len(v):.2f}')

# this code  is finding the average of each day of the week

list_one = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256}
list_two = {1, 2, 4, 8, 16} |  {1, 4, 16, 64, 256} # {2,8}
list_three = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256} # {1,4,16}
list_four = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256} # {2,8,64,256}
list_five = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256} # False

print(list_one)
print(list_two)
print(list_three)
print(list_four)
print(list_five)

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
print(tlds.__contains__("Canada"))
