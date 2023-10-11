# сам односвязный список

import random


class LinkedList:

# создание ноды в которой содержется значение и ссылка на следующее значение
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

# init содержит ноду и длинну списка для дальнейшего определения
    def __init__(self):
        self.head = self.Node(None)
        self.len = 0

# вставить переменную в конец списка
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

# показать весь список
    def show(self):
        p = self.head.next
        print('head ', end='')
        while p is not None:
            print('-> %s ' % p.val, end='')
            p = p.next
        print('-> None')

# вставить значение в начало списка
    def push_front(self, val):
        tmp = self.Node(val)
        if self.len == 0:
            self.head.next = tmp
        else:
            tmp.next = self.head.next
            self.head.next = tmp
        self.len += 1

# удалить значание по номеру элемента
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
        

def delling():
    pass


# удалить по значению, и вернуть в место вызова удалённое значение
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

# количество элементов в списке
    def length(self):
        return self.len

# генератор случайного списка
    def generate(self, len):
        for i in range(len):
            self.push_front(random.randint(0, 100))


def main():
    l_test = LinkedList()
    l_test.generate(5)
    l_test.show()


if __name__ == '__main__':
    main()
    