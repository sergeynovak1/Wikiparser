
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
        self.size = 0

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
                self.size += 1
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

    def get_list(self):
        return self.list

    def get_size(self):
        return self.size