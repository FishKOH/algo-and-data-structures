import unittest
from deque import Deque

class TestDeque(unittest.TestCase):

    def test_init(self):
        deq = Deque()
        self.assertEqual(deq.size(), 0)
        self.assertIsNone(deq.removeFront())
        self.assertIsNone(deq.removeTail())
    
    def test_add_remove(self):
        deq = Deque()
        deq.addFront(-1)
        deq.addFront(-2)
        deq.addTail(1)
        deq.addTail(2)
        deq.addTail(3)
        self.assertEqual(deq.size(), 5)
        self.assertEqual(deq.removeFront(), -2)
        self.assertEqual(deq.removeFront(), -1)
        self.assertEqual(deq.removeTail(), 3)
        self.assertEqual(deq.removeTail(), 2)
        self.assertEqual(deq.removeTail(), 1)
        self.assertEqual(deq.size(), 0)
        self.assertIsNone(deq.removeFront())
        self.assertIsNone(deq.removeTail())
    
    def test_add_remove_complex(self):
        front_elems = [-1,-2,-3,-8,-42]
        tail_elems = [1,2,3,8,42]
        deq = Deque()
        for elem in front_elems:
            deq.addFront(elem)
        for elem in tail_elems:
            deq.addTail(elem)

        removed_front_elem = []
        removed_tail_elem = []
        for _ in range(7):
            removed_front_elem.append(deq.removeFront())   
        while deq.size() > 0:
            removed_tail_elem.append(deq.removeTail())    
        self.assertEqual(removed_front_elem, [-42, -8, -3, -2, -1, 1, 2])
        self.assertEqual(removed_tail_elem, [42, 8, 3])
