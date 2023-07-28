import unittest
from typing import List
from ordered_list import Node, OrderedList, OrderedStringList

def extract_values(nodes_list : List[Node]):
    values = []
    for node in nodes_list:
        values.append(node.value)
    return values

class TestOrderedList(unittest.TestCase):

    def test_init_increasing(self):
        inc_ord_list = OrderedList(True)
        self.assertEqual(inc_ord_list.len(), 0)
        self.assertEqual(inc_ord_list.get_all(), [])
        self.assertIsNone(inc_ord_list.find(1))
        
        #inc_ord_list.add(1)
        inc_ord_list.delete(1)
        inc_ord_list.clean(True)
        #inc_ord_list.clean(False)
        
    def test_init_decreasing(self):
        dec_ord_list = OrderedList(False)
        self.assertEqual(dec_ord_list.len(), 0)
        self.assertEqual(dec_ord_list.get_all(), [])
        self.assertIsNone(dec_ord_list.find(1))
   
    def test_add_increasing(self):
        ord_list = OrderedList(True)
        for v in [3, 6, 1, 8, 42, -100, 0, 0]:
            ord_list.add(v)
        self.assertEqual(ord_list.len(), 8)
        self.assertEqual(extract_values(ord_list.get_all()), [-100, 0, 0, 1, 3, 6, 8, 42])
    
    def test_add_decreasing(self):
        ord_list = OrderedList(False)
        for v in [3, 6, 1, 8, 42, -100, 0, 0]:
            ord_list.add(v)
        self.assertEqual(ord_list.len(), 8)
        self.assertEqual(extract_values(ord_list.get_all()), [42, 8, 6, 3, 1, 0, 0, -100])

    def test_find_increasing(self):
        ord_list = OrderedList(True)
        for v in [3, 6, 1, 8, 42, -100, 0, 0]:
            ord_list.add(v)
        finded_node = ord_list.find(0)
        self.assertIsNotNone(finded_node)
        self.assertEqual(finded_node.value, 0)
        self.assertEqual(finded_node.next.value, 0)
        self.assertEqual(finded_node.prev.value, -100)
        
        finded_node = ord_list.find(-100)
        self.assertIsNotNone(finded_node)
        self.assertEqual(finded_node.value, -100)
        self.assertEqual(finded_node.next.value, 0)
        self.assertIsNone(finded_node.prev)
        
        finded_node = ord_list.find(42)
        self.assertIsNotNone(finded_node)
        self.assertEqual(finded_node.value, 42)
        self.assertIsNone(finded_node.next)
        self.assertEqual(finded_node.prev.value, 8)
        
        self.assertIsNone(ord_list.find(-1000))
        self.assertIsNone(ord_list.find(1000))
        self.assertIsNone(ord_list.find(2))
    
    def test_find_decreasing(self):
        ord_list = OrderedList(False)
        for v in [3, 6, 1, 8, 42, -100, 0, 0]:
            ord_list.add(v)
        finded_node = ord_list.find(0)
        self.assertIsNotNone(finded_node)
        self.assertEqual(finded_node.value, 0)
        self.assertEqual(finded_node.next.value, 0)
        self.assertEqual(finded_node.prev.value, 1)
        
        finded_node = ord_list.find(-100)
        self.assertIsNotNone(finded_node)
        self.assertEqual(finded_node.value, -100)
        self.assertIsNone(finded_node.next)
        self.assertEqual(finded_node.prev.value, 0)
        
        finded_node = ord_list.find(42)
        self.assertIsNotNone(finded_node)
        self.assertEqual(finded_node.value, 42)
        self.assertEqual(finded_node.next.value, 8)
        self.assertIsNone(finded_node.prev)
        
        self.assertIsNone(ord_list.find(-1000))
        self.assertIsNone(ord_list.find(1000))
        self.assertIsNone(ord_list.find(2))

    def test_clean(self):
        ord_list = OrderedList(True)
        for v in [8, -42, 0, 0]:
            ord_list.add(v)
        self.assertEqual(ord_list.len(), 4)
        self.assertEqual(extract_values(ord_list.get_all()), [-42, 0, 0, 8])

        ord_list.clean(False)
        self.assertEqual(ord_list.len(), 0)

        for v in [8, -42, 0, 0]:
            ord_list.add(v)
        self.assertEqual(ord_list.len(), 4)
        self.assertEqual(extract_values(ord_list.get_all()), [8, 0, 0, -42])
        
        ord_list.clean(True)
        self.assertEqual(ord_list.len(), 0)
        
        for v in [8, -42, 0, 0]:
            ord_list.add(v)
        self.assertEqual(ord_list.len(), 4)
        self.assertEqual(extract_values(ord_list.get_all()), [-42, 0, 0, 8])


class TestOrderedListIncreasingDelete(unittest.TestCase):

    def setUp(self):
        self.ord_list = OrderedList(True)
        for v in [1, 2, 2, 3, 4]:
            self.ord_list.add(v)
    
    def test_delete_non_exist(self):
        self.ord_list.delete(8)
        self.assertEqual(self.ord_list.len(), 5)
        self.assertEqual(extract_values(self.ord_list.get_all()), [1, 2, 2, 3, 4])
        
    def test_delete_max(self):
        self.ord_list.delete(4)
        self.assertEqual(self.ord_list.len(), 4)
        self.assertEqual(extract_values(self.ord_list.get_all()), [1, 2, 2, 3])

    def test_delete_min(self):
        self.ord_list.delete(1)
        self.assertEqual(self.ord_list.len(), 4)
        self.assertEqual(extract_values(self.ord_list.get_all()), [2, 2, 3, 4])
    
    def test_delete_middle(self):
        self.ord_list.delete(2)
        self.assertEqual(self.ord_list.len(), 4)
        self.assertEqual(extract_values(self.ord_list.get_all()), [1, 2, 3, 4])
    
    def test_delete_full(self):
        ord_list = OrderedList(True)
        ord_list.add(42)
        ord_list.delete(42)
        self.assertEqual(ord_list.len(), 0)
        self.assertEqual(ord_list.get_all(), [])


class TestOrderedListDecreasingDelete(unittest.TestCase):

    def setUp(self):
        self.ord_list = OrderedList(False)
        for v in [1, 2, 2, 3, 4]:
            self.ord_list.add(v)
    
    def test_delete_non_exist(self):
        self.ord_list.delete(8)
        self.assertEqual(self.ord_list.len(), 5)
        self.assertEqual(extract_values(self.ord_list.get_all()), [4, 3, 2, 2, 1])
        
    def test_delete_max(self):
        self.ord_list.delete(4)
        self.assertEqual(self.ord_list.len(), 4)
        self.assertEqual(extract_values(self.ord_list.get_all()), [3, 2, 2, 1])

    def test_delete_min(self):
        self.ord_list.delete(1)
        self.assertEqual(self.ord_list.len(), 4)
        self.assertEqual(extract_values(self.ord_list.get_all()), [4, 3, 2, 2])
    
    def test_delete_middle(self):
        self.ord_list.delete(2)
        self.assertEqual(self.ord_list.len(), 4)
        self.assertEqual(extract_values(self.ord_list.get_all()), [4, 3, 2, 1])

    def test_delete_full(self):
        ord_list = OrderedList(False)
        ord_list.add(42)
        ord_list.delete(42)
        self.assertEqual(ord_list.len(), 0)
        self.assertEqual(ord_list.get_all(), [])


class TestOrderedStringList(unittest.TestCase):

    def test_all_methods(self):
        ord_list = OrderedStringList(True)
        for s in [' ab', 'a', ' a ', '  z', 'x', ' zeeeee  ']:
            ord_list.add(s)
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(extract_values(ord_list.get_all()), [' a ', 'a', ' ab', 'x', '  z', ' zeeeee  '])
        self.assertIsNotNone(ord_list.find('a'))
        self.assertIsNone(ord_list.find('FishKOH'))
        
        ord_list.clean(False)
        for s in [' ab', 'a', ' a ', '  z', 'x', ' zeeeee  ']:
            ord_list.add(s)
        self.assertEqual(extract_values(ord_list.get_all()), [' zeeeee  ', '  z', 'x', ' ab', ' a ', 'a'])
        
        ord_list.delete('FishKOH')
        ord_list.delete('a')
        ord_list.delete(' zeeeee  ')
        ord_list.delete('x')
        self.assertEqual(ord_list.len(), 3)
        self.assertEqual(extract_values(ord_list.get_all()), ['  z', ' ab', ' a '])

