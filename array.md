# Declaration of Array:
    
    import array  

    arr = array.array('i')     # This array will store integer type element

    arr = array.array('b')     # This array will store char type element

    arr = array.array('f')     # This array will store float type element




# Initialization of Array:

    import array

    arr = array.array('i', [1, 2, 3, 4, 5])     # This array will store integer type element

    arr = array.array('b', [])                  # This array will store char type element

    arr = array.array('f')                      # This array will store float type element



# Static Array

    import array

    arr = array.array('i', [1, 2, 3, 4, 5])



# Dynamic Array

    arr = []


# Traversing over arr[]

    import array
    arr = array.array('i', [1, 2, 3, 4, 5])     # Traversing over arr[]

    for x in arr:
        print(x, end=" ")


# Insertion in Array:

    def insertElement(arr, n, x, pos):
        # shift elements to the right
        # which are on the right side of pos
        for i in range(n-1, pos-1, -1):
            arr[i + 1] = arr[i]

        arr[pos] = x

# Deletion in Array:

    from array import array

    # Function to search for a key in the array

    def findElement(arr, n, key):
        for i in range(n):
              # Return the index if key is found
            if arr[i] == key:
                return i
        # Return -1 if key is not found
        return -1  

    # Function to delete an element from the array

    def deleteElement(arr, n, key):
        # Find position of element to be deleted
        pos = findElement(arr, n, key)
        if pos == -1:
            print("Element not found")
            return n

        # Deleting element
        for i in range(pos, n - 1):
            arr[i] = arr[i + 1]

        return n - 1
  
# Searching in Array:

    # unsorted array

    def findElement(arr, n, key):
        for i in range(n):
            if (arr[i] == key):
                return i
        # If the key is not found
        return -1