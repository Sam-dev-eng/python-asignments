first_input = input("What is your problem")
second_input = input("Have had this problem before(yes or no)?")

answer = second_input.lower()
if second_input == 'yes':
    print('Well, you have it again')
else:
    print('Well, you have it now') 