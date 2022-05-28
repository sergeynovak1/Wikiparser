import unittest
from random import *

from src.maps.hash_map import HashMap
from src.maps.tree_map import TreeMap


class TestHashMapGet(unittest.TestCase):
    def test_getitem_equel(self):
        hash = HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_getitem_not_equel(self):
        hash = HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] + 5
        self.assertNotEqual(val, elem)

    def test_getitem_cnt(self):
        hash = HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        ex1 = hash.get_cnt()
        elem = hash[key]
        ex2 = hash.get_cnt()
        self.assertEqual(ex1, ex2)


class TestHashMapSet(unittest.TestCase):
    def test_setitem_equel(self):
        hash = HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_setitem_notequel(self):
        hash = HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] - 2
        self.assertNotEqual(val, elem)

    def test_setitem_cnt(self):
        hash = HashMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        ex1 = hash.get_cnt()
        hash[key] = val
        ex2 = hash.get_cnt()
        self.assertEqual(ex1, ex2 - 1)


class TestTreeMapGet(unittest.TestCase):
    def test_getitem_equel(self):
        tree = TreeMap()
        for i in range(randint(1, 20)):
            tree[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        tree[key] = val
        elem = tree[key]
        self.assertEqual(val, elem)

    def test_getitem_notequel(self):
        hash = TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] + 5
        self.assertNotEqual(val, elem)

    def test_getitem_size(self):
        hash = TreeMap()
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
        hash = TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key]
        self.assertEqual(val, elem)

    def test_setitem_notequel(self):
        hash = TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        elem = hash[key] - 2
        self.assertNotEqual(val, elem)

    def test_setitem_size(self):
        hash = TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        ex1 = len(hash.get_list())
        hash[key] = val
        ex2 = len(hash.get_list())
        self.assertEqual(ex1, ex2 - 1)

    def test_setitem_include(self):
        hash = TreeMap()
        for i in range(randint(1, 20)):
            hash[randint(1, 1000)] = randint(1, 1000)
        key = randint(1000, 10000)
        val = randint(1000, 10000)
        hash[key] = val
        list = hash.get_list()
        self.assertIn(key, list)
