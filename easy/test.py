#  Merge Sort

import time
from random import randint

nums = [randint(0,1000000) for i in range(1000000)]


def mergeSort(alist):
    
    # Step 1: Divide the array into equal parts (as much as possible)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        # recursively call mergeSort to perform splits if need
        # Then merge once splits are done
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        # index pointers for our list
        i = 0 # pointer for left half
        j = 0 # pointer for right half
        k = 0 # pointer for main array
        
        # Step 2: Compare the lefthalf and righthalf
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        # Step 3: While merging place items in correct position
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    return alist



start = time.time()
mergeSort(nums)
end = time.time()
print(f"MergeSort time:\n{(end - start) * 1000.0}\n\n")


# Bubble Sort

# Helper Function
def swap(i,j, array):
    array[i],array[j] = array[j],array[i]
    
    
    
def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for num in range(len(array) - 1):
            if array[num] > array[num + 1]:
                swap(num, num + 1, array)
                isSorted = False
    return array

start1 = time.time()
bubbleSort(nums)
end1 = time.time()
print(f"BubbleSort time:\n{(end1 - start1) * 1000.0}")