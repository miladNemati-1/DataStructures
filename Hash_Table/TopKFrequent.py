""""
 Top K Frequent Elements

Solution
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


""""
better way is by using a heap instead of doing what you did with the dictionary manipulations




import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
"""




from collections import Counter
import heapq
def topKFrequent(nums, k):
    if k == len(nums):
        return nums

    # 1. build hash map : character and how often it appears
    # O(N) time
    count = Counter(nums)
    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    print(count.get(4))
    see = heapq.nlargest(k, count.keys(), key=count.get)
    print(see)
    return heapq.nlargest(k, count.keys(), key=count.get)


topKFrequent([4, 4, 4, 4, 4, 101, 101, 101, 9], k=2)
