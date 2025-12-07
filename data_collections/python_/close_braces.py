def closed_bracket(user_input):
    open_bracket = ["(","[","{","<"]
    close_bracket = [")","]","}",">"]
    open_list = []
    close_list = []
    for char in user_input:
        if char in open_bracket:
            open_list.append(open_bracket.index(char))

        if char in close_bracket:
            close_list.append(close_bracket.index(char))

    open_list.sort()
    close_list.sort()
        
    if len(open_list) != len(close_list):
        return False

    for index in range(len(open_list)):
        if open_list[index] != close_list[index]:
             return False
    return True


print(closed_bracket("k(l))()"))


























