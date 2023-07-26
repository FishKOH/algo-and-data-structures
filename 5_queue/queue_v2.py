import os
import sys

script_dir = os.path.dirname(__file__)
stack_dir = os.path.join(script_dir, '..', '4_stack')
sys.path.append(stack_dir)
#learn correct way for import local modules
from stack import Stack


class Queue:
    def __init__(self):
        # Time Complexity
        # |                    | enqueue  | dequeue    | size |
        # | ---                | ---      | ---        | ---  |
        # | two stacks         | O(1)     | Amort O(1) | O(1) |
        self.__stack_in = Stack()
        self.__stack_out = Stack()

    def __transfer(self):
        if self.__stack_out.size() == 0:
            while self.__stack_in.size() > 0:
                self.__stack_out.push(self.__stack_in.pop())

    def enqueue(self, item):
        self.__stack_in.push(item)

    def dequeue(self):
        self.__transfer()
        return self.__stack_out.pop()

    def size(self):
        return self.__stack_in.size() + self.__stack_out.size()
