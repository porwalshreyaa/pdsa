# Searching Algorithms

### Linear Search
* Naive Solution
* Check every element in the list one by one
* Worst case is when element is not present in the list

Best Case        |    Average Case   |     Worst Case 
-----------------|-------------------|----------------
`O(1)`           | `O(n)`            | `O(n)`

### Binary Search
* Prerequisite : `List Must Be Sorted!!!`
* Compare with mid point element
* Halve the list till interval becomes empty
* Recurrence : `T(n) = T(n/2) + 1`

Best Case        |    Average Case   |     Worst Case 
-----------------|-------------------|----------------
`O(1)`           | `O(log n)`            | `O(log n)`