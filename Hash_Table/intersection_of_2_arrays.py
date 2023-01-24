
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
import collections



def intersect(nums1, nums2):
    answer = {}
    final_arr = []
    nums1_map = collections.Counter(nums1)
    nums2_map = collections.Counter(nums2)
    for i,number in enumerate(nums1):
        if nums1_map.__contains__(number) and nums2_map.__contains__(number):
            min_occurances = min(nums1_map[number], nums2_map[number])
            answer[number] = min_occurances
    for item in answer:
        final_arr.append([item]*answer[item])
    final_arr = sum(final_arr, [])
    return final_arr



intersect([3,2,1,1,3],[1,8,9,1,1,2,2])