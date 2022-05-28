import unittest
from random import *

import src.maps.tree_hash_map as tr


class TestHashMapGet(unittest.TestCase):
    def test_getitem_equel(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_getitem_not_equel(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] + 5
        self.assertNotEqual(val, elem)

    def test_getitem_cnt(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        ex1 = hash.get_cnt()
        elem = hash[key]
        ex2 = hash.get_cnt()
        self.assertEqual(ex1, ex2)

    def test_getitem_include(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        list = hash.get_list()
        for elem in list:
            node = elem.head
            while node:
                if node.element == val:
                    self.assertIs(node.element, val)
                    return 0
                node = node.next_node
        else:
            self.assertIs(list[0].head.element, val)

class TestHashMapSet(unittest.TestCase):
    def test_setitem_equel(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_setitem_notequel(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] - 2
        self.assertNotEqual(val, elem)

    def test_setitem_cnt(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        ex1 = hash.get_cnt()
        hash[key] = val
        ex2 = hash.get_cnt()
        self.assertEqual(ex1, ex2 - 1)

    def test_setitem_include(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        list = hash.get_list()
        for elem in list:
            node = elem.head
            while node:
                if node.element == val:
                    self.assertIs(node.element, val)
                    return 0
                node = node.next_node
        else:
            self.assertIs(list[0].head.element, val)

class TestHashMapDel(unittest.TestCase):
    def test_delitem_notequel(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        hash.__delitem__(key)
        elem = hash[key]
        self.assertNotEqual(val, elem)

    def test_delitem_only_none(self):
        hash = tr.HashMap()
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        hash.__delitem__(key)
        list = hash.get_list()
        for elem in list:
            node = elem.head
            while node:
                node = node.next_node
                raise EOFError
        else:
            self.assertIsNone(list[0].head)

    def test_delitem_notinclude(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        hash.__delitem__(key)
        list = hash.get_list()
        for elem in list:
            node = elem.head
            while node:
                if node.element == val:
                    raise EOFError
                ram = node
                node = node.next_node
        else:
            self.assertIsNot(ram.element, val)

    def test_delitem_cnt(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        ex1 = hash.get_cnt()
        hash.__delitem__(key)
        ex2 = hash.get_cnt()
        self.assertEqual(ex1, ex2 + 1)



class TestTreeMapGet(unittest.TestCase):
    def test_getitem_equel(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_getitem_notequel(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] + 5
        self.assertNotEqual(val, elem)

    def test_getitem_include(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        list = hash.get_list()
        self.assertIn(key, list)

    def test_getitem_size(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        ex1 = len(hash.get_list())
        elem = hash[key]
        ex2 = len(hash.get_list())
        self.assertEqual(ex1, ex2)

class TestTreeMapSet(unittest.TestCase):
    def test_setitem_equel(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_setitem_notequel(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] - 2
        self.assertNotEqual(val, elem)

    def test_setitem_size(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        ex1 = len(hash.get_list())
        hash[key] = val
        ex2 = len(hash.get_list())
        self.assertEqual(ex1, ex2 - 1)

    def test_setitem_include(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        list = hash.get_list()
        self.assertIn(key, list)

class TestTreeMapDel(unittest.TestCase):
    def test_delitem_notequel(self):
        hash = tr.TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        hash.__delitem__(key)
        elem = hash[key]
        self.assertNotEqual(val, elem)

    def test_delitem_only_none(self):
        hash = tr.HashMap()
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        hash.__delitem__(key)
        list = hash.get_list()
        for elem in list:
            node = elem.head
            while node:
                node = node.next_node
                raise EOFError
        else:
            self.assertIsNone(list[0].head)

    def test_delitem_notinclude(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        hash.__delitem__(key)
        list = hash.get_list()
        for elem in list:
            node = elem.head
            while node:
                if node.element == val:
                    raise EOFError
                ram = node
                node = node.next_node
        else:
            self.assertIsNot(ram.element, val)

    def test_delitem_cnt(self):
        hash = tr.HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        ex1 = hash.get_cnt()
        hash.__delitem__(key)
        ex2 = hash.get_cnt()
        self.assertEqual(ex1, ex2 + 1)





