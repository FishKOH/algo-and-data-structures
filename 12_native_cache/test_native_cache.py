import unittest
from unittest.mock import Mock
from native_cache import NativeCache

class TestNativeCache(unittest.TestCase):

    @unittest.mock.patch(
        "native_cache.NativeCache.hash_fun",
        Mock(return_value=0),
    )
    def test_fullness(self):
        native_cache = NativeCache(3)
        native_cache.put('8', 8)
        native_cache.is_key('8')
        native_cache.get('8')
        native_cache.put('0', 0)
        native_cache.put('42', 42)
        native_cache.is_key('42')

        self.assertEqual(native_cache.hits, [3,1,2])
        self.assertTrue(native_cache.is_key('0'))
        self.assertTrue(native_cache.is_key('8'))
        self.assertTrue(native_cache.is_key('42'))
        
        native_cache.put('100', 100)
        self.assertFalse(native_cache.is_key('0'))        
        self.assertTrue(native_cache.is_key('100'))
        self.assertTrue(native_cache.is_key('8'))
        self.assertTrue(native_cache.is_key('42'))
