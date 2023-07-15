import unittest
from linked_list import Node, LinkedList

def to_native_list(linked_list):
    native_list = []
    node = linked_list.head
    while node is not None:
        native_list.append(node.value)
        node = node.next
    return native_list

def create_LinkedList(container):
    l = LinkedList()
    for item in container:
        l.add_in_tail(item)
    return l


class TestLinkedListBlank(unittest.TestCase):

    def test_init(self):
        l = LinkedList()
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)
        self.assertEqual(to_native_list(l), [])

    def test_add_in_tail(self):
        l = LinkedList()
        l.add_in_tail(Node(1))
        l.add_in_tail(Node(2))
        l.add_in_tail(Node(4))
        l.add_in_tail(Node(8))
        self.assertEqual(l.head.value, 1)
        self.assertIsNotNone(l.head.next)
        self.assertEqual(l.tail.value, 8)
        self.assertIsNone(l.tail.next)
        self.assertEqual(to_native_list(l), [1,2,4,8])


class TestLinkedListFind(unittest.TestCase):

    def test_find(self):
        l = LinkedList()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(0)
        node4 = Node(1)
        l.add_in_tail(node1)
        l.add_in_tail(node2)
        l.add_in_tail(node3)
        l.add_in_tail(node4)
        self.assertIsNone(l.find(2))
        self.assertEqual(l.find(-1), node1)
        self.assertEqual(l.find(0), node2)
        self.assertEqual(l.find(1), node4)
    
    def test_find_at_empty(self):
        l = LinkedList()
        self.assertIsNone(l.find(2))
        self.assertIsNone(l.find(-1))
    
    def test_find_all(self):
        l = LinkedList()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(0)
        node4 = Node(1)
        l.add_in_tail(node1)
        l.add_in_tail(node2)
        l.add_in_tail(node3)
        l.add_in_tail(node4)
        self.assertEqual(l.find_all(2), [])
        self.assertEqual(l.find_all(-1), [node1])
        self.assertEqual(l.find_all(0), [node2, node3])
        self.assertEqual(l.find_all(1), [node4])
    
    def test_find_all_at_empty(self):
        l = LinkedList()
        self.assertEqual(l.find_all(2), [])
        self.assertEqual(l.find_all(-1), [])

class TestLinkedListDelete(unittest.TestCase):
    @unittest.expectedFailure
    def test_delete_first_at_middle(self):
        l = create_LinkedList([1,2,2,8])
        l.delete(2)
        self.assertIsNotNone(l.head)
        self.assertIsNotNone(l.tail)
        self.assertEqual(to_native_list(l), [1,2,8])
    @unittest.expectedFailure
    def test_delete_first_at_head(self):
        l = create_LinkedList([1,2,2,8])
        l.delete(1)
        self.assertEqual(l.head.value, 2)
        self.assertIsNotNone(l.head.next)
        self.assertIsNotNone(l.tail)
        self.assertEqual(to_native_list(l), [2,2,8])
    @unittest.expectedFailure
    def test_delete_first_at_tail(self):
        l = create_LinkedList([1,2,2,8])
        l.delete(8)
        self.assertIsNotNone(l.head)
        self.assertEqual(l.tail.value, 2)
        self.assertIsNone(l.tail.next)
        self.assertEqual(to_native_list(l), [1,2,2])
    @unittest.expectedFailure
    def test_delete_not_exist(self):
        l = create_LinkedList([1,2,2,8])
        l.delete(4)
        self.assertIsNone(l.tail.next)
        self.assertEqual(to_native_list(l), [1,2,2,8])

    def test_delete_at_empty(self):
        l = LinkedList()
        l.delete(1)
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)
    @unittest.expectedFailure
    def test_delete_at_oneitem(self):
        l = create_LinkedList([1])
        l.delete(1)
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)
        self.assertEqual(to_native_list(l), [])
    @unittest.expectedFailure
    def test_delete_all_sequently(self):
        l = create_LinkedList([1,1,1,2,4])
        l.delete(1, all=True)
        self.assertEqual(to_native_list(l), [2,4])
    @unittest.expectedFailure
    def test_delete_all_nonsequently(self):
        l = create_LinkedList([1,2,1,4,1])
        l.delete(1, all=True)
        self.assertEqual(to_native_list(l), [2,4])
    @unittest.expectedFailure
    def test_delete_all_same_items(self):
        l = create_LinkedList([1,1,1,1,1])
        l.delete(1, all=True)
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)
        self.assertEqual(to_native_list(l), [])
    @unittest.expectedFailure
    def test_delete_all_same_items_except_one(self):
        l = create_LinkedList([1,1,2,1,1,1])
        l.delete(1, all=True)
        self.assertIsNone(l.tail.next)
        self.assertEqual(to_native_list(l), [2])
    
    
    #middle head tail
    #exist not exist
    #many empty single
    #all sequently / not sequently / all deleted / all-1 deleted
    
if __name__ == '__main__':
    unittest.main()
