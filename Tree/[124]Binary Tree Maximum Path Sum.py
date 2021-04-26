# A path in a binary tree is a sequence of nodes where each pair of adjacent nod
# es in the sequence has an edge connecting them. A node can only appear in the se
# quence at most once. Note that the path does not need to pass through the root. 
# 
# 
#  The path sum of a path is the sum of the node's values in the path. 
# 
#  Given the root of a binary tree, return the maximum path sum of any path. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 
# = 42.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3 * 104]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Depth-first Search Recursion 
#  👍 5554 👎 385


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -100000

        def func(node):
            nonlocal res
            if node is None:
                return 0
            left = max(func(node.left), 0)
            right = max(func(node.right), 0)
            res = max(res, node.val + left + right)
            return max(node.val + left, node.val + right)

        func(root)
        return res
# leetcode submit region end(Prohibit modification and deletion)
