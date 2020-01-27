# 1 Bubble sort | Swap elements

A = [5, 9, 1, 2, 4, 8, 6, 3, 7]

def bubblesort(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

print(bubblesort(A))

# asymptotic time complexity - 0(n2) - tita (0) of n square - performance is worst (not good to use for sorting for 1 mln numbers)

# 2 Selection sort | Brute force - Locate the smallest item and put it in the first place, then the next smallest and put it in second place. From left to right.

A = [5,9,1,2,4,8,6,3,7]

def selectionsort(A):
    for i in range (0, len(A)-1):
        minIndex = i
        for j in range (i+1, len(A)):   # itterate for unsorted part of array
            if A[j] < A[minIndex]:      # If you find smaller item than minIndex
                minIndex = j            # update the index of the min element
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]   # exchange/swap elements
    return A

print(selectionsort(A))

# asymptotic time complexity - 0(n2) - tita (O) of n square - if make input 10 times bigger, time will increase 100 times biggers

# 30 Insertion sort

A = [5,9,1,2,4,8,6,3,7]

def insertionsort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    return A

print(insertionsort(A))

# 31 Quick Sort | https://www.geeksforgeeks.org/quick-sort/

arr = [10, 7, 8, 9, 1, 5]

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

quicksort(arr, 0, len(arr)-1)
print(arr)

# 32 Merge Sort | https://www.geeksforgeeks.org/merge-sort/

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(mergeSort(arr))