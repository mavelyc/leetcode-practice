# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.ans = 1
        
        self.helper(root)
        
        return self.ans
        
    def helper(self, node):
        if not node:
            return 0
        
        L = self.helper(node.left)
        R = self.helper(node.right)
        
        self.ans = max(self.ans, L+R)
        
        return max(L + 1, R + 1)
        