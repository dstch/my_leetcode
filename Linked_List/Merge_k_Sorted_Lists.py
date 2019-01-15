#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Merge_k_Sorted_Lists.py
@time: 2019/1/11 17:01
@desc: Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        return_result = result
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        if l1 == None:
            result.next = l2
        else:
            result.next = l1
        return return_result.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp_list = []
        for node in lists:
            if len(temp_list) < 2:
                temp_list.append(node)
            else:
                temp_node = self.mergeTwoLists(temp_list[0], temp_list[1])
                temp_list.clear()
                temp_list.append(temp_node)
                temp_list.append(node)
        if len(lists) < 1:
            return None
        elif len(lists) == 1:
            return lists[0]
        return self.mergeTwoLists(temp_list[0], temp_list[1])


if __name__ == '__main__':
    ss = Solution()
    ss.mergeKLists([[]])
