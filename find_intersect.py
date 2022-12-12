
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


class Solution:
    def intersection(self, nums1, nums2):

        return set(set(list(nums1) + list(nums2))) - set(list(set(nums1) - set(nums2)) + list(set(nums2) - set(nums1)))


sol = Solution()

a = sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])

print(a)
