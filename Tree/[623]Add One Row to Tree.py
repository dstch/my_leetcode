# Given the root of a binary tree and two integers val and depth, add a row of n
# odes with value val at the given depth depth. 
# 
#  Note that the root node is at depth 1. 
# 
#  The adding rule is: 
# 
#  
#  Given the integer depth, for each not null tree node cur at the depth depth -
#  1, create two tree nodes with value val as cur's left subtree root and right su
# btree root. 
#  cur's original left subtree should be the left subtree of the new left subtre
# e root. 
#  cur's original right subtree should be the right subtree of the new right sub
# tree root. 
#  If depth == 1 that means there is no depth depth - 1 at all, then create a tr
# ee node with value val as the new root of the whole original tree, and the origi
# nal tree is the new root's left subtree. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  The depth of the tree is in the range [1, 104]. 
#  -100 <= Node.val <= 100 
#  -105 <= val <= 105 
#  1 <= depth <= the depth of tree + 1 
#  
#  Related Topics Tree 
#  👍 890 👎 161


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:

        def func(node, v, d, dep):
            if node:
                if d == dep:
                    add1_node = TreeNode(v)
                    add1_node.left = node.left
                    node.left = add1_node
                    add2_node = TreeNode(v)
                    add2_node.right = node.right
                    node.right = add2_node
                else:
                    func(node.left, v, d, dep + 1)
                    func(node.right, v, d, dep + 1)

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        func(root, val, depth - 1, 1)
        return root
# leetcode submit region end(Prohibit modification and deletion)
