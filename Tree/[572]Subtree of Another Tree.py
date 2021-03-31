# Given two non-empty binary trees s and t, check whether tree t has exactly the
#  same structure and node values with a subtree of s. A subtree of s is a tree co
# nsists of a node in s and all of this node's descendants. The tree s could also 
# be considered as a subtree of itself. 
# 
#  Example 1: 
# Given tree s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#  
# Given tree t:
# 
#  
#    4 
#   / \
#  1   2
#  
# Return true, because t has the same structure and node values with a subtree o
# f s.
# 
#  
# 
#  Example 2: 
# Given tree s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#  
# Given tree t:
# 
#  
#    4
#   / \
#  1   2
#  
# Return false.
# 
#  
#  Related Topics Tree 
#  👍 3262 👎 162


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isMatch(ss, tt):
            if ss is None or tt is None:
                return ss is tt
            return (ss.val == tt.val) and isMatch(ss.left, tt.left) and isMatch(ss.right, tt.right)

        if s is None or t is None:
            return s is t
        if isMatch(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
# leetcode submit region end(Prohibit modification and deletion)
