class InsertionSort:
    def __init__(self, arr):
        self.name = "Merge Sort"
        self.array = arr
        self.length = len(arr)
        self.curI = 1
        self.swapCount = 0
        self.comparisons = 0
        self.timePerItem = 0
        self.totalTimeSorting = 0

    def update(self):
        a = 1

    def mergeSort(self, arr, l, r):
        if l >= r:
            return

        m = l + (r - 1 / 2) # find middle element
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m+1, r)
        self.mergeArrays(arr, l, m, r)

    def mergeArrays(self, arr, l, m, r):


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
