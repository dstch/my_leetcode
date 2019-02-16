#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Reverse Nodes in k-Group.py
@time: 2019/2/16 21:09
@desc: Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not
a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        cur = head
        return_head = head
        while cur is not None:
            cur = self.reverseList(cur, k)
            n = k
            while n > 0 and cur is not None:
                cur = cur.next
                n-=1
        while k>0 and

    def reverseList(self, sub_head: 'ListNode', n: 'int') -> 'ListNode':
        cur = sub_head
        prev = None
        while cur is not None:
            n -= 1
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        if n > 0:
            return sub_head
        else:
            return prev
