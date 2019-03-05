#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: util.py
@time: 2019/3/5 11:14
@desc: the common method of linked list solution
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def build_linked_list(l: list):
        head = ListNode(l[0])
        return_head = head
        for n in l[1:]:
            head.next = ListNode(n)
            head = head.next
        return return_head
