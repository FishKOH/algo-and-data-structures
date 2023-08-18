import unittest
from abst import aBST

class TestABST(unittest.TestCase):
    
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
        tree = aBST(4)
        tree.Tree = [40, 20, 80, 10, None, 42, 160, None, None, None, None, None, None, None, 500]

        self.tree = tree
    
    def test_init(self):
        tree = aBST(3)
        self.assertEqual(len(tree.Tree), 15)
        tree = aBST(0)
        self.assertEqual(len(tree.Tree), 1)
        tree = aBST(1)
        self.assertEqual(len(tree.Tree), 3)
    
    def test_find_at_empty(self):
        tree = aBST(4)
        self.assertEqual(tree.FindKeyIndex(42), 0)
    
    def test_find_exist(self):
        tree = self.tree
        self.assertEqual(tree.FindKeyIndex(40), 0)
        self.assertEqual(tree.FindKeyIndex(20), 1)
        self.assertEqual(tree.FindKeyIndex(10), 3)
        self.assertEqual(tree.FindKeyIndex(80), 2)
        self.assertEqual(tree.FindKeyIndex(42), 5)
        self.assertEqual(tree.FindKeyIndex(160), 6)
        self.assertEqual(tree.FindKeyIndex(500), 14)
    
    def test_find_non_exist(self):
        self.assertEqual(self.tree.FindKeyIndex(100), -13)
        self.assertEqual(self.tree.FindKeyIndex(30), -4)  
    
    def test_find_partially_full(self):
        self.assertIsNone(self.tree.FindKeyIndex(499))

class TestBSTAdd(unittest.TestCase):

    def setUp(self):
        '''
        40
        | \
        20 80
        |   | \
        10  42 160
                 \
                  500
        [40, 20, 80, 10, None, 42, 160, None, None, None, None, None, None, None, 500]
        '''
        tree = aBST(3)
        tree.AddKey(40)
        tree.AddKey(20)
        tree.AddKey(10)
        tree.AddKey(80)
        tree.AddKey(42)
        tree.AddKey(160)
        tree.AddKey(500)
        
        self.tree = tree

    def test_add_new_keys(self):
        tree = aBST(3)
        self.assertEqual(tree.AddKey(40), 0)
        self.assertEqual(tree.AddKey(20), 1)
        self.assertEqual(tree.AddKey(10), 3)
        self.assertEqual(tree.AddKey(80), 2)
        self.assertEqual(tree.AddKey(42), 5)
        self.assertEqual(tree.AddKey(160), 6)
        self.assertEqual(tree.AddKey(500), 14)
    
    def test_add_exist_keys(self):
        self.assertEqual(self.tree.AddKey(40), 0)
        self.assertEqual(self.tree.AddKey(20), 1)
        self.assertEqual(self.tree.AddKey(10), 3)
    
    def test_add_partially_full(self):
        self.assertEqual(self.tree.AddKey(499), -1)
        self.assertEqual(self.tree.AddKey(501), -1)

