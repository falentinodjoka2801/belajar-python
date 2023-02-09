class HashTableList():
    def __init__(self) -> None:
        self.capacity   =   10
        self.data       =   [[] for _ in range(self.capacity)]

    def hash_key(self, key) -> int:
        string_key  =   str(key)

        total_ascii =   0
        for character in string_key:
            ascii_number    =   ord(character)
            total_ascii     +=  ascii_number

        return total_ascii % self.capacity
 
    def __setitem__(self, key, value) -> None:
        hashed_key  =   self.hash_key(key)

        data_exist  =   False
        for index, tuple_item in enumerate(self.data[hashed_key]):
            tuple_key, tuple_value = tuple_item
            if tuple_key == key:
                self.data[hashed_key][index]    =   (key, value)
                data_exist  =   True
                break

        if not data_exist:
            self.data[hashed_key].append((key, value))
    
    def __getitem__(self, key):
        hashed_key  =   self.hash_key(key)
        
        for tuple_item in self.data[hashed_key]:
            tuple_key, tuple_value  =   tuple_item
            if tuple_key == key:
                return tuple_value

        return None
    
    def __delitem__(self, key) -> None:
        hashed_key  =   self.hash_key(key)
        
        for index, tuple_item in enumerate(self.data[hashed_key]):
            tuple_key, _    =   tuple_item
            if tuple_key == key:
                del self.data[hashed_key][index]
                break