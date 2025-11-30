class Node:
    """Узел связного списка для стека"""
    def __init__(self, value):
        self.value = value  # Значение узла
        self.next = None    # Ссылка на следующий узел


class Stack:
    """Реализация стека на связном списке"""
    def __init__(self):
        self.head = None  # Вершина стека
        self.size = 0     # Счетчик элементов

    def push(self, item):
        """Добавление элемента на вершину стека"""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        """Удаление и возврат элемента с вершины стека"""
        if self.__len__() == 0:
            raise IndexError("Пустой стек, удалить нельзя")
        pop_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return pop_value

    def peek(self):
        """Просмотр элемента на вершине стека без удаления"""
        if self.__len__() == 0:
            raise IndexError("Пустой стек, смотреть нельзя")
        return self.head.value

    def is_empty(self):
        """Проверка стека на пустоту"""
        return self.__len__() == 0

    def __len__(self):
        """Возвращает количество элементов в стеке"""
        return self.size