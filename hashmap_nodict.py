class MyHashMap:

    def __init__(self):
        self.set = [None] * 10000000

    def put(self, key: int, value: int) -> None:
        self.set[self.hash_function(key)] = value

    def get(self, key: int) -> int:
        # print(self.set)
        print(self.set[self.hash_function(key)])
        if self.contains(key):
            return self.set[self.hash_function(key)]
        return -1

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[self.hash_function(key)] = None

    def hash_function(self, key: int) -> int:
        return key % 10000000

    def contains(self, key: int) -> bool:
        if self.set[self.hash_function(key)] == None:
            return False
        return True


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
