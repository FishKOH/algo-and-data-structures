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

class TestDynArrayInsertWithoutRealloc(unittest.TestCase):

    def setUp(self):
        self.dyn_array = DynArray()
        for i in range(10):
            self.dyn_array.append(i)

    def test_insert_raises(self):
        with self.assertRaises(IndexError):
            self.dyn_array.insert(-1, 42)
        with self.assertRaises(IndexError):            
            self.dyn_array.insert(11, 42)
            
        self.assertEqual(len(self.dyn_array), 10)
    
    def test_insert_at_begin(self):
        self.dyn_array.insert(0, 42)
        
        self.assertEqual(self.dyn_array.count, 11)
        self.assertEqual(self.dyn_array.capacity, 16)
        self.assertEqual(self.dyn_array[0], 42)
        self.assertEqual(self.dyn_array[1], 0)
        self.assertEqual(self.dyn_array[10], 9)
        
    def test_insert_at_middle(self):
        self.dyn_array.insert(5, 73)
        
        self.assertEqual(self.dyn_array.count, 11)
        self.assertEqual(self.dyn_array.capacity, 16)
        self.assertEqual(self.dyn_array[4], 4)
        self.assertEqual(self.dyn_array[5], 73)
        self.assertEqual(self.dyn_array[6], 5)
        self.assertEqual(self.dyn_array[10], 9)

    def test_insert_at_end(self):
        self.dyn_array.insert(10, 1000)
        
        self.assertEqual(self.dyn_array.count, 11)
        self.assertEqual(self.dyn_array.capacity, 16)
        self.assertEqual(self.dyn_array[9], 9)
        self.assertEqual(self.dyn_array[10], 1000)

class TestDynArrayInsertWithRealloc(unittest.TestCase):

    def setUp(self):
        self.dyn_array = DynArray()
        for i in range(16):
            self.dyn_array.append(i)

    def test_insert_at_begin(self):
        self.dyn_array.insert(0, 42)
        
        self.assertEqual(self.dyn_array.count, 17)
        self.assertEqual(self.dyn_array.capacity, 32)
        self.assertEqual(self.dyn_array[0], 42)
        self.assertEqual(self.dyn_array[1], 0)
        self.assertEqual(self.dyn_array[16], 15)
        
    def test_insert_at_middle(self):
        self.dyn_array.insert(8, 73)
        
        self.assertEqual(self.dyn_array.count, 17)
        self.assertEqual(self.dyn_array.capacity, 32)
        self.assertEqual(self.dyn_array[7], 7)
        self.assertEqual(self.dyn_array[8], 73)
        self.assertEqual(self.dyn_array[9], 8)
        self.assertEqual(self.dyn_array[16], 15)
        
    def test_insert_at_end(self):
        self.dyn_array.insert(16, 1000)
        
        self.assertEqual(self.dyn_array.count, 17)
        self.assertEqual(self.dyn_array.capacity, 32)
        self.assertEqual(self.dyn_array[15], 15)
        self.assertEqual(self.dyn_array[16], 1000)

class TestDynArrayDeleteWithoutDealloc(unittest.TestCase):

    def setUp(self):
        self.dyn_array = DynArray()
        for i in range(10):
            self.dyn_array.append(i)

    def test_delete_raises(self):
        with self.assertRaises(IndexError):
            self.dyn_array.delete(-1)
        with self.assertRaises(IndexError):            
            self.dyn_array.delete(10)
            
        self.assertEqual(len(self.dyn_array), 10)
    
    def test_delete_at_begin(self):
        self.dyn_array.delete(0)
        
        self.assertEqual(self.dyn_array.count, 9)
        self.assertEqual(self.dyn_array.capacity, 16)
        self.assertEqual(self.dyn_array[0], 1)
        self.assertEqual(self.dyn_array[8], 9)
        
    def test_delete_at_middle(self):
        self.dyn_array.delete(4)
        
        self.assertEqual(self.dyn_array.count, 9)
        self.assertEqual(self.dyn_array.capacity, 16)
        self.assertEqual(self.dyn_array[3], 3)
        self.assertEqual(self.dyn_array[4], 5)
        self.assertEqual(self.dyn_array[8], 9)
        
    def test_delete_at_end(self):
        self.dyn_array.delete(9)
        
        self.assertEqual(self.dyn_array.count, 9)
        self.assertEqual(self.dyn_array.capacity, 16)
        self.assertEqual(self.dyn_array[7], 7)
        self.assertEqual(self.dyn_array[8], 8)

class TestDynArrayDeleteWithDealloc(unittest.TestCase):

    def setUp(self):
        self.dyn_array = DynArray()
        self.dyn_array.resize(32)
        for i in range(16):
            self.dyn_array.append(i)
  
    def test_delete_at_begin(self):
        self.dyn_array.delete(0)
        
        self.assertEqual(self.dyn_array.count, 15)
        self.assertEqual(self.dyn_array.capacity, 21)
        self.assertEqual(self.dyn_array[0], 1)
        self.assertEqual(self.dyn_array[14], 15)
        
    def test_delete_at_middle(self):
        self.dyn_array.delete(8)
        
        self.assertEqual(self.dyn_array.count, 15)
        self.assertEqual(self.dyn_array.capacity, 21)
        self.assertEqual(self.dyn_array[7], 7)
        self.assertEqual(self.dyn_array[8], 9)
        self.assertEqual(self.dyn_array[14], 15)

    def test_delete_at_end(self):
        self.dyn_array.delete(15)
        
        self.assertEqual(self.dyn_array.count, 15)
        self.assertEqual(self.dyn_array.capacity, 21)
        self.assertEqual(self.dyn_array[13], 13)
        self.assertEqual(self.dyn_array[14], 14)
        
    def test_delete_minimal_capacity(self):
        self.dyn_array.delete(0)
        
        self.assertEqual(self.dyn_array.count, 15)
        self.assertEqual(self.dyn_array.capacity, 21)
        
        for i in range(4):
            self.dyn_array.delete(0)
            
        self.assertEqual(self.dyn_array.count, 11)
        self.assertEqual(self.dyn_array.capacity, 21)
        
        self.dyn_array.delete(0)
            
        self.assertEqual(self.dyn_array.count, 10)
        self.assertEqual(self.dyn_array.capacity, 16)
        
        for i in reversed(range(10)):
            self.dyn_array.delete(0)
            with self.subTest(i=i):
                self.assertEqual(self.dyn_array.count, i)
                self.assertEqual(self.dyn_array.capacity, 16)
        

if __name__ == '__main__':
    unittest.main()
