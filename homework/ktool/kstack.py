class kstack():
    def __init__(self):
        self.stack = list()

    def push(self, element):
        self.stack.append(element)
        return self.stack

    def pop(self):
        if len(self.stack) != 0:
            pop_element = self.stack[-1]
            del self.stack[-1]
            return pop_element
        else:
            return None

    def size(self):
        return len(self.stack)
    
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None
