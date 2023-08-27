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
    
    def DepthFirstSearch(self, idx_v_from, idx_v_to):
        if not self.__exist(idx_v_from) or not self.__exist(idx_v_to):
            return []
        
        def __dfs_recursive(idx_cur_v, idx_search_v, path_as_stack):
            self.vertex[idx_cur_v].Hit = True
            path_as_stack.append(idx_cur_v)
            if self.m_adjacency[idx_cur_v][idx_search_v] == 1:
                if idx_cur_v != idx_search_v:
                    path_as_stack.append(idx_search_v)
                return
            for idx in range(self.max_vertex):
                if self.m_adjacency[idx_cur_v][idx] and self.vertex[idx].Hit == False:
                    __dfs_recursive(idx, idx_search_v, path_as_stack)
                    if path_as_stack[-1] == idx_search_v: # check -1 exist
                        return
            
            path_as_stack.pop()
            if len(path_as_stack) == 0:
                return
        
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        
        path_as_stack = []
        __dfs_recursive(idx_v_from, idx_v_to, path_as_stack)
        return [self.vertex[idx] for idx in path_as_stack]

