# Given the root of a binary tree, return the leftmost value in the last row of 
# the tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [2,1,3]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 1275 👎 169


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = []

        def func(node, level):
            if node is not None:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                func(node.left, level + 1)
                func(node.right, level + 1)

        func(root, 0)
        return res[-1][0]
# leetcode submit region end(Prohibit modification and deletion)
