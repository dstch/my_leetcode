# Given a non-empty special binary tree consisting of nodes with the non-negativ
# e value, where each node in this tree has exactly two or zero sub-node. If the n
# ode has two sub-nodes, then this node's value is the smaller value among its two
#  sub-nodes. More formally, the property root.val = min(root.left.val, root.right
# .val) always holds. 
# 
#  Given such a binary tree, you need to output the second minimum value in the 
# set made of all the nodes' value in the whole tree. 
# 
#  If no such second minimum value exists, output -1 instead. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest valu
# e.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 25]. 
#  1 <= Node.val <= 231 - 1 
#  root.val == min(root.left.val, root.right.val) for each internal node of the 
# tree. 
#  
#  Related Topics Tree 
#  👍 802 👎 1049


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root.left:
            return -1
        left = self.findSecondMinimumValue(root.left) if root.left.val == root.val else root.left.val
        right = self.findSecondMinimumValue(root.right) if root.right.val == root.val else root.right.val
        return max(left, right) if left == -1 or right == -1 else min(left, right)

# leetcode submit region end(Prohibit modification and deletion)
