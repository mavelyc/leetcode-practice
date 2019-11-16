# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        
        self.helper(root)
        return self.ans
    
    def helper(self, node):
        if not node:
            return False
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        mid = node == self.p or node == self.q
        
        if mid + left + right >= 2:
            self.ans = node
            
        return mid or left or right