class HashTableList():
    def __init__(self) -> None:
        self.size_of_storage    =   10
        self.array              =   [[] for _ in range(self.size_of_storage)]

    def get_hash(self, key) -> int:
        sum_of_ascii    =   0
        for character in key:
            sum_of_ascii    +=  ord(character)
        return sum_of_ascii % self.size_of_storage

    def __setitem__(self, key, value) -> None:
        hashed_key  =   self.get_hash(key)
        
        found   =   False
        for index, tuple_element in enumerate(self.array[hashed_key]):
            if tuple_element[0] == key:
                self.array[hashed_key][index]  =   (key, value)
                found   =   True
                break
        
        if not found:
            self.array[hashed_key].append((key, value))

    def __getitem__(self, key):
        hashed_key  =   self.get_hash(key)
        
        for tuple_key, tuple_value in self.array[hashed_key]:
            if tuple_key == key:
                return tuple_value
    
    def __delitem__(self, key) -> None:
        hashed_key  =   self.get_hash(key)
        
        for index, tuple_element in enumerate(self.array[hashed_key]):
            if tuple_element[0] == key:
                del self.array[hashed_key][index]