"""
  Contains Duplicate II

Solution
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

def find_duplicated_extended_problem(numbers,k):
    number_indices_dict = {}
    for index,number in enumerate(numbers):
        if number_indices_dict.__contains__(number) and abs(number_indices_dict[number] - index) <= k:
            return True
        else:
            number_indices_dict[number] = index
    return False


print(find_duplicated_extended_problem([1,2,3,1,2,3],2))