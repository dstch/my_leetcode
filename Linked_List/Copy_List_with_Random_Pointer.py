#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Copy_List_with_Random_Pointer.py
@time: 2019/3/20 9:50
@desc: A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

"""


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        temp_head = Node(head.val, None, None)
        node = temp_head
        cur = head.next
        dic = {}
        dic[head] = temp_head
        while cur is not None:
            tmp = Node(cur.val, None, None)
            node.next = tmp
            dic[cur] = tmp
            cur = cur.next
            node = node.next
        cur = head
        node = temp_head
        while cur is not None:
            if cur.random is None:
                node.random = None
            else:
                node.random = dic[cur.random]
            cur = cur.next
            node = node.next
        return temp_head


if __name__ == '__main__':
    head = Node(-1, None, None)
    s = Solution()
    s.copyRandomList(head)
