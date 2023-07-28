class BaseNode:
    def __init__(self):
        self.prev = None
        self.next = None

class Node(BaseNode):
    def __init__(self, v):
        self.value = v
        super().__init__()

class LinkedList2:  
    def __init__(self):
        self.__dummy_head = BaseNode()
        self.__dummy_head.next = self.__dummy_head
        self.__dummy_head.prev = self.__dummy_head

    def empty(self):
        return self.__dummy_head.next == self.__dummy_head    

    def head(self):
        return None if self.empty() else self.__dummy_head.next

    def tail(self):
        return None if self.empty() else self.__dummy_head.prev

    def __insert(self, after_node, new_node):
        new_node.next = after_node.next
        new_node.prev = after_node

        after_node.next.prev = new_node
        after_node.next = new_node

    def __delete(self, delete_node):
        delete_node.prev.next = delete_node.next
        delete_node.next.prev = delete_node.prev

    def add_in_tail(self, item):
        self.__insert(self.__dummy_head.prev, item)

    def len(self):
        node_count = 0
        node = self.head()
        while isinstance(node, Node):
            node_count += 1
            node = node.next
        return node_count

    __len__ = len

    def add_in_head(self, newNode):
        if self.empty():
            self.add_in_tail(newNode)
        else:
            self.__insert(self.__dummy_head, newNode)
    
    def delete_in_tail(self):
        if not self.empty():
            self.__delete(self.__dummy_head.prev)

    def delete_in_head(self):
        if not self.empty():
            self.__delete(self.__dummy_head.next)

class Queue:
    def __init__(self):
        # Time Complexity
        # |                    | enqueue  | dequeue | size |
        # | ---                | ---      | ---     | ---  |
        # | native_list        | O(1)     | O(N)    | O(1) |
        # | linked_list        | O(1)     | O(N)    | O(N) |
        # | doubly_linked_list | O(1)     | O(1)    | O(N) |
        self.__queue = LinkedList2()
        self.__size = 0 # optimize self.size() O(N) -> O(1)

    def enqueue(self, item):
        self.__queue.add_in_tail(Node(item))
        self.__size += 1

    def dequeue(self):
        if self.__queue.empty():
            return None
        
        head_value = self.__queue.head().value
        self.__queue.delete_in_head()
        self.__size -= 1
        return head_value

    def size(self):
        return self.__size
