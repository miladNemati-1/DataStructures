"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeros(nums):
    countZero = nums.count(0)
    for i in range(len(nums)):

        if nums[i] == 0:
            for x in range(i, len(nums) - 1):
                nums[x] = nums[x + 1]
    for i in range(-1, -countZero-1, -1):
        nums[i] = 0
    print(nums)





moveZeros([0,0,1])