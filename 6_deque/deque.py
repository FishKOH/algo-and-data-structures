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
        self.__size = 0 # optimize self.size() O(N) -> O(1)

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
        
        self.__size += 1 # optimize self.size() O(N) -> O(1)

    def __delete(self, delete_node):
        delete_node.prev.next = delete_node.next
        delete_node.next.prev = delete_node.prev
        
        self.__size -= 1 # optimize self.size() O(N) -> O(1)

    def add_in_tail(self, item):
        self.__insert(self.__dummy_head.prev, item)

    def len(self):
        return self.__size # optimize self.size() O(N) -> O(1)
        # node_count = 0
        # node = self.head()
        # while isinstance(node, Node):
        #     node_count += 1
        #     node = node.next
        # return node_count

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

class Deque:
    def __init__(self):
        # Time Complexity
        # |                           | addFront  | addTail | removeFront | removeTail | size |
        # | ---                       | ---       | ---     | ---         | ---        | ---  |
        # | native_list               | O(N)      | O(1)    | O(N)        | O(1)       | O(1) |
        # | native_list(tail:front)   | O(1)      | O(N)    | O(1)        | O(N)       | O(1) |
        # | linked_list               | O(1)      | O(1)    | O(1)        | O(N)       | O(N) |
        # | linked_list(tail->front)  | O(1)      | O(1)    | O(N)        | O(1)       | O(N) |
        # | doubly_linked_list        | O(1)      | O(1)    | O(1)        | O(1)       | O(N) |
        self.__deque = LinkedList2()

    def addFront(self, item):
        self.__deque.add_in_head(Node(item))

    def addTail(self, item):
        self.__deque.add_in_tail(Node(item))
        
    def removeFront(self):
        if self.__deque.empty():
            return None

        saved_value = self.__deque.head().value
        self.__deque.delete_in_head()
        return saved_value

    def removeTail(self):
        if self.__deque.empty():
            return None

        saved_value = self.__deque.tail().value
        self.__deque.delete_in_tail()
        return saved_value

    def size(self):
        return len(self.__deque)
