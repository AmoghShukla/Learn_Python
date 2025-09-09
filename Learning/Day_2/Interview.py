# Q1) Find the max number in a list without using built-in functions

def Max_num(List1):
    max_num = List1[0]
    for i in List1:
        if i > max_num:
            max_num = i
    return max_num
print("Maximum Number is : ",Max_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  