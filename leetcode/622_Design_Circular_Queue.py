class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """

        self.queue = [None for _ in range(k)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % len(self.queue)
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """

        if self.queue[self.front] is not None:
            self.queue[self.front] = None
            self.front = (self.front + 1) % len(self.queue)
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        return  -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.queue[self.rear -1] is None else self.queue[self.rear -1]

    def isEmpty(self):
        """
        :rtype: bool
        """

        return self.rear == self.front and self.queue[self.front] == None

    def isFull(self):
        """
        :rtype: bool
        """

        return self.rear == self.front and self.queue[self.front] is not None


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # return True
print(myCircularQueue.enQueue(2))  # return True
print(myCircularQueue.enQueue(3))  # return True
print(myCircularQueue.enQueue(4))  # return False
print(myCircularQueue.Rear())  # return 3
print(myCircularQueue.isFull())  # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.enQueue(4))  # return True
print(myCircularQueue.Rear())  # return 4
