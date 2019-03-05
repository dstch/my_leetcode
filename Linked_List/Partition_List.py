#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Partition_List.py
@time: 2019/3/3 10:57
@desc: Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

from util import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # if head is None or head.next is None:
        #    return head
        temp_head = ListNode(-1)
        temp_head.next = head
        # find the first bigger number position
        cur = head
        prev = temp_head
        while cur is not None:
            if cur.val >= x:
                break
            cur = cur.next
            prev = prev.next
        # find the less number
        cur_2 = cur
        prev_2 = prev
        while cur_2 is not None:
            if cur_2.val < x:
                # move the node position
                prev_2.next = cur_2.next
                prev.next = cur_2
                cur_2.next = cur
                # update all pointer
                prev = cur_2
                cur_2 = prev_2.next
            else:
                cur_2 = cur_2.next
                prev_2 = prev_2.next
        return temp_head.next


if __name__ == '__main__':
    head = ListNode.build_linked_list([1, 1])
    s = Solution()
    result = s.partition(head, 0)
    print(result)
