# Selection Sort Algorithm Implementation in Python
# Selection Sort is an in-place comparison sorting algorithm that divides the input list into two parts: a sorted and an unsorted region. It repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the end of the sorted region.
# The algorithm maintains two subarrays in a given array:
# 1) The subarray which is already sorted.
# 2) The subarray which is unsorted.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11, 90]
print("Sorted Array is :", selection_sort(arr))