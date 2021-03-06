# Serialization is the process of converting a data structure or object into a s
# equence of bits so that it can be stored in a file or memory buffer, or transmit
# ted across a network connection link to be reconstructed later in the same or an
# other computer environment. 
# 
#  Design an algorithm to serialize and deserialize a binary tree. There is no r
# estriction on how your serialization/deserialization algorithm should work. You 
# just need to ensure that a binary tree can be serialized to a string and this st
# ring can be deserialized to the original tree structure. 
# 
#  Clarification: The input/output format is the same as how LeetCode serializes
#  a binary tree. You do not necessarily need to follow this format, so please be 
# creative and come up with different approaches yourself. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,2]
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 104]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Design 
#  👍 4208 👎 192


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""

        def func(node):
            nonlocal res
            if not node:
                res += "#|"
            else:
                res += str(node.val) + "|"
                func(node.left)
                func(node.right)

        func(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        index = 0
        data_list = data.split("|")

        def func():
            nonlocal index
            if index < len(data_list):
                if data_list[index] == '#':
                    return None
                node = TreeNode(data_list[index])
                index += 1
                node.left = func()
                index += 1
                node.right = func()
                return node
            return None

        return func()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
