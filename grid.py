# grid

#           _ _ _ _ _(5,10)
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|         there are many paths to reach from bottom left to top right
#          |_|_|_|_|_|         but you can only move up and right, and not left and down
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#      (0,0)


#  from (0,0) to (m,n) there are exactly m+n moves, m right and n up

# combinatorial solution

# so you have to find positions where you moved up and where you moved right... acc to permutations and combinations... combinations to be prcise as all the up moves are same and all the right moves are same and you needn't arrange them
#  you can either fix up positions or fix right positions ... so select m outta m+n and make combinaions
#  both gives the same result i.e. (m+n)!/m!n!

# BUT, what if there is a big hole somewhere in the mid? and you are not allowed to take that path

# grid

#           _ _ _ _ _(5,10)
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|         there is a hole at (2,4), so you must avoid all the paths that pass through (2,4)
#          |_|_!_|_|_|         
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#          |_|_|_|_|_|
#      (0,0)


# so you need to count all the paths
# that go from [(0,0)to(2,4) x (2,4)to (5,10) ] and minus them from total paths

# what if there are more holes?


# you've to calculate and discard paths seperately thinking of each hole as an independent one
# but if you calculate seperately you while discard some of the paths multiple times... 
# so you'll have to calculate and add them again... 
# remember your lessons from statistics/probability courses... 
# remember that venn diagram thing?? exactly that!

#### This general counting principle is called inclusion-exclusion.
