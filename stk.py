from llst import LinkedList


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, val):
        self.linked_list.push_front(val)

    def pop(self):
        if self.linked_list.len == 0:
            return None
        return self.linked_list.pop(0)

    def show(self):
        self.linked_list.show()

    def top(self):
        tmp = self.pop()
        self.push(tmp)
        return tmp
