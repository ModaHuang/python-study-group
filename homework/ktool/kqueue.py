class kqueue():
    def __init__(self):
        self.queue = list()

    def push(self, element):
        self.queue.append(element)
        return self.queue

    def pop(self):
        if len(self.queue) != 0:
            pop_element = self.queue[0]
            del self.queue[0]
            return pop_element
        else:
            return None

    def size(self):
        return len(self.queue)

    def front(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return None

    def back(self):
        if len(self.queue) != 0:
            return self.queue[-1]
        else:
            return None
