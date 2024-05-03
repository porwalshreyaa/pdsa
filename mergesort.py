def mergeSort(A):
    n = len(A)
    if n <=1:
        return A
    print(A[:n//2])
    print(A[n//2:])
    L = mergeSort(A[:n//2])
    R = mergeSort(A[n//2:])
    

    B = merge(L,R)

    return(B)


def merge(A,B):
    print(A)
    print(B)
    (m,n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)
    while k < m+n:
        if i == m:
            C.extend(B[j:])
            k = k + (n-j)
        elif j == n:
            C.extend(A[i:])
            k = k + (m-i)
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i+1, k+1)
        else:
            C.append(B[j])
            (j, k) = (j+1, k+1)
    return C

print(mergeSort([4,2,62,6,3,6,66,89,34,65,366,21,56,35,5]))