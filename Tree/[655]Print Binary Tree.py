# Print a binary tree in an m*n 2D string array following these rules: 
# 
#  
#  The row number m should be equal to the height of the given binary tree. 
#  The column number n should always be an odd number. 
#  The root node's value (in string format) should be put in the exactly middle 
# of the first row it can be put. The column and the row where the root node belon
# gs will separate the rest space into two parts (left-bottom part and right-botto
# m part). You should print the left subtree in the left-bottom part and print the
#  right subtree in the right-bottom part. The left-bottom part and the right-bott
# om part should have the same size. Even if one subtree is none while the other i
# s not, you don't need to print anything for the none subtree but still need to l
# eave the space as large as that for the other subtree. However, if two subtrees 
# are none, then you don't need to leave space for both of them. 
#  Each unused space should contain an empty string "". 
#  Print the subtrees following the same rules. 
#  
# 
#  Example 1: 
#  
# Input:
#      1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
#  
#  
# 
# 
#  Example 2: 
#  
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
#  
#  
# 
#  Example 3: 
#  
# Input:
#       1
#      / \
#     2   5
#    / 
#   3 
#  / 
# 4 
# Output:
# 
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
#  
#  
# 
#  Note:
# The height of binary tree is in the range of [1, 10].
#  Related Topics Tree 
#  👍 420 👎 970


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))

        def func(node, level, i, j):
            if not node:
                return
            nonlocal w
            if len(res) == level:
                res.append([''] * w)
            res[level][int((i + j) / 2)] = str(node.val)
            func(node.left, level + 1, i, (i + j) / 2)
            func(node.right, level + 1, (i + j) / 2, j)

        res = []
        w = pow(2, getDepth(root)) - 1
        func(root, 0, 0, w)
        return res

# leetcode submit region end(Prohibit modification and deletion)
