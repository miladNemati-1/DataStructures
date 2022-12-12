class MyHashSet:

    def __init__(self):
        self.set = [None] * 10000000

    def add(self, key: int) -> None:

        self.set[self.hash_function(key)] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[self.hash_function(key)] = None

    def hash_function(self, key: int) -> int:
        return key % 10000000

    def contains(self, key: int) -> bool:
        if self.set[self.hash_function(key)] == None:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# Your MyHashSet object will be instantiated and called as such:
