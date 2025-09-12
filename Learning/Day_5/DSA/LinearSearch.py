# Linear Search in Python 

def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [30,40,50,60,70]
print(Linear_Search(arr, 70))


# Q1) Write a program to implement Linear Search (Recursive)
def Recursive_LinearSearch(arr, target, length, ind = 0):
    if ind == length:
        return -1
    
    if arr[ind] == target:
        return ind

    return Recursive_LinearSearch(arr, target, length, ind+1)

arr = [122,23,34,45,23,12,13,14,15,21,32,22,41,76]
length = len(arr)
print(Recursive_LinearSearch(arr, 14, length))

# Q2) Write a program to find the minimum and maximum element in an array.
def minmax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        elif min >  arr[i]:
            min = arr[i]
        else:
            continue
    return "Maximum : ", max," Minimum : ", min

arr = [27, 5, 12, 14 ,15, 25, 1, 2]
print(minmax(arr))


# Q3) Search for a roll No. in Student Record using Linear Search
def RollNo(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return "The Roll No is at Index : ",i+1
        else:
            continue
    return -1

arr = [21, 23, 54, 11, 1, 3, 2]
print(RollNo(arr, 3))
