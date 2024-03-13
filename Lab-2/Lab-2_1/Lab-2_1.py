import math
import matplotlib.pyplot as plt
import FunctionTeser as ft

def plot_graphs(name):
    # Графік для tester.timeUsageInt
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 2, 1)
    plt.plot(tester.timeUsageInt, label='timeUsageInt')
    plt.title('Time Usage (Int) ' + name)

    # Графік для tester.memoryUsageInt
    plt.subplot(2, 2, 2)
    plt.plot(tester.memoryUsageInt, label='memoryUsageInt')
    plt.title('Memory Usage (Int) ' + name)

    # Графік для tester.memoryUsageFloat
    plt.subplot(2, 2, 3)
    plt.plot(tester.memoryUsageFloat, label='memoryUsageFloat')
    plt.title('Memory Usage (Float) ' + name)

    # Графік для tester.timeUsageFloat
    plt.subplot(2, 2, 4)
    plt.plot(tester.timeUsageFloat, label='timeUsageFloat')
    plt.title('Time Usage (Float) ' + name)

    plt.tight_layout()
    plt.show()


def ArrayFlip(inputArray): #Обернення масиву
    temp = 0.0
    arraySize = inputArray.size - 1

    index = arraySize
    while index > math.floor(arraySize / 2):        
        temp = inputArray[arraySize - index]
        inputArray[arraySize - index] = inputArray[index]
        inputArray[index] = temp
        index -= 1     

def BubbleSort(inputArray):
    n = len(inputArray)
    for i in range(n):        
        for j in range(0, n-i-1):            
            if inputArray[j] > inputArray[j+1]:                
                inputArray[j], inputArray[j+1] = inputArray[j+1], inputArray[j]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

def BinarySearch(arr, target = -1):
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

tester = ft.FunctionTester()

tester.TestSpeedAndMemory(ArrayFlip)
plot_graphs("ArrayFlip")

tester.TestSpeedAndMemory(BubbleSort)
plot_graphs("BubbleSort")

tester.TestSpeedAndMemory(InsertionSort)
plot_graphs("InsertionSort")

tester.TestSpeedAndMemory(QuickSort)
plot_graphs("QuickSort")

tester.TestSpeedAndMemory(BinarySearch)
plot_graphs("BinarySearch")