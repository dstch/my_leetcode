#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Linked_List_Cycle_II.py
@time: 2019/3/20 23:47
@desc: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""

from util import ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 记录第一次相遇后，slow走过的距离；
        # 此时，slow走过a+b，fast走过a+b+c+b；
        # fast走过的是slow走过的两倍，有2（a+b）= a+b+c+b
        # 环长度是L=b+c=a+b，即相遇时slow走过的距离
        # 同时，因为a=c，从相遇点和起始点一起出发，相遇的地方即环起始点
        slow = head
        fast = head
        flag = False
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break

        if flag:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            return None
