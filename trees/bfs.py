class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from collections import deque

def bfs(root):
    if root is None:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


# Create a simple tree
#       1
#      / \
#     2   3
#    / \ 
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# BFS
print("BFS:", bfs(root))


