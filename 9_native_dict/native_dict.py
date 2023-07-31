class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.__step = 1
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key : str):
        assert isinstance(key, str)

        p = 13
        hash = 0
        for c in key:
            hash = hash * p + ord(c)
        return hash % self.size
    
    def __seek_slot(self, value : str) -> int: #or None
        index = self.hash_fun(value)

        for _ in range(self.size):
            if self.slots[index] is None:
                return index
                
            index = (index + self.__step) % self.size
        return None

    def __put(self, value : str) -> int: #or None
        index = self.__seek_slot(value)
        if index is None:
            return None
        
        self.slots[index] = value
        return index
        

    def __find(self, value : str)-> int: #or None
        index = self.hash_fun(value)

        for _ in range(self.size):
            if self.slots[index] is None:
                return None                
            if self.slots[index] == value:
                return index
                
            index = (index + self.__step) % self.size
        return None    
    
    def is_key(self, key):
        return self.__find(key) is not None

    def put(self, key, value):
        index = self.__find(key)
        if index is None:
            index = self.__put(key)
        
        if index is not None:
            self.values[index] = value

    def get(self, key):
        index = self.__find(key)
        if index is None:
            return None

        return self.values[index]
