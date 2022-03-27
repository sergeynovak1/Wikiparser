import unittest
from random import randint

import src.tree_hash_map as tr



class TestHashMapGet(unittest.TestCase):
    """тестирование метода get  в Hash-MAp"""
    def test_getitem_equel(self):
        """тестим get равно"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key]
        self.assertEqual(val, elem)

    def test_getitem_notequel(self):
        """тестим get не равно"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key] + 5
        self.assertNotEqual(val, elem)

    def test_getitem_cnt(self):
        """тестим get размер"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        ex1 = hash_map.get_cnt()
        elem = hash_map[key]
        ex2 = hash_map.get_cnt()
        self.assertEqual(ex1, ex2)

    def test_getitem_include(self):
        """тестим get входит"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        list_test = hash_map.get_list()
        for elem in list_test:
            node = elem.head
            while node:
                if node.element == val:
                    self.assertIs(node.element, val)
                    return 0
                node = node.next_node
        else:
            self.assertIs(list_test[0].head.element, val)

class TestHashMapSet(unittest.TestCase):
    """тестирование метода get  в Hash-MAp"""
    def test_setitem_equel(self):
        """тестим set равно"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key]
        self.assertEqual(val, elem)

    def test_setitem_notequel(self):
        """тестим set не равно"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key] - 2
        self.assertNotEqual(val, elem)

    def test_setitem_cnt(self):
        """тестим set размер"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        ex1 = hash_map.get_cnt()
        hash_map[key] = val
        ex2 = hash_map.get_cnt()
        self.assertEqual(ex1, ex2 - 1)

    def test_setitem_include(self):
        """тестим get входит"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        list_test = hash_map.get_list()
        for elem in list_test:
            node = elem.head
            while node:
                if node.element == val:
                    self.assertIs(node.element, val)
                    return 0
                node = node.next_node
        else:
            self.assertIs(list_test[0].head.element, val)

class TestHashMapDel(unittest.TestCase):
    """тестирование метода del  в Hash-MAp"""
    def test_getitem_equel(self):
        """тестим get не равно"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        hash_map.__delitem__(key)
        elem = hash_map[key]
        self.assertNotEqual(val, elem)

    def test_delitem_only_none(self):
        """тестим удаление только одного"""
        hash_map = tr.HashMap()
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        hash_map.__delitem__(key)
        list_test = hash_map.get_list()
        for elem in list_test:
            node = elem.head
            while node:
                node = node.next_node
                raise EOFError
        else:
            self.assertIsNone(list_test[0].head)

    def test_delitem_notinclude(self):
        """тестим удаленный не состоит"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        hash_map.__delitem__(key)
        list_test = hash_map.get_list()
        for elem in list_test:
            node = elem.head
            while node:
                if node.element == val:
                    raise EOFError
                ram = node
                node = node.next_node
        else:
            self.assertIsNot(ram.element, val)

    def test_delitem_cnt(self):
        """тестим размер удаления"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        ex1 = hash_map.get_cnt()
        hash_map.__delitem__(key)
        ex2 = hash_map.get_cnt()
        self.assertEqual(ex1, ex2 + 1)



class TestTreeMapGet(unittest.TestCase):
    """тестирование метода get  в Tree-MAp"""
    def test_getitem_equel(self):
        """тестим get равно"""
        hash_map = tr.TreeMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key]
        self.assertEqual(val, elem)

    def test_getitem_notequel(self):
        """тестим get не равно"""
        hash_map = tr.TreeMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key] + 5
        self.assertNotEqual(val, elem)

    def test_getitem_include(self):
        """тестим get входит"""
        hash_map = tr.TreeMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        list_test = hash_map.get_list()
        self.assertIn(key, list_test)

    def test_getitem_size(self):
        """тестим get размер"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        ex1 = hash_map.get_cnt()
        elem = hash_map[key]
        ex2 = hash_map.get_cnt()
        self.assertEqual(ex1, ex2)

class TestTreeMapSet(unittest.TestCase):
    """тестирование метода get  в Hash-MAp"""
    def test_setitem_equel(self):
        """тестим set равно"""
        hash_map = tr.TreeMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key]
        self.assertEqual(val, elem)

    def test_setitem_notequel(self):
        """тестим set не равно"""
        hash_map = tr.TreeMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        elem = hash_map[key] - 2
        self.assertNotEqual(val, elem)

    def test_setitem_size(self):
        """тестим set размер"""
        hash_map = tr.TreeMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        ex1 = hash_map.get_cnt()
        hash_map[key] = val
        ex2 = hash_map.get_cnt()
        self.assertEqual(ex1, ex2 - 1)

    def test_setitem_include(self):
        """тестим get входит"""
        hash_map = tr.HashMap()
        for _ in range(randint(1, 20)):
            hash_map[randint(1, 1000)] = randint(1, 1000)
        key = randint(1, 1000)
        val = randint(1, 1000)
        hash_map[key] = val
        list_test = hash_map.get_list()
        self.assertIn(key, list_test)





