class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.__len__() == 0:
            raise IndexError("Пустой стек, удалить нельзя")
        pop_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return pop_value

    def peek(self):
        if self.__len__() == 0:
            raise IndexError("Пустой стек, смотреть нельзя")
        return self.head.value

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return self.size