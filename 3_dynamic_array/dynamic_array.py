import ctypes

class DynArray:
    
    realloc_multiplier = 2
    dealloc_threshold = 0.5
    dealloc_divider = 1.5
    minimal_capacity = 16
    
    def __init__(self):
        self.count = 0
        self.capacity = self.minimal_capacity
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def __fullness(self):
        return self.count/self.capacity

    def __realloc(self):
        if self.count == self.capacity:
            self.resize(self.realloc_multiplier*self.capacity)

    def __dealloc(self):
        if self.__fullness() < self.dealloc_threshold:
            self.resize(max(self.minimal_capacity, int(self.capacity / self.dealloc_divider)))

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        # time complexity - O(N)
        assert new_capacity >= self.minimal_capacity, f"Couldn't resize({new_capacity}). {self.minimal_capacity} is minimal capacity"
        
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        # time complexity - Asymptotic O(1)
        self.__realloc()
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # time complexity - O(N)
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        self.__realloc()
        for idx in reversed(range(i, self.count)):
            self.array[idx+1] = self.array[idx]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        # time complexity - O(N)
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for i in range(i, self.count-1):
            self.array[i] = self.array[i+1]
        self.count -= 1    
        self.__dealloc()

