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

class Vertex:

    def __init__(self, val : int):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:
    
    def __init__(self, size : int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v : int):
        if None not in self.vertex:
            return
        
        free_index = self.vertex.index(None)
        self.vertex[free_index] = Vertex(v)
    
    def __exist(self, idx_v : int):
        return idx_v >=0 and idx_v < self.max_vertex and self.vertex[idx_v] is not None
    
    def RemoveVertex(self, idx_v : int):
        if not self.__exist(idx_v):
            return
        
        self.vertex[idx_v] = None
        self.m_adjacency[idx_v] = [0] * self.max_vertex
        for i in range(self.max_vertex):
            self.m_adjacency[i][idx_v] = 0
    
    def IsEdge(self, idx_v1 : int, idx_v2 : int):
        if not self.__exist(idx_v1) or not self.__exist(idx_v2):
            return False
        
        return self.m_adjacency[idx_v1][idx_v2] == 1
    
    def AddEdge(self, idx_v1 : int, idx_v2 : int):
        if not self.__exist(idx_v1) or not self.__exist(idx_v2):
            return
        
        self.m_adjacency[idx_v1][idx_v2] = 1
        self.m_adjacency[idx_v2][idx_v1] = 1
    
    def RemoveEdge(self, idx_v1 : int, idx_v2 : int):
        if not self.__exist(idx_v1) or not self.__exist(idx_v2):
            return
        
        self.m_adjacency[idx_v1][idx_v2] = 0
        self.m_adjacency[idx_v2][idx_v1] = 0
    
    def __prepare_search(self):
        for v in self.vertex:
                if v is not None:
                    v.Hit = False
    
    def __dfs_recursive(self, idx_cur_v, idx_search_v, path_as_stack):
        self.vertex[idx_cur_v].Hit = True
        path_as_stack.append(idx_cur_v)
        if self.m_adjacency[idx_cur_v][idx_search_v] == 1:
            if idx_cur_v != idx_search_v:
                path_as_stack.append(idx_search_v)
            return
        for idx in range(self.max_vertex):
            if self.m_adjacency[idx_cur_v][idx] == 1 and self.vertex[idx].Hit == False:
                self.__dfs_recursive(idx, idx_search_v, path_as_stack)
                if path_as_stack[-1] == idx_search_v: # check -1 exist
                    return
        
        path_as_stack.pop()
        if len(path_as_stack) == 0:
            return
    
    def DepthFirstSearch(self, idx_v_from, idx_v_to):
        if not self.__exist(idx_v_from) or not self.__exist(idx_v_to):
            return []
        
        self.__prepare_search()
        
        path_as_stack = []
        self.__dfs_recursive(idx_v_from, idx_v_to, path_as_stack)
        return [self.vertex[idx] for idx in path_as_stack]
    
    def BreadthFirstSearch(self, idx_v_from, idx_v_to):
        if not self.__exist(idx_v_from) or not self.__exist(idx_v_to):
            return []
        
        self.__prepare_search()
        
        parents = [None] * self.max_vertex
        
        idx_v_q = Queue()
        idx_v_q.enqueue(idx_v_from)
        self.vertex[idx_v_from].Hit = True
        while idx_v_q.size() != 0:
            cur_idx = idx_v_q.dequeue()
            if self.m_adjacency[cur_idx][idx_v_to] == 1:
                parents[idx_v_to] = cur_idx
                break
            for idx in range(self.max_vertex):
                if self.m_adjacency[cur_idx][idx] == 1 and self.vertex[idx].Hit == False:
                    idx_v_q.enqueue(idx)
                    self.vertex[idx].Hit = True
                    parents[idx] = cur_idx
        
        if parents[idx_v_to] is None:
            return []        
        
        path = [idx_v_to]
        idx = idx_v_to
        while idx != idx_v_from:
            idx = parents[idx]
            path.append(idx)
        return [self.vertex[idx] for idx in reversed(path)]
        
