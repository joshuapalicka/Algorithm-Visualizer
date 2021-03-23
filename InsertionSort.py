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