import unittest
from gen_bbst import GenerateBBSTArray

class TestGbst(unittest.TestCase):
  
    def test_lvl0(self):
        array = [8]
        abst = [8]
        self.assertEqual(GenerateBBSTArray(array), abst)

    def test_lvl1(self):
        array = [2, 4, 1]
        abst = [2, 1, 4]
        self.assertEqual(GenerateBBSTArray(array), abst)

    def test_lvl3(self):
        array = [1, 2, 4, 8, 16, 32, 64]
        abst = [8, 2, 32, 1, 4, 16, 64]
        self.assertEqual(GenerateBBSTArray(array), abst)

    def test_lvl3_nonfull4(self):
        array = [1, 2, 4, 8]
        abst = [4, 2, 8, 1, None, None, None]
        self.assertEqual(GenerateBBSTArray(array), abst)

    def test_lvl3_nonfull5(self):
        array = [1, 2, 4, 8, 16]
        abst = [4, 2, 16, 1, None, 8, None]
        self.assertEqual(GenerateBBSTArray(array), abst)

    def test_lvl3_nonfull6(self):
        array = [1, 2, 4, 8, 16, 32]
        abst = [8, 2, 32, 1, 4, 16, None]
        self.assertEqual(GenerateBBSTArray(array), abst)

