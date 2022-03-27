CONST_TO_INCREASE = 0.8
'''переменная для увеличения размера массива'''

class LinkedList:
    """односвязный список"""
    head = None
    node = None

    class NodeHash:
        """инициализация элементов"""
        def __init__(self, key, element = None, next_node = None):
            self.element = element
            self.next_node = next_node
            self.key = key

    def append(self, key, element):
        """добавление элементов в конец"""
        if not self.head:
            self.head = self.NodeHash(key, element)
            return element
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.NodeHash(key, element)

    def delkey(self, key):
        """удаление по ключу"""
        if self.head.key == key:
            self.head = self.head.next_node
        else:
            node = self.head
            prev_node = node
            while node.next_node and node.next_node.key != key:
                prev_node = node
                node = node.next_node
            if node.next_node.key == key:
                prev_node = node
                node = node.next_node
                prev_node.next_node = node.next_node

    def __iter__(self):
        """итерация"""
        self.node = self.head
        return self

    def __next__(self):
        """возвращение слудующего"""
        if self.node is not None:
            self.node = self.node.next_node
            return self.node.element
        raise StopIteration

    def __str__(self):
        """вывод в строку"""
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.element))
            node = node.next_node
        return ' -> '.join(values)


class HashMap:
    """Hash-Map"""
    def __init__(self, _size=100):
        """инициализация"""
        self._inner_list = []
        for _ in range(_size):
            self._inner_list.append(LinkedList())
        self._size = _size
        self._cnt = 0

    def __getitem__(self, key):
        """получение"""
        linked_list = self._inner_list[hash(key) % self._size]
        node = linked_list.head
        while node:
            if node.key == key:
                return node.element
            node = node.next_node

    def __setitem__(self, key, value):
        """добавление"""
        self._inner_list[hash(key) % self._size].append(key, value)
        self._cnt += 1
        # увеличиваем массив
        if self._size * CONST_TO_INCREASE >= self._cnt:
            self._size *= 1
            new_inner_list = []
            for _ in range(self._size):
                new_inner_list.append(LinkedList())
            for elem in self._inner_list:
                node = elem.head
                while node:
                    new_inner_list[hash(node.key) % self._size].append(node.key, node.element)
                    node = node.next_node
            self._inner_list = new_inner_list

    def __delitem__(self, key):
        """удаление"""
        self._inner_list[hash(key) % self._size].delkey(key)
        self._cnt -= 1

    def __str__(self):
        """вывод"""
        mas = []
        for index in range(len(self._inner_list)):
            node = self._inner_list[index].head
            values = []
            while node is not None:
                values.append(str(node.element))
                node = node.next_node
            if len(values) == 0:
                mas.append(f'No elements with hash-key "{index}"')
            else:
                first = ' --> '.join(values)
                second = f'Elements with hash-key "{index}" \t'
                mas.append(f'{first} {second}')
        return '\n'.join(map(str, mas))

    @property
    def get_cnt(self):
        """размер"""
        return self._cnt

    @property
    def get_list(self):
        """лист"""
        return self._inner_list


class TreeMap:
    """Tree-Map"""
    root = None
    class NodeTree:
        """инициализация элементов"""
        def __init__(self, key, element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right
            self.key = key

    def __init__(self):
        self.list = []
        self.root = None

    def __getitem__(self, key):
        def getitem(node):
            if node is None:
                raise KeyError
            if key == node.key:
                return node.element
            if key < node.key:
                return getitem(node.left)
            return getitem(node.right)
        return getitem(self.root)

    def __setitem__(self, key, element):
        def setitem(node):
            if node is None:
                self.list.append(key)
                return self.NodeTree(key, element)
            if key == node.key:
                node.element = element
            elif key < node.key:
                node.left = setitem(node.left)
            else:
                node.right = setitem(node.right)
            return node
        self.root = setitem(self.root)

    @staticmethod
    def find_min_node(node):
        """поиск минимального"""
        if node.left is not None:
            return TreeMap.find_min_node(node.left)
        return node

    def __delitem__(self, key):
        def delitem(node, key):
            """удаление по ключу"""
            if node is None:
                raise KeyError
            if key < node.key:
                node.left = delitem(node.left, key)
                return node
            if key > node.key:
                result = delitem(node.right, key)
                node.right = result
                return node
            if node.left is None and node.right is None:
                return None
            if node.left is not None and node.right is None:
                return node.left
            if node.left is None and node.right is not None:
                return node.right
            min_node = TreeMap.find_min_node(node.right)
            node.key = min_node.key
            node.value = min_node.value
            node.right = delitem(node.right, min_node.key)
            return node
        self.root = delitem(self.root, key)

    def __str__(self):
        def return_key(node):
            return f" {node.key}:{node.element} "
        def return_all(node):
            if node is None:
                return ''
            return return_all(node.left) + return_key(node) + return_all(node.right)
        return return_all(self.root)

    @property
    def get_list(self):
        return self.list

