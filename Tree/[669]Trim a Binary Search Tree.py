# Given the root of a binary search tree and the lowest and highest boundaries a
# s low and high, trim the tree so that all its elements lies in [low, high]. Trim
# ming the tree should not change the relative structure of the elements that will
#  remain in the tree (i.e., any node's descendant should remain a descendant). It
#  can be proven that there is a unique answer. 
# 
#  Return the root of the trimmed binary search tree. Note that the root may cha
# nge depending on the given bounds. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1], low = 1, high = 2
# Output: [1]
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,null,2], low = 1, high = 3
# Output: [1,null,2]
#  
# 
#  Example 5: 
# 
#  
# Input: root = [1,null,2], low = 2, high = 4
# Output: [2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree in the range [1, 104]. 
#  0 <= Node.val <= 104 
#  The value of each node in the tree is unique. 
#  root is guaranteed to be a valid binary search tree. 
#  0 <= low <= high <= 104 
#  
#  Related Topics Tree Recursion 
#  👍 2744 👎 208


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def func(node):
            if not node:
                return None
            nonlocal low
            nonlocal high
            if low <= node.val <= high:
                node.left = func(node.left)
                node.right = func(node.right)
                return node
            else:
                left = func(node.left)
                right = func(node.right)
                return left if left else right

        return func(root)

# leetcode submit region end(Prohibit modification and deletion)
