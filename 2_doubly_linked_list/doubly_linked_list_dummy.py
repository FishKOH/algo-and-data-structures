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

    def find(self, val):
        node = self.head()
        while isinstance(node, Node):
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        finded_nodes = []
        node = self.head()
        while isinstance(node, Node):
            if node.value == val:
                finded_nodes.append(node)
            node = node.next
        return finded_nodes

    def delete(self, val, all=False):
        node = self.head()
        while isinstance(node, Node):
            next_node = node.next
            if node.value == val:
                self.__delete(node)
                if not all:
                    return
            node = next_node

    def clean(self):
        self.__dummy_head.next = self.__dummy_head
        self.__dummy_head.prev = self.__dummy_head

    def len(self):
        node_count = 0
        node = self.head()
        while isinstance(node, Node):
            node_count += 1
            node = node.next
        return node_count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            self.__insert(afterNode, newNode)

    def add_in_head(self, newNode):
        if self.empty():
            self.add_in_tail(newNode)
        else:
            self.__insert(self.__dummy_head, newNode)
