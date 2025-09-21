print("number  square  cube")
for number in range(1,6):
   
    square = number * number
    cube = number ** 3
   
    print(f"{number:<7} {square:<7} {cube:<7}")


#The print(f" is for place holders as strings 
#the {:<} are for allignment in a table of how many collums 
#you have to close the strings from the begining to the end of the {}
#eg. print(f"{} {} {} {}") not any other format 