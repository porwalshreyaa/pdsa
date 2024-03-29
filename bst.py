########################### basic search tree ###########################
class Tree:
    def __init__(self, initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return
    
    def isempty(self):
        return (self.value == None)
    
    def isleaf(self):
        return (self.value != None and self.left.isempty() and self.right.isempty())
        
   # inorder traversal----- 1 = this value, 2 = left tree, 3 = right tree
    def inorder(self):
        # inorder = 213, postorder = 231, preorder = 123
        if self.isempty():
            return([])
        else:
            return( self.left.inorder() + [self.value] + self.right.inorder())
    
    def __str__(self):
        return(str(self.inorder()))
        
   # check if the value v occurs in the tree
    def find(self, v):
        if self.isempty():
            return(False)
        if self.value == v:
            return(True)
        if v < self.value:
            return(self.left.find(v))
        if v > self.value:
            return(self.right.find(v))
            
   # finding minimum values in the tree
    def minval(self):
        if self.left.isempty():
            return(self.value)
        else:
            return(self.left.minval())
    def maxval(self):   # finding maximum values in the tree
        if self.right.isempty():
            return(self.value)
        else:
            return(self.right.maxval())
            
   # insert a value
    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            return
        if v > self.value:
            self.right.insert(v)
            return
    # delete a node
    def delete(self, v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            elif self.right.isempty():
                self.copyleft()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return
    # convert leaf node to empty 
    def makeempty(self):
        self.value = None
        self.right = None
        self.left = None
        return
    # promote left child
    def copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left = self.left.left
        return
    # promote right child
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return
        

# complexity
# find(), insert() and delete() all walk down a single path
# worst case: height of the tree
# unbalanced tree with n nodes may have height O(n)
# balanced trees have height O(log n)
        
########################### Balanced search trees ###########################


    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right
        
        newleft = Tree(v)
        newleft.left = tl
        newleft.right = trl
        
        self.value = vr
        self.right = trr
        self.left = newleft
        return
    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tr = self.right
        tlr = self.left.right
        tll = self.left.left
        
        newright = Tree(v)
        newright.left = tlr
        newright.right = tr
        
        self.value = vl
        self.left = tll
        self.right = newright
        return
   # insert a value
    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            # new step introduced...
            self.left.rebalance()
            return
        if v > self.value:
            self.right.insert(v)
            self.right.rebalance()
            return
    
    # rebalance
    def rebalance(self):
        
