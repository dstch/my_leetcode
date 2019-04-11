#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Remove_Linked_List_Elements.py
@time: 2019/4/11 18:59
@desc: Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

from util import ListNode


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp_head = ListNode(-1)
        temp_head.next = head
        pre = temp_head
        while head is not None:
            if head.val == val:
                pre.next = head.next
                head = pre.next
            else:
                head = head.next
                pre = pre.next
        return temp_head.next
