class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        finded_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                finded_nodes.append(node)
            node = node.next
        return finded_nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            next_node = node.next
            if node.value == val:
                if node.prev is not None:
                    node.prev.next = next_node
                else: # node is head
                    self.head = next_node
                if next_node is not None:
                    next_node.prev = node.prev
                else: # node is tail
                    self.tail = node.prev
                if not all:
                    return
            node = next_node

    def clean(self):
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

    def add_in_head(self, newNode):
        pass # здесь будет ваш код   
