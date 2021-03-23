import array


class BubbleSort:
    def __init__(self, arr, leng, algInt):
        self.name = "Bubble Sort"
        self.algType = algInt
        self.array = arr
        self.length = leng
        self.curI = 0
        self.swapCount = 0
        self.comparisons = 0
        self.timePerItem = 0
        self.totalTimeSorting = 0

    def update(self):
        if self.curI == self.length - 1:
            return False
        self.comparisons += 1

        for j in range(self.length - 1):
            if self.array[j] > self.array[j + 1]:
                temp = self.array[j + 1]
                self.array[j + 1] = self.array[j]
                self.array[j] = temp
                self.swapCount += 2
            self.comparisons += 1

        self.curI += 1
        return True

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
