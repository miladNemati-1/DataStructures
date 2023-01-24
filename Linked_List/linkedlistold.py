class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None


    def get(self, index):

        if self.head is None or index > self.length():
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
        firstNode = self.head
        while firstNode.next != None:
            firstNode = firstNode.next
        firstNode.next = curr

    def addAtIndex(self, index, val):

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
        count = 0
        fNode = self.head
        while fNode is not None:
            fNode = fNode.next
            count += 1
        if index == count:
            curr = Node(val)
            node = self.head
            for i in range(index):
                node = node.next
            curr.next = node
            prev = self.head
            for i in range(index - 1):
                prev = prev.next
            prev.next = curr
            return
        curr = Node(val)
        node = self.head
        for i in range(index):
            if node.next is None:
                return
            node = node.next
        curr.next = node
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        prev.next = curr

    def deleteAtIndex(self, index):

        if index == 0 and self.head.next is None:
            self.head = None
            return
        if index == 0:
            self.head = self.head.next
            return
        node = self.head
        for i in range(index):
            if node.next is None:
                return
            node = node.next
        prev = self.head
        for i in range(index - 1):
            if prev.next is None:
                return
            prev = prev.next
        prev.next = node.next

    # Your MyLinkedList object will be instantiated and called as such:


obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(2)
obj.addAtHead(3)
print(obj.length())
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
