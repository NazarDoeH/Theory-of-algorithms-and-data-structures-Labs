from time import perf_counter
import numpy as np
import tracemalloc

class FunctionTester:
    def __init__(self):

        #Випадкові цілочиселні масиви
        self.intArray10 = np.random.randint(0, 999, 10)
        self.intArray100 = np.random.randint(0, 999, 100)
        self.intArray500 = np.random.randint(0, 999, 500)
        self.intArray1000 = np.random.randint(0, 999, 1000)

        self.memoryUsageInt = np.array([0.0,0.0,0.0,0.0])   
        self.timeUsageInt = np.array([0.0,0.0,0.0,0.0])

        #Випадкові дробові масиви
        self.floatArray10 = np.random.ranf(10)
        self.floatArray100 = np.random.ranf(100)
        self.floatArray500 = np.random.ranf(500)
        self.floatArray1000 = np.random.ranf(1000)
                
        self.memoryUsageFloat = np.array([0.0,0.0,0.0,0.0])
        self.timeUsageFloat = np.array([0.0,0.0,0.0,0.0])


    def TestMemory(self, function, array): #Визначення викорисатння пам'яті
        tempArray = array
        tracemalloc.start()
        function(tempArray)            
        return tracemalloc.get_traced_memory()[0]                           

    def TestSpeed(slef, function, array): #Визначення затрат часу
        tempArray = array
        startTime = perf_counter()
        function(tempArray)    
        return perf_counter() - startTime

    def TestSpeedAndMemory(self, function):
        self.memoryUsageInt[0] = self.TestMemory(function, self.intArray10)
        self.memoryUsageInt[1] = self.TestMemory(function, self.intArray100)
        self.memoryUsageInt[2] = self.TestMemory(function, self.intArray500)
        self.memoryUsageInt[3] = self.TestMemory(function, self.intArray1000)

        self.timeUsageInt[0] = self.TestSpeed(function, self.intArray10)
        self.timeUsageInt[1] = self.TestSpeed(function, self.intArray100)
        self.timeUsageInt[2] = self.TestSpeed(function, self.intArray500)
        self.timeUsageInt[3] = self.TestSpeed(function, self.intArray1000)

        self.memoryUsageFloat[0] = self.TestMemory(function, self.floatArray10)
        self.memoryUsageFloat[1] = self.TestMemory(function, self.floatArray100)
        self.memoryUsageFloat[2] = self.TestMemory(function, self.floatArray500)
        self.memoryUsageFloat[3] = self.TestMemory(function, self.floatArray1000)

        self.timeUsageFloat[0] = self.TestSpeed(function, self.floatArray10)
        self.timeUsageFloat[1] = self.TestSpeed(function, self.floatArray100)
        self.timeUsageFloat[2] = self.TestSpeed(function, self.floatArray500)
        self.timeUsageFloat[3] = self.TestSpeed(function, self.floatArray1000)
