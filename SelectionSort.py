import array

class SelectionSort:
    def __init__(self, arr):
        self.name = "Selection Sort"
        self.array = arr
        self.length = len(arr)
        self.curI = 0
        self.swapCount = 0
        self.comparisons = 0
        self.timePerItem = 0
        self.totalTimeSorting = 0

    def update(self):
        if self.curI == self.length - 1:
            return False
        self.comparisons += 1

        curMin = self.curI
        for j in range(self.curI + 1, self.length):
            self.comparisons += 1
            if self.array[j] < self.array[curMin]:
                curMin = j

        if curMin != self.curI:
            self.swap(self.curI, curMin)
            self.swapCount += 2

        self.comparisons += 1
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
