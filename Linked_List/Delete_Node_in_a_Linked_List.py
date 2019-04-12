#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Delete_Node_in_a_Linked_List.py
@time: 2019/4/12 20:32
@desc: Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
"""

from util import ListNode


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = None
        while node.next is not None:
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None
