#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Swap_Nodes_in_Pairs.py
@time: 2019/1/15 22:10
@desc: Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
