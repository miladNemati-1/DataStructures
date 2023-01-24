"""
  4Sum II

Solution
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

1: 1, 2: 3, -1:3 , -2:1, 0: 1

2:2 , -1:2, 0:1 -> comb 1 has theese numbers

1:1, -1:1, 2:1, -2:1 -> comb 2 has these numbers


import itertools

numbers = [1, 2, 3, 7, 7, 9, 10]
target = 10

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]

print(result)
"""
import collections
import itertools


# def whichCombOfFourAddsToZero(numbers, target):

#     result = [seq for i in range(len(numbers), 0, -1)
#               for seq in itertools.combinations(numbers, i)
#               if sum(seq) == target if len(seq) == 4]
#     return max(result)


def fourSumCount(nums1, nums2, nums3, nums4):
    n, hm, res = len(nums1), collections.defaultdict(int), 0

    for i in range(n):
        for j in range(n):
            hm[nums1[i] + nums2[j]] += 1

    for k in range(n):
        for l in range(n):
            res += hm[0 - (nums3[k] + nums4[l])]

    return res


fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
