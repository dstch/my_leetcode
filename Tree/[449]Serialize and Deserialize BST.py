# Serialization is converting a data structure or object into a sequence of bits
#  so that it can be stored in a file or memory buffer, or transmitted across a ne
# twork connection link to be reconstructed later in the same or another computer 
# environment. 
# 
#  Design an algorithm to serialize and deserialize a binary search tree. There 
# is no restriction on how your serialization/deserialization algorithm should wor
# k. You need to ensure that a binary search tree can be serialized to a string, a
# nd this string can be deserialized to the original tree structure. 
# 
#  The encoded string should be as compact as possible. 
# 
#  
#  Example 1: 
#  Input: root = [2,1,3]
# Output: [2,1,3]
#  Example 2: 
#  Input: root = []
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 104]. 
#  0 <= Node.val <= 104 
#  The input tree is guaranteed to be a binary search tree. 
#  
#  Related Topics Tree 
#  👍 1851 👎 94


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        tree = []

        def func(node):
            if node is None:
                tree.append('#')
            else:
                tree.append(str(node.val))
                func(node.left)
                func(node.right)

        func(root)
        print(tree)
        return ' '.join(tree)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        tree = data.split()[::-1]

        def func():
            if len(tree) > 0:
                val = tree.pop()
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = func()
                root.right = func()
                return root

        return func()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# leetcode submit region end(Prohibit modification and deletion)
