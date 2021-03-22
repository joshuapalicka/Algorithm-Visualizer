import array

class SelectionSort:
    def __init__(self, arr, leng, algInt):
        self.name = "Selection Sort"
        self.algType = algInt
        self.array = arr
        self.length = leng
        self.curI = 0
        self.swapCount = 0
        self.comparisons = 0

    def update(self):
        if self.curI == self.length - 1:
            return False

        curMin = self.curI
        for j in range(self.curI + 1, self.length):
            if self.array[j] < self.array[curMin]:
                curMin = j

                self.comparisons += 1

        if curMin != self.curI:
            self.comparisons += 1
            temp = self.array[curMin]
            self.array[curMin] = self.array[self.curI]
            self.array[self.curI] = temp

            self.swapCount += 2

        self.curI += 1
        return True

    def getArray(self):
        return self.array

    def getSwaps(self):
        return str(self.swapCount)

    def getComparisons(self):
        return str(self.comparisons)

    def getName(self):
        return self.name
