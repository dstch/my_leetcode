# We are given the head node root of a binary tree, where additionally every nod
# e's value is either a 0 or a 1. 
# 
#  Return the same tree where every subtree (of the given tree) not containing a
#  1 has been removed. 
# 
#  (Recall that the subtree of a node X is X, plus every node that is a descenda
# nt of X.) 
# 
#  
# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
#  
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# 
# 
#  
# 
#  
# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# 
# 
# 
#  
# 
#  
# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
# 
# 
# 
#  
# 
#  Note: 
# 
#  
#  The binary tree will have at most 200 nodes. 
#  The value of each node will only be 0 or 1. 
#  
#  Related Topics Tree 
#  👍 1397 👎 53


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def func(node):
            if not node:
                return None
            node.left = func(node.left)
            node.right = func(node.right)
            if node.val != 1 and not node.left and not node.right:
                return None
            return node

        return func(root)
# leetcode submit region end(Prohibit modification and deletion)
