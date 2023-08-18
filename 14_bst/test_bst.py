import unittest
from bst import * #BST, BSTNode, BSTFind


class TestBSTRawInit(unittest.TestCase):
    
    def setUp(self):
        '''
        40
        | \
        20 80
        |   \
        10  160
        '''
        root = BSTNode(40, '40', None)
        
        node20 = BSTNode(20, '20', root)
        root.LeftChild = node20
        
        node10 = BSTNode(10, '10', node20)
        node20.LeftChild = node10
        
        node80 = BSTNode(80, '80', root)
        root.RightChild = node80
        
        node160 = BSTNode(160, '160', node80)
        node80.RightChild = node160
        
        self.tree = BST(root)
    
    def test_init(self):
        tree = self.tree
        self.assertIsNotNone(tree.Root)
        self.assertIsNotNone(tree.Root.LeftChild)
        self.assertIsNotNone(tree.Root.RightChild)
        self.assertEqual(tree.Root.NodeKey, 40)
        self.assertEqual(tree.Root.NodeValue, '40')
    
    def test_find_at_empty(self):
        tree = BST(None)
        bst_find = tree.FindNodeByKey(42)
        self.assertIsNone(bst_find.Node)
    
    def test_find_exisr_root(self):
        bst_find = self.tree.FindNodeByKey(40)
        self.assertEqual(bst_find.Node, self.tree.Root)
        self.assertTrue(bst_find.NodeHasKey)
    
    def test_find_exist_any_node(self):
        bst_find = self.tree.FindNodeByKey(10)
        self.assertIsNotNone(bst_find.Node)
        self.assertTrue(bst_find.NodeHasKey)
        self.assertEqual(bst_find.Node.NodeKey, 10)
    
    def test_find_non_exist_right(self):
        bst_find = self.tree.FindNodeByKey(30)
        self.assertIsNotNone(bst_find.Node)
        self.assertFalse(bst_find.NodeHasKey)
        self.assertEqual(bst_find.Node.NodeKey, 20)
        self.assertFalse(bst_find.ToLeft)
    
    def test_find_non_exist_left(self):
        bst_find = self.tree.FindNodeByKey(100)
        self.assertIsNotNone(bst_find.Node)
        self.assertFalse(bst_find.NodeHasKey)
        self.assertEqual(bst_find.Node.NodeKey, 160)
        self.assertTrue(bst_find.ToLeft)

class TestBSTAdd(unittest.TestCase):

   def test_add(self):
        tree = BST(None)
        self.assertTrue(tree.AddKeyValue(40, '40'))
        self.assertIsNotNone(tree.Root)
        self.assertEqual(tree.Root.NodeKey, 40)
        self.assertEqual(tree.Root.NodeValue, '40')
        self.assertIsNone(tree.Root.Parent)
        self.assertIsNone(tree.Root.LeftChild)
        self.assertIsNone(tree.Root.RightChild)
        
        self.assertTrue(tree.AddKeyValue(20, '20'))
        self.assertIsNotNone(tree.Root.LeftChild)
        node20 = tree.Root.LeftChild
        self.assertEqual(node20.NodeKey, 20)
        self.assertEqual(node20.NodeValue, '20')
        self.assertEqual(node20.Parent, tree.Root)
        self.assertIsNone(node20.LeftChild)
        self.assertIsNone(node20.RightChild)
        
        self.assertTrue(tree.AddKeyValue(30, '30'))
        self.assertIsNotNone(node20.RightChild)
        node30 = node20.RightChild
        self.assertEqual(node30.NodeKey, 30)
        self.assertEqual(node30.NodeValue, '30')
        self.assertEqual(node30.Parent, node20)
        self.assertIsNone(node30.LeftChild)
        self.assertIsNone(node30.RightChild)
        
        self.assertFalse(tree.AddKeyValue(40, '4040'))
        self.assertIsNotNone(tree.Root)
        self.assertEqual(tree.Root.NodeKey, 40)
        self.assertEqual(tree.Root.NodeValue, '40')
        self.assertIsNone(tree.Root.Parent)
        self.assertIsNotNone(tree.Root.LeftChild)
        self.assertIsNone(tree.Root.RightChild)
        
class TestBST(unittest.TestCase):
    
    def setUp(self):
        '''
        40
        | \
        20 80
        |   \
        10  160
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        tree.AddKeyValue(10, '10')
        tree.AddKeyValue(80, '80')
        tree.AddKeyValue(160, '160')
        
        self.tree = tree
    
    def test_find_min_max_at_empty(self):
        tree = BST(None)
        self.assertIsNone(tree.FinMinMax(FromNode=tree.Root, FindMax=True))
        self.assertIsNone(tree.FinMinMax(FromNode=tree.Root, FindMax=False))
    
    def test_find_min_max_from_root(self):
        max_node = self.tree.FindMinMax(FromNode=self.tree.Root, FindMax=True)
        self.assertEqual(max_node.NodeKey, 160)
        
        min_node = self.tree.FindMinMax(FromNode=self.tree.Root, FindMax=False)
        self.assertEqual(min_node.NodeKey, 10)
    
    def test_find_min_max_from_non_root(self):
        node20 = self.tree.FindNodeByKey(20).Node
        
        max_node = self.tree.FindMinMax(FromNode=node20, FindMax=True)
        self.assertEqual(max_node.NodeKey, 20)
        
        min_node = self.tree.FindMinMax(FromNode=node20, FindMax=False)
        self.assertEqual(min_node.NodeKey, 10)

# def isunconnected(node : BSTNode):
#     return all(con_node is None for con_node in [node.Parent, node.LeftChild, node.RightChild])

class TestBSTDelete(unittest.TestCase):
    
    def setUp(self):
        '''
        40
        | \
        20 80
        |   | \
        10  42 160
                 \
                  500
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        tree.AddKeyValue(80, '80')
        tree.AddKeyValue(10, '10')
        tree.AddKeyValue(42, '42')
        tree.AddKeyValue(160, '160')
        tree.AddKeyValue(500, '500')
        
        self.tree = tree
    
    def test_delete_at_empty(self):
        tree = BST(None)
        self.assertFalse(tree.DeleteNodeByKey(-1))
    
    def test_delete_single_root(self):
        tree = BST(None)
        tree.AddKeyValue(-1, '----1')
        self.assertTrue(tree.DeleteNodeByKey(-1))
        self.assertIsNone(tree.Root)

    def test_delete_root(self):
        tree = self.tree
        self.assertTrue(tree.DeleteNodeByKey(40))
        '''
        42
        | \
        20 80
        |     \
        10    160
                 \
                  500
        '''
        self.assertFalse(tree.FindNodeByKey(40).NodeHasKey)
        
        self.assertIsNotNone(tree.Root)
        self.assertIsNone(tree.Root.Parent)
        
        node42 = tree.FindNodeByKey(42).Node
        node20 = tree.FindNodeByKey(20).Node
        node80 = tree.FindNodeByKey(80).Node
        self.assertEqual(tree.Root, node42)
        self.assertEqual(tree.Root.LeftChild, node20)
        self.assertEqual(tree.Root.RightChild, node80)
        self.assertEqual(node20.Parent, node42)
        self.assertEqual(node80.Parent, node42)
        self.assertIsNone(node80.LeftChild)
        
    def test_delete_non_exist(self):
        self.assertFalse(self.tree.DeleteNodeByKey(-1))
        #TODO: check that nothing happened
    
    def test_delete_node_with_only_left(self):
        tree = self.tree
        self.assertTrue(tree.DeleteNodeByKey(20))
        self.assertFalse(tree.FindNodeByKey(20).NodeHasKey)
        '''
        40
        | \
        10 80
           |  \
           42  160
                 \
                  500
        '''
        node10 = tree.FindNodeByKey(10).Node
        self.assertEqual(node10.Parent, tree.Root)
        self.assertEqual(tree.Root.LeftChild, node10)
        
    
    def test_delete_node_with_only_right(self):
        tree = self.tree
        self.assertTrue(tree.DeleteNodeByKey(160))
        self.assertFalse(tree.FindNodeByKey(160).NodeHasKey)
        '''
        40
        | \
        20 80
        |   | \
        10  42 500
        '''
        node80  = tree.FindNodeByKey(80).Node
        node500 = tree.FindNodeByKey(500).Node
        self.assertEqual(node80.RightChild, node500)
        self.assertEqual(node500.Parent, node80)
    
    def test_delete_complex(self):
        tree = self.tree
        self.assertTrue(tree.DeleteNodeByKey(80))
        self.assertFalse(tree.FindNodeByKey(80).NodeHasKey)
        '''
        40
        | \
        20 160
        |   | \
        10  42 500
        '''
        node160 = tree.FindNodeByKey(160).Node
        node42  = tree.FindNodeByKey(42).Node
        node500 = tree.FindNodeByKey(500).Node
        self.assertEqual(tree.Root.RightChild, node160)
        self.assertEqual(node160.Parent,     tree.Root)
        self.assertEqual(node160.LeftChild,  node42)
        self.assertEqual(node160.RightChild, node500)
        self.assertEqual(node42.Parent,  node160)
        self.assertEqual(node500.Parent, node160)
        
        self.assertTrue(tree.DeleteNodeByKey(160))
        self.assertFalse(tree.FindNodeByKey(160).NodeHasKey)
        '''
        40
        | \
        20 500
        |   | 
        10  42
        '''
        self.assertEqual(tree.Root.RightChild, node500)
        self.assertEqual(node500.Parent,     tree.Root)
        self.assertEqual(node500.LeftChild,  node42)
        self.assertIsNone(node500.RightChild)
        self.assertEqual(node42.Parent,  node500)
    
    def test_delete_leaf(self):
        tree = self.tree
        self.assertTrue(tree.DeleteNodeByKey(10))
        self.assertFalse(tree.FindNodeByKey(10).NodeHasKey)
        '''
        40
        | \
        20 80
            | \
            42 160
                 \
                  500
        '''
        node20 = tree.FindNodeByKey(20).Node
        self.assertIsNone(node20.LeftChild)
        self.assertIsNone(node20.RightChild)

class TestBSTCount(unittest.TestCase):
    
    def test_count(self):
        tree = BST(None)
        self.assertEqual(tree.Count(), 0)
        tree.AddKeyValue(40, '40')
        self.assertEqual(tree.Count(), 1)
        tree.AddKeyValue(20, '20')
        self.assertEqual(tree.Count(), 2)
        tree.AddKeyValue(80, '80')
        self.assertEqual(tree.Count(), 3)
        tree.AddKeyValue(10, '10')
        self.assertEqual(tree.Count(), 4)
        tree.AddKeyValue(42, '42')
        self.assertEqual(tree.Count(), 5)
        tree.AddKeyValue(160, '160')
        self.assertEqual(tree.Count(), 6)
        tree.AddKeyValue(500, '500')
        self.assertEqual(tree.Count(), 7)

def nodes_to_keys(nodes):
    return [node.NodeKey for node in nodes]

class TestBST_Search(unittest.TestCase):
    
    def setUp(self):
        '''
        40
        | \
        20 80
        |   | \
        10  42 160
                 \
                  500
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        tree.AddKeyValue(80, '80')
        tree.AddKeyValue(10, '10')
        tree.AddKeyValue(42, '42')
        tree.AddKeyValue(160, '160')
        tree.AddKeyValue(500, '500')
        
        self.tree = tree
    
    def test_bfs(self):
        self.assertEqual(nodes_to_keys(self.tree.BFS()), 
        [40, 20, 80, 10, 42, 160, 500])
    
    def test_bfs_at_empty(self):
        tree = BST(None)
        self.assertEqual(nodes_to_keys(tree.BFS()), [])

    def test_dfs_in_order(self):
        self.assertEqual(nodes_to_keys(self.tree.DFS(IN_ORDER)), 
        [10, 20, 40, 42, 80, 160, 500])

    def test_dfs_post_order(self):
        self.assertEqual(nodes_to_keys(self.tree.DFS(POST_ORDER)), 
        [10, 20, 42, 500, 160, 80, 40])

    def test_dfs_pre_order(self):
        self.assertEqual(nodes_to_keys(self.tree.DFS(PRE_ORDER)), 
        [40, 20, 10, 80, 42, 160, 500])
    
    def test_dfs_at_empty(self):
        tree = BST(None)
        self.assertEqual(nodes_to_keys(tree.DFS(IN_ORDER)), [])

