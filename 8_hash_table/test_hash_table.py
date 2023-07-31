import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def test_init(self):
        hash_table = HashTable(17, 3)
        self.assertIsNone(hash_table.find('FishKOH'))

    def test_put_same(self):
        hash_table_size = 17
        hash_table_step = 3
        hash_table = HashTable(hash_table_size, hash_table_step)
        
        s = 'same string'
        index = hash_table.seek_slot(s) #first index unknown
        self.assertIsNotNone(index)
        self.assertEqual(hash_table.put(s), index)
        for i in range(1, 4):
            with self.subTest(i=i):
                next_index = hash_table.seek_slot(s)
                self.assertIsNotNone(next_index)
                self.assertEqual(next_index, (index + i * hash_table_step) % hash_table_size)
                self.assertEqual(hash_table.put(s), next_index)
                self.assertEqual(hash_table.slots[next_index], s)
    
    def test_overput(self):
        hash_table_size = 17
        hash_table = HashTable(hash_table_size, 3)
        
        all_possible_indexies = set()
        for i in range(hash_table_size):
            all_possible_indexies.add(i)
        busy_indexes = set()
        
        for i in range(hash_table_size):
            s = str(i)
            with self.subTest(i=i):
                self.assertTrue(hash_table.hash_fun(s) < hash_table_size)
                seeked_index = hash_table.seek_slot(s)
                self.assertIsNotNone(hash_table.seek_slot(s))
                self.assertIsNotNone(hash_table.put(s))
                self.assertIsNotNone(hash_table.find(s))
                self.assertEqual(hash_table.slots[seeked_index], s)
                busy_indexes.add(seeked_index)
        self.assertEqual(all_possible_indexies, busy_indexes)
                
        self.assertIsNone(hash_table.seek_slot('FishKOH'))
        self.assertIsNone(hash_table.put('FishKOH'))
        self.assertIsNone(hash_table.find('FishKOH'))

