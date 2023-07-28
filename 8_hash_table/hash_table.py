class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value : str) -> int: #or None; int|None available at python 3.10
        assert isinstance(value, str)

        p = 13
        hash = 0
        for c in value:
            hash = hash * p + ord(c)
        return hash % self.size

    def seek_slot(self, value : str) -> int: #or None
        index = self.hash_fun(value)

        steps = 0
        while steps < self.size:
            if self.slots[index] is None:
                return index
                
            index = (index + self.step) % self.size
            steps += 1
        return None

    def put(self, value : str) -> int: #or None
        index = self.seek_slot(value)
        if index is None:
            return None
        
        self.slots[index] = value
        return index
        

    def find(self, value : str)-> int: #or None
        index = self.hash_fun(value)

        steps = 0
        while steps < self.size:
            if self.slots[index] is None:
                return None                
            if self.slots[index] == value:
                return index
                
            index = (index + self.step) % self.size
            steps += 1
        return None
