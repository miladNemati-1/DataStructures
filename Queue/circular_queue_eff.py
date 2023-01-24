class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [None]*k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.tail = (self.tail % (len(self.queue)))
        self.queue[self.tail] = value
        self.tail += 1
        self.size += 1

        return True

    def deQueue(self):
        """
        :rtype: bool
        """

        if self.isEmpty():
            return False
        self.head = (self.head % len(self.queue))
        self.head += 1
        self.size -= 1

        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.head % len(self.queue))]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.tail-1 % len(self.queue))]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.max
