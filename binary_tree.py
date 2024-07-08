"""
link to my notes on doc:

"""


# dfs traversal 
#preorder


#inorder


#postorder




#bfs traversal 

#level order traversal - queue

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        return ans
