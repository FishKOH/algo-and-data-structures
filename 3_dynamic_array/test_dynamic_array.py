import unittest
from dynamic_array import DynArray


class TestDynArray(unittest.TestCase):

    def test_init(self):
        a = DynArray()
        self.assertEqual(a.count, 0)
        self.assertEqual(a.capacity, 16)
    
    def test_resize(self):
        a = DynArray()
        a.resize(42)
        self.assertEqual(a.count, 0)
        self.assertEqual(a.capacity, 42)
        
        a.resize(16)
        self.assertEqual(a.count, 0)
        self.assertEqual(a.capacity, 16)
        
        a.resize(24)
        self.assertEqual(a.count, 0)
        self.assertEqual(a.capacity, 24)     

    def test_append(self):
        a = DynArray()
        for i in range(15):
            a.append(i)
        self.assertEqual(a.count, 15)
        self.assertEqual(a.capacity, 16)
        
        a.append(15)
        self.assertEqual(a.count, 16)
        self.assertEqual(a.capacity, 16)
        
        a.append(16)
        self.assertEqual(a.count, 17)
        self.assertEqual(a.capacity, 32)
        
    def test_indexing(self):
        a = DynArray()
        for i in range(15):
            a.append(i)
        
        self.assertEqual(a[0], 0)
        self.assertEqual(a[8], 8)
        self.assertEqual(a[14], 14)
        
        with self.assertRaises(IndexError):
            a[-1]
            
        with self.assertRaises(IndexError):            
            a[15]
