#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Add_Two_Numbers_II.py
@time: 2019/8/13 9:55
@desc: You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""
from util import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = ''
        l = l1
        while l:
            s1 += str(l.val)
            l = l.next
        l = l2
        while l:
            s2 += str(l.val)
            l = l.next
        s1 = int(s1)
        s2 = int(s2)
        s = str(s1 + s2)
        l = ListNode(-1)
        p = l
        for w in s:
            p.next = ListNode(int(w))
            p = p.next
        return l.next
