import unittest

from deque import Deque

def is_palindrome_deq(deq : Deque) -> bool:
    while deq.size() > 1:
        if deq.removeFront() != deq.removeTail():
            return False
    return True
    

def is_palindrome(s : str) -> bool:
    deq = Deque()
    for c in s:
       deq.addTail(c) 
    return is_palindrome_deq(deq)

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('ABBA'))
        self.assertTrue(is_palindrome('abrarba'))
        self.assertTrue(is_palindrome('amanaplanacaddyoreroyddacanalpanama'))
        self.assertFalse(is_palindrome('core'))
        self.assertFalse(is_palindrome('FishKOH'))
        self.assertFalse(is_palindrome('abraqba'))
