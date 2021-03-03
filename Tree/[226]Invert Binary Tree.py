# Invert a binary tree. 
# 
#  Example: 
# 
#  Input: 
# 
#  
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  Output: 
# 
#  
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  Trivia: 
# This problem was inspired by this original tweet by Max Howell: 
# 
#  Google: 90% of our engineers use the software you wrote (Homebrew), but you c
# an’t invert a binary tree on a whiteboard so f*** off. 
#  Related Topics Tree 
#  👍 4815 👎 71


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def func(node):
            if node is None:
                return node
            func(node.left)
            func(node.right)

            node.left, node.right = node.right, node.left
            return node

        node = root
        func(node)
        return root

# leetcode submit region end(Prohibit modification and deletion)
