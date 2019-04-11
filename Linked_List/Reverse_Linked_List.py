#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Reverse_Linked_List.py
@time: 2019/4/11 19:09
@desc: Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
from util import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head is not None:
            last = head.next
            head.next = pre
            pre = head
            head = last
        return pre


if __name__ == '__main__':
    head = ListNode.build_linked_list([4, 2, 1, 3])  # ([-1, 5, 3, 4, 0])
    s = Solution()
    print(ListNode.show_linked_list(s.reverseList(head)))
