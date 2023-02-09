class HashTable():
    def __init__(self) -> None:
        self.capacity   =   10
        self.data       =   [None for _ in range(self.capacity)]
    
    def hash(self, key) -> int:
        string_key: str     =   str(key)
        
        total_ascii =   0
        for character in string_key:
            ascii_number    =   ord(character)
            total_ascii     +=  ascii_number
        
        index   =   total_ascii % self.capacity
        return index

    def __setitem__(self, key, value) -> None:
        hashed_index    =   self.hash(key)
        self.data[hashed_index] =   value

    def __getitem__(self, key):
        hashed_index    =   self.hash(key)
        item    =   self.data[hashed_index]
        return item

    def __delitem__(self, key) -> None:
        hashed_index    =   self.hash(key)
        self.data[hashed_index] =   None