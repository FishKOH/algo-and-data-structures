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

class Stack:
    def __init__(self):
        # Time Complexity
        # |      | native_list/dynamic_array      | linked_list                   | doubly linked_list            |
        # | ---  | ---                            | ---                           | ---                           |
        # | tail | size O(1) pop O(1) push O(1)   | size O(N) pop O(N) push O(1)  | size O(N) pop O(1) push O(1)  |
        # | head | size O(1) pop O(N) push O(N)   | size O(N) pop O(1) push O(1)  | size O(N) pop O(1) push O(1)  |
        
        self.stack = LinkedList2()
        self.__size = 0 # optimize self.size() O(N) -> O(1)

    def size(self):
        return self.__size

    def pop(self):
        if self.stack.head() is None:
            return None

        saved_value = self.peek()
        self.stack.delete_in_head()
        self.__size -= 1
        return saved_value

    def push(self, value):
        self.stack.add_in_head(Node(value))
        self.__size += 1

    def peek(self):
        if self.stack.head() is None:
            return None

        return self.stack.head().value


class Stack_v0:
    def __init__(self):
        self.stack = LinkedList2() 

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack.tail() is None:
            return None

        saved_value = self.peek()
        self.stack.delete_in_tail()
        return saved_value

    def push(self, value):
        self.stack.add_in_tail(Node(value))     

    def peek(self):
        if self.stack.tail() is None:
            return None

        return self.stack.tail().value
