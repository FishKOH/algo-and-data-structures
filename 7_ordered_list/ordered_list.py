class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc : bool):
        self.head = None
        self.tail = None
        self.__ascending = asc # True - ascending(head < tail), False - descending(head > tail)

    def compare(self, v1, v2):
        assert isinstance(v1, int) and isinstance(v2, int)
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1 # v1 > v2

    def empty(self):
        return self.head is None

    def __add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def __add_in_head(self, newNode):
        if self.empty():
            self.__add_in_tail(newNode)
        else:
            # newNode.prev = None # don't guarantee
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def __insert(self, afterNode, newNode):
        if afterNode is None:
            self.__add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            if newNode.next is None: #afterNode was tail
                self.tail = newNode
            else:
                newNode.next.prev = newNode

    # v1 is after v2 
    def __is_after(self, v1, v2):
        after_compare_result = 1 if self.__ascending else -1
        return self.compare(v1, v2) == after_compare_result

    # v1 is after v2 or v1 == v2
    def __is_after_or_same(self, v1, v2):
        after_compare_result = 1 if self.__ascending else -1
        cmp_result = self.compare(v1, v2)
        return cmp_result == after_compare_result or cmp_result == 0

    def add(self, value):
        # Time Complexity O(N)
        node = self.head
        while node is not None and self.__is_after(value, node.value):
            node = node.next
        
        if node == self.head:
            self.__add_in_head(Node(value))
        elif node is None:
            self.__add_in_tail(Node(value))
        else:    
            self.__insert(node.prev, Node(value))

    def find(self, val):
        # Time Complexity O(N)
        node = self.head
        while node is not None and self.__is_after_or_same(val, node.value):
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        # Time Complexity O(N)
        node = self.head
        while node is not None and self.__is_after_or_same(val, node.value):
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
                return
            node = next_node

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        node_count = 0
        node = self.head
        while node is not None:
            node_count += 1
            node = node.next
        return node_count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        assert isinstance(v1, str) and isinstance(v2, str)
        stripped_v1 = v1.strip()
        stripped_v2 = v2.strip()
        if stripped_v1 < stripped_v2:
            return -1
        if stripped_v1 == stripped_v2:
            return 0
        return 1 # stripped_v1 > stripped_v2
