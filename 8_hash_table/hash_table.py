class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

     def hash_fun(self, value : str) -> int: #or None
         assert isistance(value, str)

         # всегда возвращает корректный индекс слота
         return 0

     def seek_slot(self, value : str) -> int: #or None
         # находит индекс пустого слота для значения, или None
         return None

     def put(self, value : str) -> int: #or None
         # записываем значение по хэш-функции
         
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 
         return None

     def find(self, value : str)-> int: #or None
         # находит индекс слота со значением, или None
         return None
