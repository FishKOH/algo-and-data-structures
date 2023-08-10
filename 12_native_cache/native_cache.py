class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.__step = 1
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key : str):
        assert isinstance(key, str)

        p = 223
        hash = 0
        for c in key:
            hash = (hash * p + ord(c)) % self.size
        return hash
    
    def __seek_slot(self, key : str) -> int: #or None
        index = self.hash_fun(key)

        for _ in range(self.size):
            if self.slots[index] is None:
                return index
                
            index = (index + self.__step) % self.size
        return None

    def __put_key(self, key : str) -> int: #or None
        index = self.__seek_slot(key)
        if index is None:
            return None
        
        self.slots[index] = key
        return index
        
    # change method private to public for count hits at NativeCache
    def find(self, key : str)-> int: #or None
        index = self.hash_fun(key)

        for _ in range(self.size):
            if self.slots[index] is None:
                return None                
            if self.slots[index] == key:
                return index
                
            index = (index + self.__step) % self.size
        return None    
    
    def is_key(self, key):
        return self.find(key) is not None

    def put(self, key, value):
        index = self.find(key)
        if index is None:
            index = self.__put_key(key)
        
        if index is not None:
            self.values[index] = value
            return index
        
        return None #add return value for detect fullness(alternate can add self.cur_size)

    def get(self, key):
        index = self.find(key)
        if index is None:
            return None

        return self.values[index]


class NativeCache(NativeDictionary):
    def __init__(self, sz):
        super().__init__(sz)
        self.hits = [0] * self.size
    
    def __replace(self, key, value):
        min_hit_pos = self.hits.index(min(self.hits))
        self.slots[min_hit_pos] = key
        self.values[min_hit_pos] = value
            
    def __count_hit(self, key):
        index = self.find(key)
        if index is not None:
            self.hits[index] += 1
    
    def is_key(self, key):
        self.__count_hit(key)
        return super().is_key(key)

    def put(self, key, value):
        if super().put(key, value) is None:
            self.__replace(key, value)
        self.__count_hit(key)

    def get(self, key):
        self.__count_hit(key)
        return super().get(key)

