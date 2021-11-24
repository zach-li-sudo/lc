def merge_sort(array):
    if len(array) == 1:
        return

    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    # merge sorted arrays
    i = j = 0
    k = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]: 
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1
        k += 1

    
    while i < len(left_arr):
        array[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        array[k] = right_arr[j]
        j += 1
        k += 1


myList = [54,26,93,17,77,31,44,55,20]
merge_sort(myList)
print(myList)




# def mergeSort(myList):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]

#         # Recursive call on each half
#         mergeSort(left)
#         mergeSort(right)

#         # Two iterators for traversing the two halves
#         i = 0
#         j = 0
        
#         # Iterator for the main list
#         k = 0
        
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#               # The value from the left half has been used
#               myList[k] = left[i]
#               # Move the iterator forward
#               i += 1
#             else:
#                 myList[k] = right[j]
#                 j += 1
#             # Move to the next slot
#             k += 1

#         # For all the remaining values
#         while i < len(left):
#             myList[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             myList[k]=right[j]
#             j += 1
#             k += 1

# myList = [54,26,93,17,77,31,44,55,20]
# mergeSort(myList)
# print(myList)