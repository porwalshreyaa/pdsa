# Merge Sort

* Divide the list into two halves
* Seperately sort the left and the right half
* Combine the two sorted lists A and B to get a fully sorted list C
    * if A is empty, copy B into C
    * if B is empty, copy A into C
    * Otherwise compare first elements of A and B
    * Move the smaller one into C
    * Repeat till you exhaust A and B 
* Recurrence : `T(n) = 2T(n)/2 + n`

