"""Implement Stack using Queues"""


from queue import Queue


class MyStack(object):
    """Class implementing stack"""

    def __init__(self):
        self.queue_main = Queue()
        self.queue_second = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_main.put(x)

    def pop(self):
        """
        :rtype: int
        """
        while self.queue_main.qsize() != 1:
            self.queue_second.put(self.queue_main.get())
        last = self.queue_main.get()
        self.queue_main = self.queue_second
        self.queue_second = Queue()
        return last

    def top(self):
        """
        :rtype: int
        """
        while self.queue_main.qsize() != 1:
            self.queue_second.put(self.queue_main.get())
        last = self.queue_main.get()
        self.queue_second.put(last)
        self.queue_main = self.queue_second
        self.queue_second = Queue()
        return last


    def empty(self):
        """
        :rtype: bool
        """
        return self.queue_main.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
