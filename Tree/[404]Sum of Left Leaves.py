# Find the sum of all left leaves in a given binary tree. 
# 
#  Example:
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15 respectivel
# y. Return 24.
#  
#  Related Topics Tree 
#  👍 1721 👎 165


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return res
        if root.left is not None and root.left.left is None and root.left.right is None:
            res += root.left.val
        res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res
# leetcode submit region end(Prohibit modification and deletion)
