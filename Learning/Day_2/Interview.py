# Q1) Find the max number in a list without using built-in functions

def Max_num(List1):
    max_num = List1[0]
    for i in List1:
        if i > max_num:
            max_num = i
    return max_num
print("Maximum Number is : ",Max_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  


# Q2) Find the Second Max number in a list without using built-in functions

def Second_Max_num(List1):
    max_num = List1[0]
    second_max = 0
    for i in List1:
        if i > max_num:
            second_max = max_num
            max_num = i
        elif max_num > i > second_max:
            second_max = i
    return second_max
print("Second_Maximum Number is : ",Second_Max_num([5,7,9,1,8]))  

# Q3) Find Vowels and its count in a String

def Vowels_count(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count
str = input("Enter the String : ")
print(Vowels_count(str))

# Q4) Reverse a String without using built-in functions

def Reverse_string(string):
    reversed_string = ' '
    for i in string: # i = H e l l o
        reversed_string = i + reversed_string # reversed_string = H + ' ' = H  + e + ' ' = eH + l + ' ' = leH + l + ' ' = lleH + o + ' ' = olleH
    return reversed_string
str = input("Enter the String : ")
print(Reverse_string(str))