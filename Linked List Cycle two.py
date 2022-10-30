"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return

        sp = head
        fp = head
        while head.next is not None:
            sp = sp.next
            if sp is None:
                return
            fp = fp.next
            if fp is None:
                return
            fp = fp.next
            if fp is None:
                return
            if fp == sp:
                left = head
                while left != sp:
                    sp = fp.next
                    while sp != fp:
                        if sp == left:
                            return left
                        sp = sp.next
                    left = left.next
                return left

        return










