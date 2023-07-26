import unittest

from queue import Queue

def rotate_queue(queue : Queue, n : int):
    assert(n >= 0)
    if queue.size() == 0:
        return
    n = n % queue.size()
    for _ in range(n):
        queue.enqueue(queue.dequeue())


def get_queue_values(queue : Queue):
    values = []
    while queue.size() > 0:
        values.append(queue.dequeue())
    for v in values:
        queue.enqueue(v)
    return values

class TestQueue(unittest.TestCase):

    def test_rotate_empty(self):
        q = Queue()
        rotate_queue(q, 0)
        self.assertEqual(q.size(), 0)
        rotate_queue(q, 42)
        self.assertEqual(q.size(), 0)
    
    def test_rotate(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        self.assertEqual(get_queue_values(q), [0,1,2,3,4])
        rotate_queue(q, 0)
        self.assertEqual(get_queue_values(q), [0,1,2,3,4])
        rotate_queue(q, 1)
        self.assertEqual(get_queue_values(q), [1,2,3,4,0])
        rotate_queue(q, 101)
        self.assertEqual(get_queue_values(q), [2,3,4,0,1])
        rotate_queue(q, 2)
        self.assertEqual(get_queue_values(q), [4,0,1,2,3])
