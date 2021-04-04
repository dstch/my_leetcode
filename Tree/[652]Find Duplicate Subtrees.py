# Given the root of a binary tree, return all duplicate subtrees. 
# 
#  For each kind of duplicate subtrees, you only need to return the root node of
#  any one of them. 
# 
#  Two trees are duplicate if they have the same structure with the same node va
# lues. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,1]
# Output: [[1]]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the tree will be in the range [1, 10^4] 
#  -200 <= Node.val <= 200 
#  
#  Related Topics Tree 
#  👍 1895 👎 238


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = {}
        result = []

        def func(node):
            if node:
                s = ','.join([str(node.val), func(node.left), func(node.right)])
                if s in res:
                    if res[s] == 1:
                        result.append(node)
                    res[s] += 1
                else:
                    res[s] = 1
                return s
            else:
                return '#'

        func(root)
        return result

# leetcode submit region end(Prohibit modification and deletion)
