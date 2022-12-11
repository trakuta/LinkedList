import random


class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = self.Node(None)
        self.len = 0

    def push_back(self, val):
        tmp = self.Node(val)
        if self.len == 0:
            self.head.next = tmp
        else:
            p = self.head.next
            while p.next is not None:
                p = p.next
            p.next = tmp
        self.len += 1

    def show(self):
        p = self.head.next
        print('head ', end='')
        while p is not None:
            print('-> %s ' % p.val, end='')
            p = p.next
        print('-> None')

    def push_front(self, val):
        tmp = self.Node(val)
        if self.len == 0:
            self.head.next = tmp
        else:
            tmp.next = self.head.next
            self.head.next = tmp
        self.len += 1

    def delete(self, val):
        p = self.head.next
        if p is None:
            return
        elif p.val == val:
            self.head.next = p.next
            self.len -= 1
            return
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
                self.len -= 1
                return
            p = p.next

    def pop(self, pos):
        p = self.head.next
        if self.len <= pos:
            print('unexpected value')
            return
        elif pos == 0:
            poped = p.val
            self.head.next = p.next
            self.len -= 1
            return poped
        for i in range(pos - 1):
            p = p.next
        poped = p.next.val
        p.next = p.next.next
        self.len -= 1
        return poped

    def length(self):
        return self.len

    def generate(self, len):
        for i in range(len):
            self.push_front(random.randint(0, 100))


def main():
    llist = LinkedList()
    llist.push_front(1)
    llist.show()


if __name__ == "__main__":
    main()
