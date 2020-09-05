# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search(arr, elem, mid+1, end)

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr1, -8, 0, len(arr1)-1)
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

