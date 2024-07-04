"""
link to my notes on doc:

"""


# dfs traversal 
#preorder


#inorder


#postorder




#bfs traversal 

#level order traversal - queue
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def LevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while(len(queue)>0):
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)