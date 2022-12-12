

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = MyHashSet()
        for number in nums:
            if hashSet.contains(number):
                return True
            hashSet.add(number)
        return False


class MyHashSet:

    def __init__(self):
        self.set = [None] * 1000000

    def add(self, key: int) -> None:

        self.set[self.hash_function(key)] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[self.hash_function(key)] = None

    def hash_function(self, key: int) -> int:
        return hash(key)

    def contains(self, key: int) -> bool:
        if self.set[self.hash_function(key)] == None:
            return False
        return True


a = Solution()

print(a.containsDuplicate())
