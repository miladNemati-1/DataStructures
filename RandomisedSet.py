"""
Problem

Insert Delete GetRandom O(1)

Solution
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

"""
import random


class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if self.set.__contains__(val):
            return False
        self.set[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not self.set.__contains__(val):
            return False

        last_value = self.list[-1]
        index = self.set[val]

        self.list[index] = last_value

        self.set[last_value] = self.set[val]

        self.set.__delitem__(val)
        self.list.pop()

        return True

    def getRandom(self) -> int:
        end = len(self.list)-1

        random_index = random.randint(0, end)

        return self.list[random_index]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.remove(0)
param_2 = obj.remove(0)
param_3 = obj.insert(0)
param_4 = obj.getRandom()
param_5 = obj.remove(0)
param_6 = obj.insert(0)


# print(param_6)


# print(param_7)
