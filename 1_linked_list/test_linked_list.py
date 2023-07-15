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
        l.add_in_tail(Node(item))
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

    def tearDown(self):
        fact_tail = None
        node = self.linked_list.head
        while node is not None:
            fact_tail = node;
            node = node.next
        self.assertEqual(self.linked_list.tail, fact_tail)

    def test_delete_first_at_middle(self):
        self.linked_list = create_LinkedList([1,2,2,8])
        self.linked_list.delete(2)
        
        self.assertIsNotNone(self.linked_list.head)
        self.assertIsNotNone(self.linked_list.tail)
        self.assertEqual(to_native_list(self.linked_list), [1,2,8])
    
    def test_delete_first_at_head(self):
        self.linked_list = create_LinkedList([1,2,2,8])
        self.linked_list.delete(1)
        
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertIsNotNone(self.linked_list.head.next)
        self.assertIsNotNone(self.linked_list.tail)
        self.assertEqual(to_native_list(self.linked_list), [2,2,8])
    
    def test_delete_first_at_tail(self):
        self.linked_list = create_LinkedList([1,2,2,8])
        self.linked_list.delete(8)
        
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.tail.value, 2)
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(to_native_list(self.linked_list), [1,2,2])
    
    def test_delete_not_exist(self):
        self.linked_list = create_LinkedList([1,2,2,8])
        self.linked_list.delete(4)
        
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(to_native_list(self.linked_list), [1,2,2,8])

    def test_delete_at_empty(self):
        self.linked_list = LinkedList()
        self.linked_list.delete(1)
        
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
    
    def test_delete_at_oneitem(self):
        self.linked_list = create_LinkedList([1])
        self.linked_list.delete(1)
        
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(to_native_list(self.linked_list), [])
    
    def test_delete_all_sequently(self):
        self.linked_list = create_LinkedList([1,1,1,2,4])
        self.linked_list.delete(1, all=True)
        
        self.assertEqual(to_native_list(self.linked_list), [2,4])
    
    def test_delete_all_nonsequently(self):
        self.linked_list = create_LinkedList([1,2,1,4,1])
        self.linked_list.delete(1, all=True)
        
        self.assertEqual(to_native_list(self.linked_list), [2,4])
    
    def test_delete_all_same_items(self):
        self.linked_list = create_LinkedList([1,1,1,1,1])
        self.linked_list.delete(1, all=True)
        
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(to_native_list(self.linked_list), [])
    
    def test_delete_all_same_items_except_one(self):
        self.linked_list = create_LinkedList([1,1,2,1,1,1])
        self.linked_list.delete(1, all=True)
        
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(to_native_list(self.linked_list), [2])

class TestLinkedListClean(unittest.TestCase):

    def test_clean(self):
        l = create_LinkedList([1,2,4,8,16])
        l.clean()
        
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)

    def test_clean_empty(self):
        l = LinkedList()
        l.clean()
        
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)        

class TestLinkedListLen(unittest.TestCase):

    def test_clean(self):
        l = create_LinkedList([1,2,4,8,16])
        self.assertEqual(l.len(), 5)

    def test_clean_empty(self):
        l = LinkedList()
        self.assertEqual(l.len(), 0)

class TestLinkedListInsert(unittest.TestCase):

    def tearDown(self):
        fact_tail = None
        node = self.linked_list.head
        while node is not None:
            fact_tail = node;
            node = node.next
        self.assertEqual(self.linked_list.tail, fact_tail)

    def test_insert_at_middle(self):
        self.linked_list = LinkedList()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.linked_list.add_in_tail(node3)
        self.linked_list.insert(node1, Node(5))
        self.assertEqual(to_native_list(self.linked_list), [-1, 5, 0, 1])

    def test_insert_at_tail(self):
        self.linked_list = LinkedList()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.linked_list.add_in_tail(node3)
        self.linked_list.insert(node3, Node(5))
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(to_native_list(self.linked_list), [-1, 0, 1, 5])
    
    def test_insert_at_head(self):
        self.linked_list = LinkedList()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.linked_list.add_in_tail(node3)
        self.linked_list.insert(None, Node(5))
        self.assertEqual(to_native_list(self.linked_list), [5, -1, 0, 1])
    
    def test_insert_at_empty(self):
        self.linked_list = LinkedList()
        self.linked_list.insert(None, Node(5))
        self.assertEqual(to_native_list(self.linked_list), [5])
    
    def test_insert_at_head_singleitem(self):
        self.linked_list = LinkedList()
        node1 = Node(42)
        self.linked_list.add_in_tail(node1)
        self.linked_list.insert(None, Node(5))
        self.assertEqual(to_native_list(self.linked_list), [5, 42])

    def test_insert_at_tail_sinleitem(self):
        self.linked_list = LinkedList()
        node1 = Node(42)
        self.linked_list.add_in_tail(node1)
        self.linked_list.insert(node1, Node(5))
        self.assertEqual(to_native_list(self.linked_list), [42, 5])
    
if __name__ == '__main__':
    unittest.main()
