# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums)
        
    def construct(self, nums):
        max_i = nums.index(max(nums))
        root = TreeNode(nums[max_i])
        if len(nums[max_i+1:]) > 0:
            root.right = self.construct(nums[max_i+1:])
        if len(nums[:max_i]) > 0:
            root.left = self.construct(nums[:max_i])
        return root