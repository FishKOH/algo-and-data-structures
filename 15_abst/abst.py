class aBST:

    def __init__(self, depth):
        tree_size = (1 << (depth + 1)) - 1
        self.Tree = [None] * tree_size # массив ключей
    
    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2
    
    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree) and self.Tree[index] is not None:
            curr_node_key = self.Tree[index]
            if key == curr_node_key:
                return index
                
            if key < curr_node_key:
                index = self.__left_child(index)
            else:
                index = self.__right_child(index)
                
        if index >= len(self.Tree):
            return None
        
        return -index #index_for_add
    
    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1 
            
        if index <= 0:
            index = -index
            self.Tree[index] = key
        
        return index

