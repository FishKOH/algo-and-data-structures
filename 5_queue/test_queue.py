import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    
    def test_init(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        self.assertIsNone(q.dequeue())
    
    def test_enqueue_dequeue(self):
        q = Queue()

        for i in range(10):
            q.enqueue(i)
        self.assertEqual(q.size(), 10)

        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(q.dequeue(), i)
                self.assertEqual(q.size(), 10-1-i)
        self.assertEqual(q.size(), 0)
        self.assertIsNone(q.dequeue())
    
    def test_enqueue_dequeue_complex(self):
        q = Queue()

        sequence = [10, -8, 14, -15, 1]

        for num in sequence:
            if num > 0:
                for i in range(num):
                    q.enqueue(i)
            else:
                for i in range(abs(num)):
                    q.dequeue()

        self.assertEqual(q.size(), sum(sequence))
