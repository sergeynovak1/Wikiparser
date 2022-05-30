def add(tree: tuple, value: int):
    if tree is not None:
        if tree[0] > value:
            return (tree[0], add(tree[1], value), tree[2])
        else:
            return (tree[0], tree[1], add(tree[2], value))
    else:
        return (value, None, None)


def contains(tree: tuple, value: int) -> bool:
    if tree is not None:
        if tree[0] > value:
            return contains(tree[1], value)
        elif tree[0] < value:
            return contains(tree[2], value)
        else:
            return True
    else:
        return False


def tree_lenght(tree: tuple) -> int:
    if tree is not None:
        return 1 + max(tree_lenght(tree[1]), tree_lenght(tree[2]))
    else:
        return 0


class VersionedTree:
    def __init__(self):
        self.list = [None]

    def add(self, value: int) -> None:
        tree = self.list[-1]
        self.list.append(add(tree, value))
        return

    def contains(self, version: int, value: int) -> bool:
        tree = self.list[version - 1]
        return contains(tree, value)

    def height(self, version: int) -> int:
        tree = self.list[version - 1]
        return tree_lenght(tree)



