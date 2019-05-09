#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Flatten_a_Multilevel_Doubly_Linked_List.py
@time: 2019/5/8 19:24
@desc: You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        temp_head = Node(-1, None, head, None)
        cur = head
        node_list = []
        while cur.next is not None:
            if cur.child is not None:
                tmp = cur.child
                cur.child = None
                tmp.prev = None
                node_list.append(tmp)
            cur = cur.next
        for tmp in node_list[::-1]:
            cur.next = tmp
            while cur.next is not None:
                cur = cur.next
        return temp_head.next
