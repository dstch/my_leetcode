#
# Given the root of a tree, you are asked to find the most frequent subtree sum.
#  The subtree sum of a node is defined as the sum of all the node values formed b
# y the subtree rooted at that node (including the node itself). So what is the mo
# st frequent subtree sum value? If there is a tie, return all the values with the
#  highest frequency in any order.
#  
# 
#  Examples 1 
# Input:
#  
#   5
#  /  \
# 2   -3
#  
# return [2, -3, 4], since all the values happen only once, return all of them i
# n any order.
#  
# 
#  Examples 2 
# Input:
#  
#   5
#  /  \
# 2   -5
#  
# return [2], since 2 happens twice, however -5 only occur once.
#  
# 
#  Note:
# You may assume the sum of values in any subtree is in the range of 32-bit sign
# ed integer.
#  Related Topics Hash Table Tree 
#  👍 840 👎 143


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        dic = {}
        m = 0

        def func(node, m):
            if node is not None:
                m = func(node.left, m)
                m = func(node.right, m)

                s = node.val
                if node.left:
                    s += node.left.val
                if node.right:
                    s += node.right.val
                node.val = s
                if node.val in dic:
                    dic[node.val] += 1
                else:
                    dic[node.val] = 1
                if dic[node.val] > m:
                    m = dic[node.val]
            return m

        m = func(root, m)
        print(dic)
        return [x for x in dic if dic[x] == m]
# leetcode submit region end(Prohibit modification and deletion)
