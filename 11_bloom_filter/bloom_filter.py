def create_hash_fun(p : int, max_size : int):
    def hash_fun(s : str) -> int:
        h = 0
        for c in s:
            h = (h * p + ord(c)) % max_size
        return h 
    return hash_fun


class BitArray:

    def __init__(self, max_size):
        # assert max_size <= 32
        self.bits = 0
        self.mask = (1 << 32) - 1
    
    def bit(self, bit_index):
        return (self.bits & (1 << bit_index)) >> bit_index
    
    def set_bit(self, bit_index):
        self.bits |= (1 << bit_index)
    
    def reset_bit(self, bit_index):
        self.bits &= (self.mask - (1 << bit_index))


class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitarray = BitArray(f_len)
    
        self.hash1 = create_hash_fun(17,  self.filter_len)
        self.hash2 = create_hash_fun(223, self.filter_len)

    def add(self, str1):
        self.bitarray.set_bit(self.hash1(str1))
        self.bitarray.set_bit(self.hash2(str1))

    def is_value(self, str1) -> bool:
        return self.bitarray.bit(self.hash1(str1)) == 1 and self.bitarray.bit(self.hash2(str1)) == 1

