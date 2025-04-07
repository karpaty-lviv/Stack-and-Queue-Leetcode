"""Implement Queue using Stacks"""


from queue import LifoQueue


class MyQueue(object):
    """Class implementing queue"""

    def __init__(self):
        self.stack_main = LifoQueue()
        self.stack_second = LifoQueue()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_main.put(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.stack_main.get()


    def peek(self):
        """
        :rtype: int
        """
        while self.stack_main:
            self.stack_second.put(self.stack_main.get())
        first = self.stack_second.get()
        self.stack_second.put(first)
        while self.stack_second:
            self.stack_main.put(self.stack_second.get())
        return first


    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_main.full()


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
