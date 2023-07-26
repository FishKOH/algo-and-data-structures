import operator
import unittest
from stack import Stack

def calc_postfix_expression(expr_stack : Stack) -> int:
    def is_binary_op(item):
        return item in '+-*/';
    
    def compute(op, value1, value2):
        operators = {
            '+':operator.add, 
            '-':operator.sub, 
            '*':operator.mul, 
            '/':operator.truediv
        }
        return operators[op](value1, value2)
    
    calc_stack = Stack()
    while expr_stack.size() > 0:
        item = expr_stack.pop()
        if is_binary_op(item):
            op = item
            value2 = calc_stack.pop()
            value1 = calc_stack.pop()
            if value1 is None or value2 is None:
                raise ValueError('incorrect expression: not enough values')
            else:
                calc_stack.push(compute(op, int(value1), int(value2)))
        else:
            calc_stack.push(item)
    return calc_stack.peek()

def calc_postfix_expression_str(expr : str) -> int:
    expr_stack = Stack()
    for item in expr.split()[::-1]:
        expr_stack.push(item)
    return calc_postfix_expression(expr_stack)
    

class TestCalcPostfixExpr(unittest.TestCase):
    
    def test_simple(self):
        self.assertEqual(calc_postfix_expression_str('3 5 +'), 8)
        self.assertEqual(calc_postfix_expression_str('4 2 *'), 8)
        self.assertEqual(calc_postfix_expression_str('10 2 -'), 8)
        self.assertEqual(calc_postfix_expression_str('16 2 /'), 8.0)
        
    def test_complex(self):
        self.assertEqual(calc_postfix_expression_str('1 2 + 3 *'), 9)
        self.assertEqual(calc_postfix_expression_str('15 7 1 1 + - / 3 *'), 9) # 15 / (7 - (1 + 1)) * 3
        self.assertEqual(calc_postfix_expression_str('15 7 1 1 + - / 3 * 2 1 1 + + - '), 5) # 15 / (7 - (1 + 1)) * 3 - (2 + (1 + 1)
    
    def test_incorrect(self):
        with self.assertRaises(ValueError):
            calc_postfix_expression_str('1 + ')
        with self.assertRaises(ValueError):
            calc_postfix_expression_str('1 1 + 2 + *')    
