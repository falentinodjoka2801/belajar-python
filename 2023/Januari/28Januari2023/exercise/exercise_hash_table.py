class ExerciseHashTable():
    def __init__(self) -> None:
        self.max    =   10
        self.array  =   [[] for _ in range(self.max)]

    def get_hash(self, key: str) -> int:
        sum_of_ascii    =   0
        for character in key:
            ascii_number    =   ord(character)
            sum_of_ascii    +=  ascii_number

        return sum_of_ascii % self.max

    def __setitem__(self, key: str, value: any) -> None:
        hashed_key  =   self.get_hash(key)

        element_exist   =   False
        for index, tuple_element in enumerate(self.array[hashed_key]):
            tuple_key, _  =   tuple_element
            if tuple_key == key:
                self.array[hashed_key][index]   =   (key, value)
                element_exist   =   True
                break
        
        if not element_exist:
            self.array[hashed_key].append((key, value))

    def __getitem__(self, key: str):
        hashed_key  =   self.get_hash(key)

        for tuple_key, tuple_value in self.array[hashed_key]:
            if tuple_key == key:
                return tuple_value

    def __delitem__(self, key: str) -> None:
        hashed_key  =   self.get_hash(key)

        for index, tuple_element in enumerate(self.array[hashed_key]):
            tuple_key, _  =   tuple_element
            if tuple_key == key:
                del self.array[hashed_key][index]