# # Bubble Sort in Python 
# # Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the

# def bubble_sort(arr):
#     n = len(arr) - 1
#     for i in range(n):
#         for j in range(n-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
    
# arr = [64, 32, 25, 12, 22, 11, 90]
# print("Sorted Array is :", bubble_sort(arr))


# Q1) Sort the Items in the Shop on the BAsis Of their Prices using Bubble Sort

def bubble_sort_items(items):
    new_items = list(items.items())
    n = len(new_items) - 1
    for i in range(n):
        for j in range(n-i):
            if new_items[j][1] > new_items[j+1][1]:
                new_items[j], new_items[j+1] = new_items[j+1], new_items[j]
    return dict(new_items)
items = {"Apple" : 120, "Banana" : 30, "Orange" : 80, "Mango" : 150, "Grapes" : 90}
print(bubble_sort_items(items))      