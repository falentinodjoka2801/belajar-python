class HashTable():
    def __init__(self) -> None:
        self.capacity   =   10
        self.data       =   [None for _ in range(self.capacity)]
    
    def hash_key(self, key) -> int:
        string_key  =   str(key)
        
        total_ascii =   0
        for character in string_key:
            ascii_number    =   ord(character)
            total_ascii     +=  ascii_number
        
        hashed_key  =   total_ascii % self.capacity
        return hashed_key

    def __setitem__(self, key, value) -> None:
        hashed_key  =   self.hash_key(key)
        self.data[hashed_key]   =   value

    def __getitem__(self, key):
        hashed_key  =   self.hash_key(key)
        return self.data[hashed_key]
    
    def __delitem__(self, key) -> None:
        hashed_key  =   self.hash_key(key)
        self.data[hashed_key]   =   None
