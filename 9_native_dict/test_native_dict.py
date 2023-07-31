import unittest
from unittest.mock import Mock

from native_dict import NativeDictionary


class TestNativeDictionary(unittest.TestCase):

    def test_init(self):
        native_dict = NativeDictionary(17)
        self.assertFalse(native_dict.is_key('FishKOH'))
        self.assertIsNone(native_dict.get('FishKOH'))
    
    def test_put(self):
        native_dict = NativeDictionary(17)
        
        native_dict.put('A', 10)
        self.assertTrue(native_dict.is_key('A'))
        self.assertEqual(native_dict.get('A'), 10)
        
        native_dict.put('B', 11)
        self.assertTrue(native_dict.is_key('B'))
        self.assertEqual(native_dict.get('B'), 11)
        
        native_dict.put('FishKOH', 'software-engineer')
        self.assertTrue(native_dict.is_key('FishKOH'))
        self.assertEqual(native_dict.get('FishKOH'), 'software-engineer')
        
        self.assertFalse(native_dict.is_key('F'))
        self.assertIsNone(native_dict.get('F'))
    
    def test_put_override(self):
        native_dict = NativeDictionary(17)
        
        native_dict.put('A', 10)
        self.assertTrue(native_dict.is_key('A'))
        self.assertEqual(native_dict.get('A'), 10)
        
        native_dict.put('A', 'it\'s capital char \'a\'')
        self.assertTrue(native_dict.is_key('A'))
        self.assertEqual(native_dict.get('A'), 'it\'s capital char \'a\'')
        
        native_dict.put('A', [True, False, True])
        self.assertTrue(native_dict.is_key('A'))
        self.assertEqual(native_dict.get('A'), [True, False, True])
           
    @unittest.mock.patch(
        "native_dict.NativeDictionary.hash_fun",
        Mock(return_value=16),
    )
    def test_put_collizion_override(self):
        native_dict = NativeDictionary(17)
        
        native_dict.put('A', 10)
        self.assertTrue(native_dict.is_key('A'))
        self.assertEqual(native_dict.get('A'), 10)
        
        native_dict.put('B', 11)
        self.assertTrue(native_dict.is_key('B'))
        self.assertEqual(native_dict.get('B'), 11)
        
        native_dict.put('A', 'is a')
        self.assertTrue(native_dict.is_key('A'))
        self.assertEqual(native_dict.get('A'), 'is a')
        
        native_dict.put('B', 'is b')
        self.assertTrue(native_dict.is_key('B'))
        self.assertEqual(native_dict.get('B'), 'is b')

