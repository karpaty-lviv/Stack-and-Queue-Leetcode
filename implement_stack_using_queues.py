"""Implement Stack using Queues"""


from queue import Queue


class MyStack:
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
        print(self.queue_main.qsize())
        while self.queue_main.qsize() != 1:
            print(self.queue_main.qsize())
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
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)

# stack = MyStack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.top())
