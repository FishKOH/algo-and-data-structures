import unittest
from doubly_linked_list_dummy import Node, LinkedList2

def to_native_list(linked_list):
    native_list = []
    node = linked_list.head()
    while isinstance(node, Node):
        native_list.append(node.value)
        node = node.next
    return native_list

def to_native_reverse_list(linked_list):
    native_reverse_list = []
    node = linked_list.tail()
    while isinstance(node, Node):
        native_reverse_list.append(node.value)
        node = node.prev
    return native_reverse_list

def create_DoublyLinkedList(container):
    l = LinkedList2()
    for item in container:
        l.add_in_tail(Node(item))
    return l


class TestDoublyLinkedListAddInTail(unittest.TestCase):

    def test_init(self):
        l = LinkedList2()
        self.assertTrue(l.empty())
        self.assertIsNone(l.head())
        self.assertIsNone(l.tail())
        self.assertEqual(to_native_list(l), [])

    def test_add_in_tail(self):
        l = LinkedList2()
        l.add_in_tail(Node(1))
        l.add_in_tail(Node(2))
        l.add_in_tail(Node(4))
        l.add_in_tail(Node(8))
        
        self.assertFalse(l.empty())
        
        self.assertIsNotNone(l.head())
        self.assertEqual(l.head().value, 1)
        self.assertIsNotNone(l.head().next)
        self.assertNotIsInstance(l.head().prev, Node)
        
        self.assertIsNotNone(l.tail())
        self.assertEqual(l.tail().value, 8)
        self.assertIsNotNone(l.tail().prev)
        self.assertNotIsInstance(l.tail().next, Node)
        
        self.assertEqual(to_native_list(l), [1,2,4,8])
        self.assertEqual(to_native_reverse_list(l), [8,4,2,1])


class TestDoublyLinkedListFind(unittest.TestCase):

    def test_find(self):
        l = LinkedList2()
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
        l = LinkedList2()
        self.assertIsNone(l.find(2))
        self.assertIsNone(l.find(-1))
    
    def test_find_all(self):
        l = LinkedList2()
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
        l = LinkedList2()
        self.assertEqual(l.find_all(2), [])
        self.assertEqual(l.find_all(-1), [])
        


class TestDoublyLinkedListDelete(unittest.TestCase):

    def tearDown(self):
        fact_tail = None
        node = self.doubly_linked_list.head()
        while isinstance(node, Node):
            fact_tail = node;
            node = node.next
        self.assertEqual(self.doubly_linked_list.tail(), fact_tail)
        
        #DoublyLinkedList: check correctness link by prev
        fact_head = None
        node = self.doubly_linked_list.tail()
        while isinstance(node, Node):
            fact_head = node;
            node = node.prev
        self.assertEqual(self.doubly_linked_list.head(), fact_head)
        
        self.assertEqual(to_native_list(self.doubly_linked_list), to_native_reverse_list(self.doubly_linked_list)[::-1])

    def test_delete_first_at_middle(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,2,2,8])
        self.doubly_linked_list.delete(2)
        
        self.assertIsNotNone(self.doubly_linked_list.head())
        self.assertIsNotNone(self.doubly_linked_list.tail())
        self.assertEqual(to_native_list(self.doubly_linked_list), [1,2,8])
    
    def test_delete_first_at_head(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,2,2,8])
        self.doubly_linked_list.delete(1)
        
        self.assertEqual(self.doubly_linked_list.head().value, 2)
        self.assertIsNotNone(self.doubly_linked_list.head().next)
        self.assertIsNotNone(self.doubly_linked_list.tail())
        self.assertEqual(to_native_list(self.doubly_linked_list), [2,2,8])
    
    def test_delete_first_at_tail(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,2,2,8])
        self.doubly_linked_list.delete(8)
        
        self.assertIsNotNone(self.doubly_linked_list.head())
        self.assertEqual(self.doubly_linked_list.tail().value, 2)
        self.assertNotIsInstance(self.doubly_linked_list.tail().next, Node)
        self.assertEqual(to_native_list(self.doubly_linked_list), [1,2,2])
    
    def test_delete_not_exist(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,2,2,8])
        self.doubly_linked_list.delete(4)
        
        self.assertNotIsInstance(self.doubly_linked_list.tail().next, Node)
        self.assertEqual(to_native_list(self.doubly_linked_list), [1,2,2,8])

    def test_delete_at_empty(self):
        self.doubly_linked_list = LinkedList2()
        self.doubly_linked_list.delete(1)
        
        self.assertIsNone(self.doubly_linked_list.head())
        self.assertIsNone(self.doubly_linked_list.tail())
    
    def test_delete_at_oneitem(self):
        self.doubly_linked_list = create_DoublyLinkedList([1])
        self.doubly_linked_list.delete(1)
        
        self.assertIsNone(self.doubly_linked_list.head())
        self.assertIsNone(self.doubly_linked_list.tail())
        self.assertEqual(to_native_list(self.doubly_linked_list), [])
    
    def test_delete_all_sequently(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,1,1,2,4])
        self.doubly_linked_list.delete(1, all=True)
        
        self.assertEqual(to_native_list(self.doubly_linked_list), [2,4])
    
    def test_delete_all_nonsequently(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,2,1,4,1])
        self.doubly_linked_list.delete(1, all=True)
        
        self.assertEqual(to_native_list(self.doubly_linked_list), [2,4])
    
    def test_delete_all_same_items(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,1,1,1,1])
        self.doubly_linked_list.delete(1, all=True)
        
        self.assertIsNone(self.doubly_linked_list.head())
        self.assertIsNone(self.doubly_linked_list.tail())
        self.assertEqual(to_native_list(self.doubly_linked_list), [])
    
    def test_delete_all_same_items_except_one(self):
        self.doubly_linked_list = create_DoublyLinkedList([1,1,2,1,1,1])
        self.doubly_linked_list.delete(1, all=True)
        
        self.assertNotIsInstance(self.doubly_linked_list.tail().next, Node)
        self.assertEqual(to_native_list(self.doubly_linked_list), [2])

class TestDoublyLinkedListClean(unittest.TestCase):

    def test_clean(self):
        l = create_DoublyLinkedList([1,2,4,8,16])
        l.clean()
        
        self.assertIsNone(l.head())
        self.assertIsNone(l.tail())

    def test_clean_empty(self):
        l = LinkedList2()
        l.clean()
        
        self.assertIsNone(l.head())
        self.assertIsNone(l.tail())        

class TestDoublyLinkedListLen(unittest.TestCase):

    def test_len(self):
        l = create_DoublyLinkedList([1,2,4,8,16])
        self.assertEqual(l.len(), 5)

    def test_len_empty(self):
        l = LinkedList2()
        self.assertEqual(l.len(), 0)

class TestDoublyLinkedListInsert(unittest.TestCase):

    def tearDown(self):
        fact_tail = None
        node = self.doubly_linked_list.head()
        while isinstance(node, Node):
            fact_tail = node;
            node = node.next
        self.assertEqual(self.doubly_linked_list.tail(), fact_tail)
        
        #DoublyLinkedList: check correctness link by prev
        fact_head = None
        node = self.doubly_linked_list.tail()
        while isinstance(node, Node):
            fact_head = node;
            node = node.prev
        self.assertEqual(self.doubly_linked_list.head(), fact_head)
        
        self.assertEqual(to_native_list(self.doubly_linked_list), to_native_reverse_list(self.doubly_linked_list)[::-1])

    def test_insert_at_middle(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.add_in_tail(node2)
        self.doubly_linked_list.add_in_tail(node3)
        self.doubly_linked_list.insert(node1, Node(5))
        self.assertEqual(to_native_list(self.doubly_linked_list), [-1, 5, 0, 1])

    def test_insert_at_tail(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.add_in_tail(node2)
        self.doubly_linked_list.add_in_tail(node3)
        self.doubly_linked_list.insert(node3, Node(5))
        # self.assertNotIsInstance(self.doubly_linked_list.tail().next)
        self.assertEqual(to_native_list(self.doubly_linked_list), [-1, 0, 1, 5])

    def test_insert_at_tail_pass_none(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.add_in_tail(node2)
        self.doubly_linked_list.add_in_tail(node3)
        self.doubly_linked_list.insert(None, Node(5))
        # self.assertIsNone(self.doubly_linked_list.tail().next)
        self.assertEqual(to_native_list(self.doubly_linked_list), [-1, 0, 1, 5])
    
#    couldn't insert_at_head
#    def test_insert_at_head(self):
#        self.doubly_linked_list = LinkedList2()
#        node1 = Node(-1)
#        node2 = Node(0)
#        node3 = Node(1)
#        self.doubly_linked_list.add_in_tail(node1)
#        self.doubly_linked_list.add_in_tail(node2)
#        self.doubly_linked_list.add_in_tail(node3)
#        self.doubly_linked_list.insert(None, Node(5))
#        self.assertEqual(to_native_list(self.doubly_linked_list), [5, -1, 0, 1])
    
    def test_insert_at_empty(self):
        self.doubly_linked_list = LinkedList2()
        self.doubly_linked_list.insert(None, Node(5))
        self.assertEqual(to_native_list(self.doubly_linked_list), [5])

#    couldn't insert_at_head
#    def test_insert_at_head_singleitem(self):
#        self.doubly_linked_list = LinkedList2()
#        node1 = Node(42)
#        self.doubly_linked_list.add_in_tail(node1)
#        self.doubly_linked_list.insert(None, Node(5))
#        self.assertEqual(to_native_list(self.doubly_linked_list), [5, 42])

    def test_insert_at_tail_sinleitem(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(42)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.insert(node1, Node(5))
        self.assertEqual(to_native_list(self.doubly_linked_list), [42, 5])
        
    def test_insert_at_tail_sinleitem_pass_none(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(42)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.insert(None, Node(5))
        self.assertEqual(to_native_list(self.doubly_linked_list), [42, 5])

class TestDoublyLinkedListAddInHead(unittest.TestCase):

    def tearDown(self):
        fact_tail = None
        node = self.doubly_linked_list.head()
        while isinstance(node, Node):
            fact_tail = node;
            node = node.next
        self.assertEqual(self.doubly_linked_list.tail(), fact_tail)
        
        #DoublyLinkedList: check correctness link by prev
        fact_head = None
        node = self.doubly_linked_list.tail()
        while isinstance(node, Node):
            fact_head = node;
            node = node.prev
        self.assertEqual(self.doubly_linked_list.head(), fact_head)
        
        self.assertEqual(to_native_list(self.doubly_linked_list), to_native_reverse_list(self.doubly_linked_list)[::-1])

    def test_add_in_head(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(-1)
        node2 = Node(0)
        node3 = Node(1)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.add_in_tail(node2)
        self.doubly_linked_list.add_in_tail(node3)
        self.doubly_linked_list.add_in_head(Node(5))
        self.assertEqual(to_native_list(self.doubly_linked_list), [5, -1, 0, 1])

    def test_add_in_head_empty(self):
        self.doubly_linked_list = LinkedList2()
        self.doubly_linked_list.add_in_head(Node(8))
        self.assertEqual(to_native_list(self.doubly_linked_list), [8])    
    def test_add_in_head_singleitem(self):
        self.doubly_linked_list = LinkedList2()
        node1 = Node(42)
        self.doubly_linked_list.add_in_tail(node1)
        self.doubly_linked_list.add_in_head(Node(8))
        self.assertEqual(to_native_list(self.doubly_linked_list), [8, 42])

if __name__ == '__main__':
    unittest.main()
