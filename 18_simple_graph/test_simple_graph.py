import unittest
from simple_graph import SimpleGraph, Vertex

class TestGraph(unittest.TestCase):

    def setUp(self):
        graph = SimpleGraph(3)
        graph.AddVertex(42)
        graph.AddVertex(8)
        graph.AddVertex(-1)
        
        self.graph = graph

    def test_init(self):
        graph = SimpleGraph(3)
        for v1 in range(3):
            for v2 in range(3):
                with self.subTest(vv = (v1, v2)):
                    self.assertFalse(graph.IsEdge(v1,v2))
    
    def test_add_vertex(self):
        graph = self.graph
        
        self.assertEqual(graph.vertex[0].Value, 42)
        self.assertEqual(graph.vertex[1].Value, 8)
        self.assertEqual(graph.vertex[2].Value, -1)
        for v1 in range(3):
            for v2 in range(3):
                with self.subTest(vv = (v1, v2)):
                    self.assertFalse(graph.IsEdge(v1,v2))
    
    def test_add_vertex_full(self):
        graph = self.graph
        graph.AddVertex(1234)
        # not added
        self.assertEqual(graph.vertex[0].Value, 42)
        self.assertEqual(graph.vertex[1].Value, 8)
        self.assertEqual(graph.vertex[2].Value, -1)
    
    def test_add_edge(self):
        graph = self.graph
        
        self.assertFalse(graph.IsEdge(0,1))
        self.assertFalse(graph.IsEdge(1,0))
        graph.AddEdge(0,1)
        self.assertTrue(graph.IsEdge(0,1))
        self.assertTrue(graph.IsEdge(1,0))

        self.assertFalse(graph.IsEdge(0,2))
        self.assertFalse(graph.IsEdge(2,0))        
        graph.AddEdge(0,2)
        self.assertTrue(graph.IsEdge(0,2))
        self.assertTrue(graph.IsEdge(2,0))
        
        self.assertFalse(graph.IsEdge(2,2))
        graph.AddEdge(2,2)
        self.assertTrue(graph.IsEdge(2,2))
    
    def test_remove_edge(self):
        graph = self.graph
        
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(2,2)
        
        self.assertTrue(graph.IsEdge(0,1))
        self.assertTrue(graph.IsEdge(1,0))
        self.assertTrue(graph.IsEdge(0,2))
        self.assertTrue(graph.IsEdge(2,0))
        self.assertTrue(graph.IsEdge(2,2))
        self.assertFalse(graph.IsEdge(1,2))
        self.assertFalse(graph.IsEdge(2,1))
        
        graph.RemoveEdge(1, 0)
        self.assertFalse(graph.IsEdge(0,1))
        self.assertFalse(graph.IsEdge(1,0))
        
        graph.RemoveEdge(2, 2)
        self.assertFalse(graph.IsEdge(2,2))
    
    def test_remove_vertex(self):
        graph = self.graph
        
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(2,2)
        
        self.assertTrue(graph.IsEdge(0,1))
        self.assertTrue(graph.IsEdge(1,0))
        self.assertTrue(graph.IsEdge(0,2))
        self.assertTrue(graph.IsEdge(2,0))
        
        graph.RemoveVertex(0)
        self.assertIsNone(graph.vertex[0])
        self.assertFalse(graph.IsEdge(0,1))
        self.assertFalse(graph.IsEdge(1,0))
        self.assertFalse(graph.IsEdge(0,2))
        self.assertFalse(graph.IsEdge(2,0))

    def test_add_after_remove_vertex(self):
        graph = self.graph
        
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(2,2)
        graph.RemoveVertex(0)
        graph.AddVertex(512)
        self.assertEqual(graph.vertex[0].Value, 512)
        
        graph.AddEdge(2, 0)
        self.assertTrue(graph.IsEdge(0,2))
        self.assertTrue(graph.IsEdge(2,0))


class TestDfs(unittest.TestCase):

    def test_simple(self):
        graph = SimpleGraph(3)
        graph.AddVertex(42)
        graph.AddVertex(8)
        graph.AddVertex(-1)
        
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(2,2)
        self.assertEqual(graph.DepthFirstSearch(1,2), [graph.vertex[1], graph.vertex[0], graph.vertex[2]])
        graph.RemoveEdge(2, 0)
        self.assertEqual(graph.DepthFirstSearch(1,2), [])
        
        self.assertEqual(graph.DepthFirstSearch(2,2), [graph.vertex[2]])
        graph.RemoveEdge(2, 2)
        self.assertEqual(graph.DepthFirstSearch(2,2), [])
    
    def test_complex(self):
        graph = SimpleGraph(5)
        for i in range(5):
            graph.AddVertex(i)
        
        graph.AddEdge(0,1)
        graph.AddEdge(1,2)
        graph.AddEdge(2,3)
        graph.AddEdge(3,4)
        
        graph.AddEdge(0,2)
        graph.AddEdge(2,4)
        
        self.assertEqual(graph.DepthFirstSearch(0,4), [graph.vertex[0], graph.vertex[1], graph.vertex[2], graph.vertex[4]])
        graph.RemoveEdge(1, 2)
        self.assertEqual(graph.DepthFirstSearch(0,4), [graph.vertex[0], graph.vertex[2], graph.vertex[4]])
        graph.RemoveEdge(0, 2)
        self.assertEqual(graph.DepthFirstSearch(0,4), [])

class TestBfs(unittest.TestCase):

    def test_simple(self):
        graph = SimpleGraph(3)
        graph.AddVertex(42)
        graph.AddVertex(8)
        graph.AddVertex(-1)
        
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(2,2)
        self.assertEqual(graph.BreadthFirstSearch(1,2), [graph.vertex[1], graph.vertex[0], graph.vertex[2]])
        graph.RemoveEdge(2, 0)
        self.assertEqual(graph.BreadthFirstSearch(1,2), [])
        
        self.assertEqual(graph.BreadthFirstSearch(2,2), [graph.vertex[2]])
        graph.RemoveEdge(2, 2)
        self.assertEqual(graph.BreadthFirstSearch(2,2), [])
    
    def test_complex(self):
        graph = SimpleGraph(5)
        for i in range(5):
            graph.AddVertex(i)
        
        graph.AddEdge(0,1)
        graph.AddEdge(1,2)
        graph.AddEdge(2,3)
        graph.AddEdge(3,4)
        
        graph.AddEdge(0,2)
        graph.AddEdge(2,4)
        
        self.assertEqual(graph.BreadthFirstSearch(0,4), [graph.vertex[0], graph.vertex[2], graph.vertex[4]])
        graph.RemoveEdge(0, 2)
        self.assertEqual(graph.BreadthFirstSearch(0,4), [graph.vertex[0], graph.vertex[1], graph.vertex[2], graph.vertex[4]])
        graph.RemoveEdge(2, 4)
        self.assertEqual(graph.BreadthFirstSearch(0,4), [graph.vertex[0], graph.vertex[1], graph.vertex[2], graph.vertex[3], graph.vertex[4]])
        graph.RemoveEdge(0, 1)
        self.assertEqual(graph.BreadthFirstSearch(0,4), [])
        
class TestWeakVertices(unittest.TestCase):

    def test_one_triangle(self):
        graph = SimpleGraph(3)
        for i in range(3):
            graph.AddVertex(i)
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(1,2)
        
        self.assertEqual(graph.WeakVertices(), [])
    
    def test_one_triangle_one_vertex(self):
        graph = SimpleGraph(4)
        for i in range(4):
            graph.AddVertex(i)
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(1,2)
        graph.AddEdge(2,3)
        
        self.assertEqual(graph.WeakVertices(), [graph.vertex[3]])
    
    def test_two_triangle(self):
        graph = SimpleGraph(6)
        for i in range(6):
            graph.AddVertex(i)
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(1,2)
        graph.AddEdge(3,4)
        graph.AddEdge(3,5)
        graph.AddEdge(4,5)
        
        self.assertEqual(graph.WeakVertices(), [])
    
    def test_complex(self):
        graph = SimpleGraph(9)
        for i in range(9):
            graph.AddVertex(i)
        graph.AddEdge(0,1)
        graph.AddEdge(0,2)
        graph.AddEdge(1,2)
        graph.AddEdge(1,3)
        graph.AddEdge(2,3)
        
        graph.AddEdge(4,5)
        graph.AddEdge(4,6)
        graph.AddEdge(5,6)
        
        graph.AddEdge(2,4)
        
        graph.AddEdge(0,7)
        graph.AddEdge(4,7)
        graph.AddEdge(6,8)
        
        self.assertEqual(graph.WeakVertices(), [graph.vertex[7], graph.vertex[8]])
