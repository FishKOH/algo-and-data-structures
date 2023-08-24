import unittest

import os
import sys

script_dir = os.path.dirname(__file__)
bst_dir = os.path.join(script_dir, '..', '14_bst')
sys.path.append(bst_dir)
#learn correct way for import local modules
from bst import * #BST

from bbst import BalancedBST, BSTNode


class TestIsBalanced(unittest.TestCase):
  
    def test_lvl0(self):
        tree = BST(None)
        self.assertTrue(BalancedBST().IsBalanced(tree.Root))
        tree.AddKeyValue(42, '42')
        self.assertTrue(BalancedBST().IsBalanced(tree.Root))


    def test_lvl1(self):
        '''
        40
        | 
        20
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        self.assertTrue(BalancedBST().IsBalanced(tree.Root))

    def test_lvl2(self):
        '''
        40
        | \
        20 80
        |   
        10  
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        tree.AddKeyValue(10, '10')
        tree.AddKeyValue(80, '80')
        self.assertTrue(BalancedBST().IsBalanced(tree.Root))

    def test_lvl2_non_balanced(self):
        '''
        40
        | 
        20
        | 
        10
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        tree.AddKeyValue(10, '10')
        self.assertFalse(BalancedBST().IsBalanced(tree.Root))
    
    def test_lvl3(self):
        '''
        40
        |     \
        20     80
        | \    |
        10 32  64
        |
        8  
        '''
        tree = BST(None)
        tree.AddKeyValue(40, '40')
        tree.AddKeyValue(20, '20')
        tree.AddKeyValue(80, '80')
        tree.AddKeyValue(10, '10')
        tree.AddKeyValue(32, '32')
        tree.AddKeyValue(64, '64')
        tree.AddKeyValue(8, '8')
        self.assertTrue(BalancedBST().IsBalanced(tree.Root))
        tree.DeleteNodeByKey(64)
        self.assertFalse(BalancedBST().IsBalanced(tree.Root))

def nodes_to_keys(nodes):
    return [node.NodeKey for node in nodes]

class TestGenerateBalancedBST(unittest.TestCase):
    
    def setUp(self):
        self.tree = BalancedBST()
    
    def test_lvl0(self):
        array = [8]
        abst = [8]
        self.tree.GenerateTree(array)
        self.assertEqual(self.tree.Root.NodeKey, 8)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)
        
        bst = BST(self.tree.Root)
        self.assertEqual(nodes_to_keys(bst.BFS()), abst)

    def test_lvl1(self):
        array = [2, 4, 1]
        abst = [2, 1, 4]
        self.tree.GenerateTree(array)
        
        self.assertEqual(self.tree.Root.NodeKey, 2)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 1)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 4)
        self.assertEqual(self.tree.Root.LeftChild.Parent, self.tree.Root)
        self.assertEqual(self.tree.Root.RightChild.Parent, self.tree.Root)
        
        bst = BST(self.tree.Root)
        self.assertEqual(nodes_to_keys(bst.BFS()), abst)

    def test_lvl3(self):
        array = [1, 2, 4, 8, 16, 32, 64]
        abst = [8, 2, 32, 1, 4, 16, 64]
        self.tree.GenerateTree(array)
        bst = BST(self.tree.Root)
        self.assertEqual(nodes_to_keys(bst.BFS()), abst)

    def test_lvl3_nonfull4(self):
        array = [1, 2, 4, 8]
        abst = [4, 2, 8, 1]
        self.tree.GenerateTree(array)
        bst = BST(self.tree.Root)
        self.assertEqual(nodes_to_keys(bst.BFS()), abst)

    def test_lvl3_nonfull5(self):
        array = [1, 2, 4, 8, 16]
        abst = [4, 2, 16, 1, 8]
        self.tree.GenerateTree(array)
        bst = BST(self.tree.Root)
        self.assertEqual(nodes_to_keys(bst.BFS()), abst)

    def test_lvl3_nonfull6(self):
        array = [1, 2, 4, 8, 16, 32]
        abst = [8, 2, 32, 1, 4, 16]
        self.tree.GenerateTree(array)
        bst = BST(self.tree.Root)
        self.assertEqual(nodes_to_keys(bst.BFS()), abst)

    def tearDown(self):
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        bst = BST(self.tree.Root)
        for node in bst.DFS(PRE_ORDER):
            if node.Parent is not None:
                self.assertEqual(node.Parent.Level + 1, node.Level)
            if node.Parent is None:
                self.assertEqual(0, node.Level)
            
            if node.LeftChild is not None:
                self.assertTrue(node.LeftChild.NodeKey < node.NodeKey)
            if node.RightChild is not None:
                self.assertTrue(node.RightChild.NodeKey >= node.NodeKey)
