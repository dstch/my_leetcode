# Given the root of a binary tree and an integer targetSum, return all root-to-l
# eaf paths where each path's sum equals targetSum. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3], targetSum = 5
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,2], targetSum = 0
# Output: []
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
#  👍 2545 👎 85


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, cur_sum, result_list):
            if node.left is None and node.right is None:
                if cur_sum == targetSum:
                    res.append(result_list)
            if node.left is not None:
                dfs(node.left, cur_sum + node.left.val, result_list + [node.left.val])
            if node.right is not None:
                dfs(node.right, cur_sum + node.right.val, result_list + [node.right.val])

        res = []
        if root is not None:
            dfs(root, root.val, [root.val])
        return res
# leetcode submit region end(Prohibit modification and deletion)
