#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Rotate_List.py
@time: 2019/3/1 16:46
@desc: Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        cur = head
        # get the length of list
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        times = k % length
        cur = head
        for i in range(times):
            while cur.next.next is not None:
                cur = cur.next
            prev = cur
            cur = cur.next
            prev.next = cur.next
            cur.next = head
            head = cur
        return cur


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    s = Solution()
    s.rotateRight(head, 1)
