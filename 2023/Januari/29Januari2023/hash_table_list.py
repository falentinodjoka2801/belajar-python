class HashTableList():
    def __init__(self):
        self.capacity   =   10
        self.data       =   [[] for _ in range(self.capacity)]
    
    def hash(self, key) -> int:
        stringKey: str  =   str(key)

        total_ascii =   0
        for character in stringKey:
            ascii_number    =   ord(character)
            total_ascii     +=  ascii_number

        index   =   total_ascii % self.capacity
        return index

    def __setitem__(self, key, value) -> None:
        hashed_index    =   self.hash(key)

        exist   =   False
        for index, tuple_element in enumerate(self.data[hashed_index]):
            tuple_key, tuple_value  =   tuple_element
            if key == tuple_key:
                self.data[hashed_index][index]  =   (key, value)
                exist   =   True
                break
            
        if not exist:
            self.data[hashed_index].append((key, value))

    def __getitem__(self, key):
        hashed_index    =   self.hash(key)
        
        for tuple_element in self.data[hashed_index]:
            tuple_key, tuple_value  =   tuple_element
            if tuple_key == key:
                return tuple_value

    def __delitem__(self, key) -> None:
        hashed_index    =   self.hash(key)

        for index, tuple_element in enumerate(self.data[hashed_index]):
            tuple_key, _  =   tuple_element
            if tuple_key == key:
                del self.data[hashed_index][index]
                break