# Comparing sorting algorithms

Parameter  | Selection Sort | Insertion Sort | Merge Sort | Quick Sort
-----------|----------------|----------------|------------|----------------------
Best Case  | <code>O(n<sup>2</sup>)</code> | <code>O(n)</code> | <code>O(n log n)</code> | <code>O(n log n)</code> 
Average Case  | <code>O(n<sup>2</sup>)</code> | <code>O(n<sup>2</sup>)</code> | <code>O(n log n)</code> | <code>O(n log n)</code> 
Worst Case  | <code>O(n<sup>2</sup>)</code> | <code>O(n<sup>2</sup>)</code> | <code>O(n log n)</code> | <code>O(n<sup>2</sup>)</code>
In-place  | Yes | Yes | No | Yes
Stable  | No | Yes | Yes | No

> An in-place sorting algorithm is a sorting algorithm that sorts the input array in place, without using any additional memory. This means that the algorithm does not need to create a new array to store the sorted elements. In-place sorting algorithms are often used in applications where memory is limited.