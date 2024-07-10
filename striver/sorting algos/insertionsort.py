class Solution:
    def insert(self, alist, index):
        current_value = alist[index]
        position = index
        
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1
        
        alist[position] = current_value
        
    def insertionSort(self, alist, n):
        for i in range(1, n):
            self.insert(alist, i)
        return alist
