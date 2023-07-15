import unittest
from linked_list import Node, LinkedList
from test_linked_list import to_native_list, create_LinkedList

def sum_linked_lists(linked_list1, linked_list2):
    if linked_list1.len() != linked_list2.len():
        return None
    
    sums_list = LinkedList()
    node_list1 = linked_list1.head
    node_list2 = linked_list2.head
    while node_list1 is not None:
        sums_list.add_in_tail(Node(node_list1.value + node_list2.value))
        node_list1 = node_list1.next
        node_list2 = node_list2.next
    return sums_list



class TestSumLinkedList(unittest.TestCase):

    def test_sum(self):
        l1 = create_LinkedList([1,2,3,42,8])
        l2 = create_LinkedList([-1,-2,-3,4,5])
        self.assertEqual(to_native_list(sum_linked_lists(l1, l2)), [0,0,0,46,13])

    def test_sum_non_equal_size(self):
        l1 = create_LinkedList([1,2,3])
        l2 = create_LinkedList([1,2,3,4,5])
        self.assertIsNone(sum_linked_lists(l1, l2))

    def test_sum_empty(self):
        l1 = LinkedList()
        l2 = LinkedList()
        sums_list = sum_linked_lists(l1, l2)
        self.assertEqual(sums_list.len(), 0)

if __name__ == '__main__':
    unittest.main()
