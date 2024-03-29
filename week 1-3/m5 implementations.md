# Lists v/s Arrays

Lists                                 | Arrays 
--------------------------------------|---------------
Flexible Length                       | Fixed Size (and fixed type, but python is flexible in this matter)
Values are scattered in memory        | Allocate a contiguous block of memory
Need to follow links to access        | Random Acccess
Insertion and Deletion is easy        | Insertion and deletion is expensive
Swapping elements takes constant time | Swapping elements takes linear time

### Implementation of lists in Python
* Python lists (built-in) are not implemented as flexible linked lists
* underlying interpretation maps the list to an array
    * Assign a fixed block when you create a list 
    * Double the size... if the list overflows the array
* Keep track of the last position of the list in the array
    * l.append() and l.pop() are constant time, ammortized - `O(1)`
    * insertion deletion requires time `O(n)`

* Effectively, Python lists behave more like arrays than lists

### Implementation of Dictionaries in Python
* A dictionary is implemented as a hash table
    > Hash Table is :  An array plus a hash function <br> See  [Hash Table](https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/)
* Creating a good hash function is important (and hard!)
* Need a strategy to deal with collisions
    * Open addressing/closed hashing - probe for free pace in the array
    * Open Hashing - each slot in the hash table points to a list of key-value pairs