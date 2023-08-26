class Vertex:

    def __init__(self, val : int):
        self.Value = val
  
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
	
    def RemoveVertex(self, idx_v : int):
        if idx_v >= self.max_vertex and self.vertex[idx_v] is not None:
            return
        
        self.vertex[idx_v] = None
        self.m_adjacency[idx_v] = [0] * self.max_vertex
        for i in range(self.max_vertex):
            self.m_adjacency[i][idx_v] = 0
	
    def IsEdge(self, idx_v1 : int, idx_v2 : int):
        if idx_v1 >= self.max_vertex or idx_v2 >= self.max_vertex:
            return False
        
        return self.m_adjacency[idx_v1][idx_v2] == 1
	
    def AddEdge(self, idx_v1 : int, idx_v2 : int):
        if ((idx_v1 >= self.max_vertex or idx_v2 >= self.max_vertex) or 
            self.vertex[idx_v1] is None or 
            self.vertex[idx_v2] is None):
            return
        
        self.m_adjacency[idx_v1][idx_v2] = 1
        self.m_adjacency[idx_v2][idx_v1] = 1
	
    def RemoveEdge(self, idx_v1 : int, idx_v2 : int):
        if (idx_v1 >= self.max_vertex or idx_v2 >= self.max_vertex):
            return
        
        self.m_adjacency[idx_v1][idx_v2] = 0
        self.m_adjacency[idx_v2][idx_v1] = 0
