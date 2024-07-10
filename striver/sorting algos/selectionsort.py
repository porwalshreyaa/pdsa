class Solution:
    def select(self, arr, i):
        l = len(arr)
        mini = i
        for x in range(i,l):
            if arr[x] < arr[mini]:
                mini = x
        return mini
    
    def selectionSort(self, arr,n):
        for i in range(n):
            mini = self.select(arr, i)
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr