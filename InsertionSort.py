import array


class InsertionSort:
    def __init__(self, arr):
        self.name = "Insertion Sort"
        self.array = arr
        self.length = len(arr)
        self.curI = 1
        self.swapCount = 0
        self.comparisons = 0
        self.timePerItem = 0
        self.totalTimeSorting = 0

    def update(self):
        if self.curI == self.length:
            return False
        self.comparisons += 1

        j = self.curI
        while (j > 0) & (self.array[j - 1] > self.array[j]):
            self.swap(j, j-1)
            self.comparisons += 1
            j -= 1

        self.curI += 1
        return True

    def swap(self, one, two):
        temp = self.array[two]
        self.array[two] = self.array[one]
        self.array[one] = temp
        self.swapCount += 1

    def getArray(self):
        return self.array

    def getCurI(self):
        return self.curI

    def getSwaps(self):
        return str(self.swapCount)

    def getComparisons(self):
        return str(self.comparisons)

    def getName(self):
        return self.name
