# Given the root of a binary tree, return the length of the diameter of the tree
# . 
# 
#  The diameter of a binary tree is the length of the longest path between any t
# wo nodes in a tree. This path may or may not pass through the root. 
# 
#  The length of a path between two nodes is represented by the number of edges 
# between them. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree 
#  👍 4468 👎 280


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        value = 0

        def func(node):
            if node:
                lh = func(node.left)
                rh = func(node.right)
                nonlocal value
                value = max(value, lh + rh)
                return 1 + max(lh, rh)
            else:
                return 0

        func(root)

# leetcode submit region end(Prohibit modification and deletion)
