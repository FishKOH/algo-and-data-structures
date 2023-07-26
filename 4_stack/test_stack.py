import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_init(self):
        a = Stack()
        self.assertEqual(a.size(), 0)
        self.assertIsNone(a.pop())
        self.assertIsNone(a.peek())
    
    def test_push_pop_peek(self):
        a = Stack()
        a.push(42)
        a.push(2.71)
        a.push("FishKOH")
        self.assertEqual(a.size(), 3)
        self.assertEqual(a.peek(), "FishKOH")
        self.assertEqual(a.size(), 3)
        self.assertEqual(a.pop(), "FishKOH")
        self.assertEqual(a.size(), 2)
        self.assertEqual(a.peek(), 2.71)
        self.assertEqual(a.size(), 2)
        self.assertEqual(a.pop(), 2.71)
        self.assertEqual(a.size(), 1)
        self.assertEqual(a.peek(), 42)
        self.assertEqual(a.size(), 1)
        self.assertEqual(a.pop(), 42)
        self.assertEqual(a.size(), 0)
        self.assertIsNone(a.pop())
        self.assertIsNone(a.peek())
