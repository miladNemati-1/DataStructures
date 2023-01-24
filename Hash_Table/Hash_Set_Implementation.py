class MyHashSet:

    def __init__(self):
        self.set = {}

    def add(self, key: int) -> None:

        self.set[self.hash_function(key)] = None

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


# "add","remove","add","remove","remove","add","add","add","add","remove"]

# [[9], [19],   14],   [19],     [9],     [0],  [3],  [4], [0],   [9]]
# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(9)
obj.remove(19)
obj.add(14)
obj.remove(19)
obj.remove(9)
obj.add(0)
obj.add(3)
obj.add(4)
obj.add(0)
obj.remove(9)

param_3 = obj.contains(5)

'''
class HashSet:
    CONST = 2 ** 61 - 1

    def __init__(self, size = 10_000):
        self.size = size * 2
        self.contents = [None] * self.size

    def hash(self, x):
        return x % CONST

    def put(self, key):
        idx = self.hash(key) % self.size
        arr = self.contents[idx]
        if arr is None:
            self.contents[idx] = [key]
        elif key not in arr:
            arr.append(key)
        return None

    def get(self, key):
        idx = self.hash(key) % self.size
        arr = self.contents[idx]
        if arr is None or key not in arr:
            return False
        return True
        '''
