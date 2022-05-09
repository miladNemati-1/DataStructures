class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def length(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    def get(self, index):

        if self.head is None or index >= self.length():
            return -1

        node = self.head
        for i in range(index):
            node = node.next

        return node.value

    def addAtHead(self, val):

        if self.head is not None:
            curr = Node(val)
            curr.next = self.head
            self.head = curr
        else:
            self.head = Node(val)

    def addAtTail(self, val):
        if self.head is None:
            node = Node(val)
            self.head = node
            return
        curr = Node(val)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = curr

    def addAtIndex(self, index, val):

        if index > self.length():
            return

        if index == 0 and self.head is None:
            node = Node(val)
            self.head = node
            return

        if index == 0:
            node = Node(val)
            node.next = self.head
            self.head = node
            return

        if self.head is None:
            return

        curr = Node(val)
        node = self.head
        prev = None
        for i in range(index):
            prev = node
            node = node.next
        curr.next = node
        prev.next = curr

    def deleteAtIndex(self, index):

        if index >= self.length():
            return

        if index == 0 and self.head.next is None:
            self.head = None
            return

        if index == 0:
            self.head = self.head.next
            return

        node = self.head
        prev = None
        for i in range(index):
            prev = node
            node = node.next
        prev.next = node.next



