# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        self.dfs(root, sum)
        
        return self.count
        
    def helper(self, node, path_sum, ref):
        path_sum+=node.val
        if path_sum == ref: self.count+=1 
        if not node.right and not node.left:
            return
        if node.right:
            self.helper(node.right, path_sum, ref)
        if node.left:
            self.helper(node.left, path_sum, ref)
            
    def dfs(self, node, ref):
        if not node:
            return self.count
        
        self.helper(node, 0, ref)
        self.dfs(node.left, ref)
        self.dfs(node.right, ref)
    