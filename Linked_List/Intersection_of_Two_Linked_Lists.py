#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Intersection_of_Two_Linked_Lists.py
@time: 2019/4/11 14:50
@desc: Write a program to find the node at which the intersection of two singly linked lists begins.
"""

from util import ListNode


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 先获取链表长度，将长链表后移与短链表长度相同，再一并移动以找到交点
        tempA = headA
        tempB = headB

        def get_len(head):
            n = 0
            while head is not None:
                head = head.next
                n += 1
            return n

        lenA = get_len(tempA)
        lenB = get_len(tempB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next

        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
