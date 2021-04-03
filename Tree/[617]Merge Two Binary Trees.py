# You are given two binary trees root1 and root2. 
# 
#  Imagine that when you put one of them to cover the other, some nodes of the t
# wo trees are overlapped while the others are not. You need to merge the two tree
# s into a new binary tree. The merge rule is that if two nodes overlap, then sum 
# node values up as the new value of the merged node. Otherwise, the NOT null node
#  will be used as the node of the new tree. 
# 
#  Return the merged tree. 
# 
#  Note: The merging process must start from the root nodes of both trees. 
# 
#  
#  Example 1: 
# 
#  
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#  
# 
#  Example 2: 
# 
#  
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 2000]. 
#  -104 <= Node.val <= 104 
#  
#  Related Topics Tree 
#  👍 4130 👎 193


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def func(node1, node2):
            if node1 and node2:
                node1.val += node2.val
            elif node2:
                node1 = TreeNode(node2.val)
            else:
                return node1
            node1.left = func(node1.left, node2.left)
            node1.right = func(node1.right, node2.right)
            return node1

        return func(root1, root2)

# leetcode submit region end(Prohibit modification and deletion)
