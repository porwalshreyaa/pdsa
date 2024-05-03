def Insertionsort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        #  Assume L[:i] is sorted
        # Move L[:i] to correct position in L
        j = i
        while (j>0 and L[j] < L[j-1]):
            (L[j], L[j-1] ) = (L[j-1], L[j])
            j = j-1
            # now L[:j+1] is sorted

    return(L)


'''
for eg L = [43, 765, 24, 654, 54, 3, 6, 23, 64, 32, 5,31 ,30,323 ,98]

n = len(L) = 15
ie. not n < 1
for i in range(15):
    j = i
    for i = 0
    j= 0
    nothing happens
    for i = 1
    ----while (j>0 and L[j] < L[j-1])--- condition not satisfied
    L[j] = 765 and L[j-1] = 43
    nothng happens
    for i = 2
    L[j] = 24 and L[j-1] = 756
    condition met
    24 < 756 and 2>0
    so 
    L[j], L[j-1] = L[j-1],L[j]-- swap!
    j = j-1 ie j = 1 again
    new ---> L = [43, 24, 765, 654, 54, 3, 6, 23, 64, 32, 5,31 ,30,323 ,98]
    j = 1
    j>0 and L[j] = 24 and L[j-1] = 43
    okay swap again!
    L[j], L[j-1] = L[j-1], L[j]
    new ---> L = [ 24, 43, 765, 654, 54, 3, 6, 23, 64, 32, 5,31 ,30,323 ,98]
    j = 0
    condition not met since j = 0
    next i = 3
    j = 3, j>0
    L[j] = 654 and L[j-1] = 765
    L[j] < L[j-1]
    so swappp!
    L[j], L[j-1] = L[j-1], L[j]
    i = 4
    L[j] = 54, L[j-1]= 756
    swapppp many times again
    new ---> L = [ 24, 43, 54, 654, 765, 3, 6, 23, 64, 32, 5,31 ,30,323 ,98]


and so on...

'''