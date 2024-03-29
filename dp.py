#inductive definations give recursive programs

#insertion sort for instance

def isort(l):
    if l == []:
        return(l)
    else:
        return(insert(isort(l[:-1],l[-1])))
