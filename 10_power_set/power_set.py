# PowerSetBasedNativeList
class PowerSet():

    def __init__(self):
        self.__storage = []

    def size(self):
        return len(self.__storage)

    def put(self, value):
        # O(N)
        if value not in self.__storage:
            self.__storage.append(value)

    def get(self, value):
        # O(N)
        return value in self.__storage

    def remove(self, value):
        # O(N)
        if value not in self.__storage:
            return False

        self.__storage.remove(value)
        return True

    def intersection(self, set2):
        # O(N*N)
        intersection_set = PowerSet()
        for value in self.__storage:
            if set2.get(value):
               intersection_set.put(value) 
            
        return intersection_set

    def union(self, set2):
        # O(N*N)
        union_set = PowerSet()
        for value in self.__storage:
            union_set.put(value)
        for value in set2.__storage:
            union_set.put(value)
        return union_set

    def difference(self, set2):
        # O(N*N)
        diff_set = PowerSet()
        for value in self.__storage:
            if not set2.get(value):
                diff_set.put(value)
        return diff_set

    def issubset(self, set2):
        # O(N*N)
        return all( self.get(value) for value in set2.__storage)

# PowerSet = PowerSetBasedNativeList
