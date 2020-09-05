# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    alist = []
    if arrA == [] and arrB == []:
       return alist
    if arrA != [] and arrB == []:
       return alist + arrA
    if arrA == [] and arrB != []:
       return alist + arrB
    if arrA != [] and arrB != []:
       if arrA[0] <= arrB[0]:
          alist.append(arrA[0])
          alist = alist +  merge(arrA[1:], arrB)
       if arrA[0] > arrB[0]:
          alist.append(arrB[0])
          alist = alist +  merge(arrA, arrB[1:])
    return alist

    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    


    return alist

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort(arr1)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

# def partition(arr):
#     pivot = arr[1]
#     left = []
#     right = []
#     for element in arr[1:]:
#         if element < pivot:
#             left.append(element)
#         if element >= pivot:
#             right.append(element)
#     return left, right, pivot

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     left, right, pivot = partition(arr)
#     sorted_left = quicksort(left)
#     sorted_right = quicksort(right)
#     sorted = sorted_left + pivot + sorted_right
#     return sorted


