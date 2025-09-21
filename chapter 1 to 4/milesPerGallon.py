average = 0
count = 0
gallon_used = 0
while  gallon_used != -1:
    number_of_miles = float(input("Enter miles driven : "))
    gallon_used = float(input("Enter the  gallon used : "))
    #if gallon_used == -1:
     #gallon_used = 1
    #break
    miles_per_gallon = number_of_miles / gallon_used
    average +=  miles_per_gallon 
    print(miles_per_gallon)
    count = count + 1

total_average = average / count
print(total_average)

 