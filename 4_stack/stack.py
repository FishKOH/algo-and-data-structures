class Stack:
    def __init__(self):
        self.stack = [] 
        # |      | native_list/dynamic_array      | linked_list                   |
        # | ---  | ---                            | ---                           |
        # | tail | size O(1) pop O(1) push O(1)   | size O(N) pop O(1) push O(1)  |
        # | head | size O(1) pop O(N) push O(N)   | size O(N) pop O(1) push O(1)  |

    def size(self):
        return len(self.stack)

    def pop(self):
        # ваш код
        return None # если стек пустой

    def push(self, value):
        # ваш код

    def peek(self):
        # ваш код
        return None # если стек пустой
