# Given the root of a Binary Search Tree (BST), return the minimum difference be
# tween the values of any two different nodes in the tree. 
# 
#  Note: This question is the same as 530: https://leetcode.com/problems/minimum
# -absolute-difference-in-bst/ 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [4,2,6,1,3]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 100]. 
#  0 <= Node.val <= 105 
#  
#  Related Topics Tree Depth-first Search Recursion 
#  👍 992 👎 249


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        value = float('inf')

        def func(node):
            if node:
                func(node.left)
                res.append(node.val)
                func(node.right)

        func(root)
        for i in range(1, len(res)):
            if res[i] - res[i - 1] < value:
                value = res[i] - res[i - 1]
        return value
# leetcode submit region end(Prohibit modification and deletion)
