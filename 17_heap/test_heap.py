import unittest
from heap import Heap

class TestHeap(unittest.TestCase):
  
    def test_init(self):
        heap = Heap()
        self.assertEqual(heap.GetMax(), -1)
        self.assertFalse(heap.Add(8))
    
    def test_heap_from_empty_array(self):
        heap = Heap()
        heap.MakeHeap([], 2)
        self.assertEqual(heap.GetMax(), -1)
        # check that max_size is 7
        for i in range(7):
            with self.subTest(i=i):
                self.assertTrue(heap.Add(i))
        self.assertFalse(heap.Add(8))
        for i in reversed(range(7)):
            with self.subTest(i=i):
                self.assertEqual(heap.GetMax(), i)
        self.assertEqual(heap.GetMax(), -1)
    
    def test_get_max_simple(self):
        heap = Heap()
        heap.MakeHeap([4,8,1,2,42], 2)
        self.assertEqual(heap.GetMax(), 42)
        self.assertEqual(heap.GetMax(), 8)
        self.assertEqual(heap.GetMax(), 4)
        self.assertEqual(heap.GetMax(), 2)
        self.assertEqual(heap.GetMax(), 1)
        self.assertEqual(heap.GetMax(), -1)
    
    def test_add(self):
        heap = Heap()
        heap.MakeHeap([], 2)
        heap.Add(4)
        self.assertEqual(heap.HeapArray[:1], [4])
        heap.Add(8)
        self.assertEqual(heap.HeapArray[:2], [8, 4])
        heap.Add(1)
        self.assertEqual(heap.HeapArray[:3], [8, 4, 1])
        heap.Add(2)
        self.assertEqual(heap.HeapArray[:4], [8, 4, 1, 2])
        heap.Add(42)
        self.assertEqual(heap.HeapArray[:5], [42, 8, 1, 2, 4])
        heap.Add(16)
        self.assertEqual(heap.HeapArray[:6], [42, 8, 16, 2, 4, 1])
        heap.Add(8)
        self.assertEqual(heap.HeapArray[:7], [42, 8, 16, 2, 4, 1, 8])
        self.assertFalse(heap.Add(8))
    
    def test_get_max(self):
        heap = Heap()
        heap.MakeHeap([4,8,1,2,42,16,8], 2)
        self.assertEqual(heap.HeapArray[:7], [42, 8, 16, 2, 4, 1, 8])
        heap.GetMax()
        self.assertEqual(heap.HeapArray[:6], [16, 8, 8, 2, 4, 1])
        heap.GetMax()
        #left child priority
        self.assertEqual(heap.HeapArray[:5], [8, 4, 8, 2, 1])
        heap.GetMax()
        self.assertEqual(heap.HeapArray[:4], [8, 4, 1, 2])
        heap.GetMax()
        self.assertEqual(heap.HeapArray[:3], [4, 2, 1])
        heap.GetMax()
        self.assertEqual(heap.HeapArray[:2], [2, 1])
        heap.GetMax()
        self.assertEqual(heap.HeapArray[:1], [1])
        self.assertEqual(heap.GetMax(), 1)
        self.assertEqual(heap.GetMax(), -1)
