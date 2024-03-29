# Analysing an Algorithm
* Running Time (Time complexity)
* Memory Requirement (Space Complexity)

### Time C...
* Running Time `T(n)` is a function of `n`
* Upper Bound on worst case gives us an overall guarantee on performance

### Asymptotic Notations
* Big O : `f(n)` is `O(g(n))`  means that `g(n)` is an upper bound for `f(n)`
* &Omega; : `f(n)` is `O(g(n))`  means that `g(n)` is an lower bound for `f(n)`
* &Theta; : `f(n)` is `O(g(n))`  means we have found matching upper and lower bounds ( ie. Optimal Solution )

### Orders of Magnitude

Notation        | Name           ( increasing order of time )                  
----------------|---------------------------------------
`O(c)`          | Constant      (fastest)              
`O(log log n)`  | Double-Logarithmic                    
`O(log n)`      | Logarithmic                  
<code>O((log n)<sup>c</sup> ), c > 1 </code>    | Poly-Logarithmic             
<code>O((n)<sup>c</sup> ), 0< c< 1 </code>       | Fractional-Power
`O(n)`       | Linear
`O(nlog(n))`       | Log-Linear
<code>O(n<sup>2</sup> ) </code>       | Quadratic    
<code>O(n<sup>c</sup> ) </code>       | Polynomial
<code>O(c<sup>n</sup> ), c>1 </code>       | Exponential    
`O(n!)`       | Factorial   (slowest)

### Calculating Complexity

* Depends on the type of Algorithm
* Iterative programs 
    * Focus on loops
* Recursive programs 
    * Write and solve a Recurrence Relation
