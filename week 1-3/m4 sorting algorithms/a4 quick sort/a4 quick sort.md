# Quick Sort

* Choose a pivot element (tipically the first element)
* Partition the list into lower and upper parts with respect to the pivot
* Move the pivot between the lower and upper partition
* Recursively sort the 2 partitions
* This allows an in-place sort
* Iterative implementation is possible to avoid the cost of recursive calls

>An in-place sorting algorithm is a sorting algorithm that sorts the input array in place, without using any additional memory. This means that the algorithm does not need to create a new array to store the sorted elements. In-place sorting algorithms are often used in applications where memory is limited.