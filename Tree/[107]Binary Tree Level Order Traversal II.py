# Given the root of a binary tree, return the bottom-up level order traversal of
#  its nodes' values. (i.e., from left to right, level by level from leaf to root)
# . 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: [[1]]
#  
# 
#  Example 3: 
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
#  The number of nodes in the tree is in the range [0, 2000]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Breadth-first Search 
#  👍 2008 👎 236


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def func(node, level):
            if node is not None:
                if len(res) == level:
                    res.append([])

                res[level].append(node.val)
                func(node.left, level + 1)
                func(node.right, level + 1)

        func(root, 0)
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
