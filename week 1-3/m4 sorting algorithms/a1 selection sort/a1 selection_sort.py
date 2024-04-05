def SelectionSort(L):
    n = len(L)
    if n<1:
        return(L)
    for i in range(n):
        mpos = i 
        # m = min, pos = position
        for j in range(i+1,n):
            if L[j] < L[mpos]:
                mpos = j
        (L[i], L[mpos]) = (L[mpos], L[i])
    return(L)

print(SelectionSort([30,60,20,13,54,765,3,5,765,57673,5]))