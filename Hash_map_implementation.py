class MyHashMap:

    def __init__(self):
        self.set = {}

    def put(self, key: int, value: int) -> None:
        self.set[self.hash_function(key)] = value

    def get(self, key: int) -> int:
        if self.contains(key):
            return self.set[self.hash_function(key)]
        return -1

    def remove(self, key: int) -> None:
        if self.contains(key):
            del (self.set[self.hash_function(key)])

    def hash_function(self, key: int) -> int:
        return key % 5000000000

    def contains(self, key: int) -> bool:
        for existing_key in self.set.keys():
            if existing_key == self.hash_function(key):
                return True
        return False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
