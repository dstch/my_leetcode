# Given the root of a binary tree and an integer targetSum, return true if the t
# ree has a root-to-leaf path such that adding up all the values along the path eq
# uals targetSum. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3], targetSum = 5
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,2], targetSum = 0
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
#  Related Topics Tree Depth-first Search 
#  👍 2840 👎 582


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        targetSum -= root.val
        if root.left is None and root.right is None:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
# leetcode submit region end(Prohibit modification and deletion)
