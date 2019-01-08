#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Remove_Nth_Node_From_End_of_List.py
@time: 2019/1/7 17:37
@desc: Given a linked list, remove the n-th node from the end of list and return its head.
Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def removeNthFromEnd(self, head, n):
        """
        [1,2] 2  [2]
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 先用快慢指针得到要移除的节点，保存前后节点
        fast = head
        slow = head
        previous = None
        for i in range(n):
            if fast != None:
                fast = fast.next
            else:
                raise ValueError("n is larger than length of list")
        while fast != None:
            fast = fast.next
            previous = slow
            slow = slow.next
        if previous == None:
            return None
        else:
            previous.next = slow.next
            return head


if __name__ == '__main__':
    solution = Solution()
    node = ListNode(1)
    solution.removeNthFromEnd(node, 1)
