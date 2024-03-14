import Algorithms as algorithms
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

tester = ft.FunctionTester()

tester.TestSpeedAndMemory(algorithms.ArrayFlip)
plot_graphs("ArrayFlip")

tester.TestSpeedAndMemory(algorithms.BubbleSort)
plot_graphs("BubbleSort")

tester.TestSpeedAndMemory(algorithms.InsertionSort)
plot_graphs("InsertionSort")

tester.TestSpeedAndMemory(algorithms.QuickSort)
plot_graphs("QuickSort")

tester.SortTestArray(algorithms.QuickSort)
tester.TestSpeedAndMemory(algorithms.BinarySearch)
plot_graphs("BinarySearch")