def quicksort(array):
    print('q')
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot]
        more = [i for i in array[1:] if i> pivot]

    return quicksort(less) + [pivot] + quicksort(more)

# def bquick(array):
#     print('b')
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[len(array)//2]
#         less = [i for i in array if i<= pivot]
#         more = [i for i in array if i> pivot]

#     return bquick(less) + bquick(more)
    

print(bquick([4,2,6,3,54,23,54,21,76,8,23,654,97,23,97,54,7,87,8,4,7,1,0]))