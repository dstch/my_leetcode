# Given the root of a binary search tree (BST) with duplicates, return all the m
# ode(s) (i.e., the most frequently occurred element) in it. 
# 
#  If the tree has more than one mode, return them in any order. 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than or equal t
# o the node's key. 
#  The right subtree of a node contains only nodes with keys greater than or equ
# al to the node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,null,2,2]
# Output: [2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  -105 <= Node.val <= 105 
#  
# 
#  
# Follow up: Could you do that without using any extra space? (Assume that the i
# mplicit stack space incurred due to recursion does not count). Related Topics Tr
# ee 
#  👍 1263 👎 408


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        dic = {}
        m = 0

        def func(node, m):
            if node is None:
                return m
            if node.val in dic:
                dic[node.val] += 1
            else:
                dic[node.val] = 1
            if dic[node.val] > m:
                m = dic[node.val]
            m = func(node.left, m)
            m = func(node.right, m)
            return m

        m = func(root, m)

        return [x for x in dic if dic[x] == m]

# leetcode submit region end(Prohibit modification and deletion)
