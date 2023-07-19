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
        self.head = None
        self.tail = None

    def len(self):
        node_count = 0
        node = self.head
        while node is not None:
            node_count += 1
            node = node.next
        return node_count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            if newNode.next is None: #afterNode was tail
                self.tail = newNode
            else:
                newNode.next.prev = newNode

    def add_in_head(self, newNode):
        if self.empty():
            self.add_in_tail(newNode)
        else:
            # newNode.prev = None # don't guarantee
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def empty(self):
        return self.head is None
