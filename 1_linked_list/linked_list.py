class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        prev_node = None
        while node is not None:
            next_node = node.next
            if node.value == val:
                if self.head == self.tail: # singleitem
                    self.head = None
                    self.tail = None
                elif next_node is None: # node is tail
                    prev_node.next = next_node
                    self.tail = prev_node
                else:
                    if self.head == node:
                        self.head = next_node
                    else:
                        prev_node.next = next_node
                        
                if not all:
                    return
            else:
                prev_node = node
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
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            next_after_node = afterNode.next
            afterNode.next = newNode
            newNode.next = next_after_node
            if next_after_node is None:
                self.tail = newNode
