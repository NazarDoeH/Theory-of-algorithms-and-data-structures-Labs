import math

def ArrayFlip(inputArray): #Обернення масиву
    temp = 0.0
    arraySize = inputArray.size - 1

    index = arraySize
    while index > math.floor(arraySize / 2):        
        temp = inputArray[arraySize - index]
        inputArray[arraySize - index] = inputArray[index]
        inputArray[index] = temp
        index -= 1     

def BubbleSort(inputArray): #Бульбашкове сортування
    n = len(inputArray)
    for i in range(n):        
        for j in range(0, n-i-1):            
            if inputArray[j] > inputArray[j+1]:                
                inputArray[j], inputArray[j+1] = inputArray[j+1], inputArray[j]

def InsertionSort(arr): #Сортування вставкою
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def QuickSort(arr): #Швидке сортування
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

def BinarySearch(arr, target = -1): #Бінарний пошук
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1