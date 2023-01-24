# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def length(self, head):
        count = 0
        while head.next is not None:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, head_a, head_b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        alength = self.length(head_a)
        blength = self.length(head_b)

        if alength > blength:
            start_point = alength - blength
            for i in range(start_point):
                head_a = head_a.next
        if alength < blength:
            start_point = blength - alength
            for i in range(start_point):
                head_b = head_b.next
        if head_a == head_b:
            return head_b

        while head_a.next is not None:

            head_a = head_a.next
            head_b = head_b.next
            if head_a == head_b:
                return head_b
        return None



