"""Realisation of Linked list and HashMap"""
#from src.maps.base_map import BaseMap


class Node:
    """class Node"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class List:
    """class Linked List"""
    def __init__(self):
        self.head = None
        self.length = 0
        self.node = None

    def get_last(self) -> Node:
        "получаем последний элемент"
        if self.length != 0:
            node = self.head
            while node.next is not None:
                node = node.next
            return node
        raise IndexError

    def add_node(self, data) -> None:
        "добавляем элемент в конец"
        self.length += 1
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            self.head = data
        else:
            self.get_last().next = data

    def remove(self, value) -> None:
        "удаляет первый равный value"
        node = self.head
        if node.data == value:
            self.head = self.head.next
            self.length -= 1
            return
        while node.next.next is not None:
            if node.next.data == value:
                node.next = node.next.next
                self.length -= 1
                return
            node = node.next
        if node.next.data == value:
            node.next = node.next.next
            self.length -= 1

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        node = self.node
        if node is None:
            raise StopIteration
        self.node = self.node.next
        return node.data

    def __getitem__(self, item):
        if self.length >= item:
            node = self.head
            i = 0
            while i < item:
                node = node.next
                i += 1
            return node.data
        raise IndexError

    def __setitem__(self, key, value):
        if self.length >= key:
            node = self.head
            i = 0
            while i < key:
                node = node.next
                i += 1
            node.data = value

    def __str__(self):
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.element))
            node = node.next_node
        return ' -> '.join(values)


class HashMap:
    def __init__(self, _size=10):
        self._inner_list = List()
        for _ in range(_size):
            self._inner_list.add_node(List())
        self._size = _size
        self._cnt = 0

    def __getitem__(self, key):
        result = self._inner_list[hash(key) % self._size]
        if result.length == 0:
            raise KeyError
        for i in result:
            if i[0] == key:
                return i[1]
        raise KeyError

    def __setitem__(self, key, value):
        if self._inner_list[hash(key) % self._size].length == 0:
            self._cnt += 1
        flag = True
        for i in range(self._inner_list[hash(key) % self._size].length):
            if self._inner_list[hash(key) % self._size][i][0] == key:
                self._inner_list[hash(key) % self._size][i] = (key, value)
                flag = False
                break
        if flag:
            self._inner_list[hash(key) % self._size].add_node((key, value))
            if self._cnt >= 0.8 * self._size:
                self._size *= 2
                new_inner_list = List()
                for _ in range(self._size):
                    new_inner_list.add_node(List())
                for i in self._inner_list:
                    if i.length != 0:
                        for j in i:
                            new_inner_list[hash(j[0]) % self._size].add_node(j)
                self._inner_list = new_inner_list
                new_cnt = 0
                for i in self._inner_list:
                    if i.length != 0:
                        new_cnt += 1
                self._cnt = new_cnt

    def __delitem__(self, key):
        deleted = self[key]
        self._inner_list[hash(key) % self._size].remove((key, deleted))
        if self._inner_list[hash(key) % self._size].length == 0:
            self._cnt -= 1

    def __len__(self):
        return self.__iter__().length

    def __iter__(self):
        temp = List()
        for i in self._inner_list:
            for j in i:
                temp.add_node(j)
        return temp.__iter__()

    def __bool__(self):
        return len(self) != 0
