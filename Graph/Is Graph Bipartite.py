#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Is Graph Bipartite.py
@time: 2019/9/12 9:32
@desc: Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

"""


class Solution(object):
    # graph：[[1,3], [0,2], [1,3], [0,2]] 代表每个点与哪个点连接，比如第一个[1,3]代表第0点跟1和3连接。
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        c = [0 for x in range(len(graph))]
        for index, gj in enumerate(graph):
            if c[index] != 0:
                continue
            c[index] = 1
            s = [index]
            while len(s) != 0:
                p = s[0]
                s.pop(0)
                g = graph[p]
                for gi in g:
                    if c[gi] == c[p]:
                        return False
                    if c[gi] == 0:
                        c[gi] = -c[p]
                        s.append(gi)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isBipartite(
        [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]]
    ))
