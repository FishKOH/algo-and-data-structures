class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        self.__size = 0
        self.__capacity = 0

    def MakeHeap(self, array, depth):
        self.__size = 0
        self.__capacity = (1 << (depth + 1)) - 1
        self.HeapArray = [None] * self.__capacity
        for v in array:
            self.Add(v)

    def GetMax(self):
        if self.__size == 0:
            return -1
        
        maxKey = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.__size - 1]
        self.HeapArray[self.__size - 1] = None
        self.__size -= 1
        
        self.__sift_down()
                    
        return maxKey
        

    def Add(self, key):
        if self.__size == self.__capacity:
            return False

        self.__size += 1
        self.HeapArray[self.__size - 1] = key
        
        self.__sift_up()
                
        return True
        
    def __sift_down(self):
        index = 0
        lci = self.__left_child_index(index)
        rci = self.__right_child_index(index)
        while (lci is not None and self.HeapArray[lci] > self.HeapArray[index] 
                or rci is not None and self.HeapArray[rci] > self.HeapArray[index]):
            
            if lci is not None and rci is not None:
                candidate = rci if self.HeapArray[rci] > self.HeapArray[lci] else lci
            if lci is None:
                candidate = rci
            if rci is None:
                candidate = lci

            self.HeapArray[candidate], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[candidate]
            index = candidate
            lci = self.__left_child_index(index)
            rci = self.__right_child_index(index)
    
    def __sift_up(self):
        index = self.__size - 1
        pi = self.__parent_index(index)
        while pi is not None and self.HeapArray[pi] < self.HeapArray[index]:
            self.HeapArray[pi], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[pi]
            index = pi
            pi = self.__parent_index(index)
    
    def __left_child_index(self, index):
        child_index = 2 * index + 1
        return child_index if child_index < self.__size else None
    
    def __right_child_index(self, index):
        child_index = 2 * index + 2
        return child_index if child_index < self.__size else None
    
    def __parent_index(self, index):
        if index == 0:
            return None
        if index % 2 == 0:
            return (index - 2 ) // 2
        return (index - 1 ) // 2
