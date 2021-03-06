# Given a binary tree, return all root-to-leaf paths. 
# 
#  Note: A leaf is a node with no children. 
# 
#  Example: 
# 
#  
# Input:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#  Related Topics Tree Depth-first Search 
#  👍 2402 👎 127


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def func(node, path):
            if node is None:
                return None
            if node.left is None and node.right is None:
                path += str(node.val)
                res.append(path)
            else:
                path += str(node.val) + '->'
                func(node.left, path)
                func(node.right, path)

        func(root, '')
        return res
# leetcode submit region end(Prohibit modification and deletion)
