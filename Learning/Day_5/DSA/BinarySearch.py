def binary(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start+end)/2)
        if arr[mid] >= target:
            end = mid - 1
        elif arr[mid] <= target:
            start = mid + 1
    return start

arr = [1,2,3,4,5,6,7,8,9,10]
print("The Index of 7 is :",binary(arr, 7))

# Q1) In the List of Roll Numbers, if student wants to check his/her roll number is present or not. 

def find_roll(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start+end)/2)
        if arr[mid] >= target:
            end = mid - 1
        elif arr[mid] <= target:
            start = mid + 1
    return "Roll no. ", target, "is present at index no.",start

arr = [1,2,3,4,5,6,7,8,9,10]
print("The Index of 7 is :",find_roll(arr, 7))
