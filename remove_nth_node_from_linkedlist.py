# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""
class Solution(object):
    def length(self, head):
        count = 0
        while head.next is not None:
            count += 1
            head = head.next
        return count

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_to_remove_one_before = head
        node_to_be_next = head

        l = self.length(head)
        steps = l - n
        steps_to_node_to_be_next = l - n + 2

        for i in range(steps):
            node_to_remove_one_before = node_to_remove_one_before.next
        for i in range(steps_to_node_to_be_next):
            node_to_be_next = node_to_be_next.next
        node_to_remove_one_before.next = node_to_be_next

        if l == 0 and n == 1:
            head = None
            return head
        if l + 1 == n:
            head = head.next
            print(head)
            return head
        return head




