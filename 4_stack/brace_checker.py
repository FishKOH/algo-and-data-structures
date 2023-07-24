import unittest
from stack import Stack

def is_balansed_braces(braces):
    braces_stack = Stack()
    for brace in braces:
        if brace == '(':
            braces_stack.push(brace)
        else: # brace == ')'
            if braces_stack.pop() is None:
                return False
    return braces_stack.size() == 0


class TestBraceChecker(unittest.TestCase):
    
    def test_empty_braces(self):
        self.assertTrue(is_balansed_braces(''))
    
    def test_balansed_braces(self):
        self.assertTrue(is_balansed_braces('()'))
        self.assertTrue(is_balansed_braces('()()'))
        self.assertTrue(is_balansed_braces('(())'))
        self.assertTrue(is_balansed_braces('(())()'))
        self.assertTrue(is_balansed_braces('(()((())()))'))
    
    def test_unbalansed_braces(self):
        self.assertFalse(is_balansed_braces('('))
        self.assertFalse(is_balansed_braces(')'))
        self.assertFalse(is_balansed_braces(')('))
        self.assertFalse(is_balansed_braces('(()()(()'))
        self.assertFalse(is_balansed_braces('())('))
        self.assertFalse(is_balansed_braces('))(('))
        self.assertFalse(is_balansed_braces('((())'))

