# Given the root of a binary tree, return an array of the largest value in each 
# row of the tree (0-indexed). 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3]
# Output: [1,3]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,null,2]
# Output: [1,2]
#  
# 
#  Example 5: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree will be in the range [0, 104]. 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 1251 👎 72


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []

        def func(node, level):
            if node is not None:
                if len(res) == level:
                    res.append([node.val])
                elif res[level][0] < node.val:
                    res[level][0] = node.val
                func(node.left, level + 1)
                func(node.right, level + 1)

        func(root, 0)
        return [x[0] for x in res]
# leetcode submit region end(Prohibit modification and deletion)
