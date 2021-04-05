# Given the root of a Binary Search Tree and a target number k, return true if t
# here exist two elements in the BST such that their sum is equal to the given tar
# get. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = [2,1,3], k = 4
# Output: true
#  
# 
#  Example 4: 
# 
#  
# Input: root = [2,1,3], k = 1
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: root = [2,1,3], k = 3
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  -104 <= Node.val <= 104 
#  root is guaranteed to be a valid binary search tree. 
#  -105 <= k <= 105 
#  
#  Related Topics Tree 
#  👍 1984 👎 151


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []

        def func(node):
            if not node:
                return False
            if node:
                if k - node.val in res:
                    return True
                res.append(node.val)
                return func(node.left) or func(node.right)

        return func(root)

# leetcode submit region end(Prohibit modification and deletion)
