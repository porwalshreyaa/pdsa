# memoizing recursive implementation
# fibbonachi num calculation
def fib(n):
    if n in fibtable.keys():
        return(fibtable[n])
    if n<=1:
        value = n
    else:
        value = fib(n-1) + fib(n-2)
    fibtable[n] = value
    return(value)

#  in general
def f(x,y,x):
    if (x,y,z) in ftable.keys():
        return(ftable[(x,y,z)])
    ##########
    #  recursively compute value from subproblems
    ##########
    f[(x,y,z)] =value
    return(value)

###  dynamic programming
# Anticipate the structure of subproblems
## derive from inductive definitions
## dependencies form a dag
# Solve subproblems in topological order
## Never need to make a recursive call

## memo 
"""
1. store subproblem values in a table
2. look up the table before making a recursive call
"""

## dp
"""
1. solve problems in topological order of dependencies
 >> dependencies must form a DAG (directed acyclic graph)
2. iterative evaluation of subproblems, no recursion
"""