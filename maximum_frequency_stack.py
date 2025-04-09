"""Maximum Frequency Stack"""

from queue import LifoQueue


class FreqStack:
    """Class implementing frequency stack"""

    def __init__(self):
        self.main_stack = LifoQueue()
        self.second_stack = LifoQueue()
        self.val_dict = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.val_dict:
            self.val_dict[val] += 1
        else:
            self.val_dict[val] = 1
        self.main_stack.put(val)

    def pop(self):
        """
        :rtype: int
        """
        freq_dict = {}
        for key, val in self.val_dict.items():
            if val in freq_dict:
                freq_dict[val].append(key)
            else:
                freq_dict[val] = [key]
        max_freq = max(list(freq_dict.keys()))
        while True:
            elem = self.main_stack.get()
            if elem in freq_dict[max_freq]:
                while not self.second_stack.empty():
                    self.main_stack.put(self.second_stack.get())
                return elem
            else:
                self.second_stack.put(elem)



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
