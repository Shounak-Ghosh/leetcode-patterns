class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_preorder(root):
    if root is None:
        return []
    
    result = [root.value]
    result += dfs_preorder(root.left)
    result += dfs_preorder(root.right)
    
    return result

def dfs_inorder(root):
    if root is None:
        return []
    
    result = dfs_inorder(root.left)
    result.append(root.value)
    result += dfs_inorder(root.right)
    
    return result

def dfs_postorder(root):
    if root is None:
        return []
    
    result = dfs_postorder(root.left)
    result += dfs_postorder(root.right)
    result.append(root.value)
    
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

# DFS Preorder
print("DFS Preorder:", dfs_preorder(root))

# DFS Inorder
print("DFS Inorder:", dfs_inorder(root))

# DFS Postorder
print("DFS Postorder:", dfs_postorder(root))

