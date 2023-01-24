"""
  Design Circular Queue

Solution
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4


"""


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [None]*k
        self.head = 0
        self.tail = 0

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

        return True

    def deQueue(self):
        """
        :rtype: bool
        """

        if self.isEmpty():
            return False
        self.head = (self.head % len(self.queue))
        self.queue[self.head] = None
        self.head += 1

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
        if self.head == self.tail and self.queue[(self.head % len(self.queue))] == None and self.queue[(self.tail % len(self.queue))] == None:
            self.tail = 0
            self.head = 0
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        return (self.tail % len(self.queue)) == self.head


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(2)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_7 = obj.deQueue()
param_1 = obj.enQueue(3)
param_7 = obj.deQueue()
param_1 = obj.enQueue(3)
param_7 = obj.deQueue()
param_1 = obj.enQueue(3)
param_7 = obj.deQueue()
param_7 = obj.Front()


print(param_1)
