"""Maximum Frequency Stack"""

from queue import LifoQueue


class FreqStack:
    """Class implementing frequency stack"""

    def __init__(self):
        self.val_dict = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        freq = self.val_dict.get(val, 0) + 1
        self.val_dict[val] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        if freq not in self.group:
            self.group[freq] = LifoQueue()
        self.group[freq].put(val)

    def pop(self):
        """
        :rtype: int
        """
        stack = self.group[self.max_freq]
        val = stack.get()
        self.val_dict[val] -= 1
        if stack.empty():
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push()
# param_2 = obj.pop()

freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
