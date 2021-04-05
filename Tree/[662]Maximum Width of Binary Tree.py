# Given a binary tree, write a function to get the maximum width of the given tr
# ee. The maximum width of a tree is the maximum width among all levels. 
# 
#  The width of one level is defined as the length between the end-nodes (the le
# ftmost and right most non-null nodes in the level, where the null nodes between 
# the end-nodes are also counted into the length calculation. 
# 
#  It is guaranteed that the answer will in the range of 32-bit signed integer. 
# 
# 
#  Example 1: 
# 
#  
# Input: 
# 
#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 
# 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (
# 5,3,null,9).
#  
# 
#  Example 2: 
# 
#  
# Input: 
# 
#           1
#          /  
#         3    
#        / \       
#       5   3     
# 
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (
# 5,3).
#  
# 
#  Example 3: 
# 
#  
# Input: 
# 
#           1
#          / \
#         3   2 
#        /        
#       5      
# 
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 
# (3,2).
#  
# 
#  Example 4: 
# 
#  
# Input: 
# 
#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (
# 6,null,null,null,null,null,null,7).
#  
# 
#  
#  Constraints: 
# 
#  
#  The given binary tree will have between 1 and 3000 nodes. 
#  
#  Related Topics Tree 
#  👍 2131 👎 380


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = []
        result = 0

        def func(node, level, index):
            if node:
                nonlocal result
                if len(res) == level:
                    res.append([])
                res[level].append(index)
                func(node.left, level + 1, index * 2)
                func(node.right, level + 1, index * 2 + 1)
                temp = res[level][-1] - res[level][0] + 1
                if temp > result:
                    result = temp

        func(root, 0, 1)
        return result

# leetcode submit region end(Prohibit modification and deletion)
