class HashTable():
    def __init__(self) -> None:
        self.size_of_storage    =   10
        self.array              =   [None for _ in range(self.size_of_storage)]

    def get_hash(self, key) -> int:
        sum_of_ascii    =   0
        for character in key:
            sum_of_ascii    +=  ord(character)
        return sum_of_ascii % self.size_of_storage

    def __setitem__(self, key, value) -> None:
        hashed_key  =   self.get_hash(key)
        self.array[hashed_key]  =   value

    def __getitem__(self, key):
        hashed_key  =   self.get_hash(key)
        return self.array[hashed_key]
    
    def __delitem__(self, key) -> None:
        hashed_key  =   self.get_hash(key)
        self.array[hashed_key]  =   None