# очередь реализованная на основе односвязного списка

from llst import LinkedList


class MyQueue:
    def __init__(self):
        self.lined_list = LinkedList()

    def push(self, val):
        self.lined_list.push_back(val)

    def pop(self):
        if self.lined_list.len == 0:
            return None
        return self.lined_list.pop(0)

    def len(self):
        return self.lined_list.len()

    def top(self):
        res = self.pop()
        self.lined_list.push_front(tmp)
        return res
