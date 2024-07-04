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
    def __init__(self,key=0,left=0,right=0):
        self.data = key
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) ==0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None


def LevelOrderTraversal(root):
    if root is None:
        return []
    result= []
    queue = Queue()
    queue.enqueue(root)
    queue.enqueue(None)

    current_level = []

    while not queue.is_empty():

        node = queue.dequeue()
        if node:
            current_level.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        else:
            result.append(current_level)
            current_level = []
            if not queue.is_empty():
                queue.enqueue(None)
    return result 