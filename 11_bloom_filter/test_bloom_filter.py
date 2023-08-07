import unittest
from bloom_filter import BloomFilter, BitArray

class TestBitArray(unittest.TestCase):

    def test_init(self):
        bits = BitArray(32)
        self.assertEqual(bits.bit(0), 0)
        self.assertEqual(bits.bit(8), 0)
        self.assertEqual(bits.bit(31), 0)

    def test_set(self):
        bits = BitArray(32)
        bits.set_bit(0)
        bits.set_bit(31)
        self.assertEqual(bits.bit(0), 1)
        self.assertEqual(bits.bit(8), 0)
        self.assertEqual(bits.bit(31), 1)
        
    def test_reset(self):
        bits = BitArray(32)
        bits.set_bit(0)
        bits.set_bit(31)
        bits.reset_bit(31)
        self.assertEqual(bits.bit(0), 1)
        self.assertEqual(bits.bit(31), 0)        


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        init_str = '0123456789'
        self.test_strings = [init_str[i:]+init_str[:i] for i in range(10)]

    def test_one_elem(self):
        bloom_filter = BloomFilter(32)
        self.assertFalse(bloom_filter.is_value('FishKOH'))
        self.assertFalse(bloom_filter.is_value(self.test_strings[0]))
        
        bloom_filter.add(self.test_strings[0])
        self.assertTrue(bloom_filter.is_value(self.test_strings[0]))
                

    def test_full(self):
        bloom_filter = BloomFilter(32)
        for s in self.test_strings:
            bloom_filter.add(s)
        
        for s in self.test_strings:
            with self.subTest(s=s):
                self.assertTrue(bloom_filter.is_value(s))


