import unittest
from simple_tree import SimpleTreeNode, SimpleTree

class TestSimpleTree(unittest.TestCase):
    
    def setUp(self):
        '''
        0
        | \
        1  2
        | \
        11 12
        '''
        self.root_node = SimpleTreeNode(0)
        self.tree = SimpleTree(self.root_node)

        self.node1 = SimpleTreeNode(1)
        self.node2 = SimpleTreeNode(2)
        self.tree.AddChild(self.root_node, self.node1)
        self.tree.AddChild(self.root_node, self.node2)

        self.node11 = SimpleTreeNode(11)
        self.node12 = SimpleTreeNode(12)
        self.tree.AddChild(self.node1, self.node11)
        self.tree.AddChild(self.node1, self.node12)

    def test_init_empty(self):
        tree = SimpleTree(None)
        self.assertIsNone(tree.Root)
    
    def test_init_root(self):
        root_node = SimpleTreeNode(0)
        tree = SimpleTree(root_node)
        self.assertEqual(tree.Root, root_node)

    def test_add(self):
        self.assertEqual(self.tree.Root.Children, [self.node1, self.node2])
        self.assertEqual(self.node1.Parent, self.root_node)
        self.assertEqual(self.node1.Children, [self.node11, self.node12])
        self.assertEqual(self.node2.Parent, self.root_node)
        self.assertEqual(self.node2.Children, [])
        self.assertEqual(self.node11.Parent, self.node1)
        self.assertEqual(self.node12.Parent, self.node1)

        # self.assertEqual(tree.Count(),5)
        # self.assertEqual(tree.LeafCount(),3)

    def test_delete_leaf(self):
        self.tree.DeleteNode(self.node2)
        
        self.assertEqual(self.tree.Root.Children, [self.node1])
        self.assertIsNone(self.node2.Parent)
    
    def test_delete_node_non_leaf(self):
        self.tree.DeleteNode(self.node1)
        
        self.assertEqual(self.tree.Root.Children, [self.node2])
        self.assertIsNone(self.node1.Parent)
    
    def test_get_all_nodes(self):
        self.assertEqual(set(self.tree.GetAllNodes()), {self.root_node, self.node1, self.node2, self.node11, self.node12})
    
    def test_find(self):
        self.assertEqual(self.tree.FindNodesByValue(0), [self.root_node])
        self.assertEqual(self.tree.FindNodesByValue(11), [self.node11])
        self.assertEqual(self.tree.FindNodesByValue(42), [])
        
        other_node = SimpleTreeNode(12)
        other_one_node = SimpleTreeNode(12)
        self.tree.AddChild(self.node1, other_node)
        self.tree.AddChild(self.node1, other_one_node)
        
        self.assertEqual(set(self.tree.FindNodesByValue(12)), {self.node12, other_node, other_one_node})
    
    def test_get_all_nodes_empty(self):
        tree = SimpleTree(None)
        self.assertEqual(tree.GetAllNodes(), [])
    
    def test_move(self):
        self.tree.MoveNode(self.node1, self.node2)
        
        self.assertEqual(self.tree.Root.Children, [self.node2])
        self.assertEqual(self.node1.Parent, self.node2)
        self.assertEqual(self.node2.Children, [self.node1])
        self.assertEqual(self.node1.Children, [self.node11, self.node12])
    
    def test_count(self):
        self.assertEqual(self.tree.Count(), 5)
        self.assertEqual(self.tree.LeafCount(), 3)

    def test_count_only_root(self):
        tree = SimpleTree(SimpleTreeNode(0))

        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.LeafCount(), 1)
    
    def test_count_empty(self):
        tree = SimpleTree(None)
        self.assertEqual(tree.Count(), 0)
        self.assertEqual(tree.LeafCount(), 0)
