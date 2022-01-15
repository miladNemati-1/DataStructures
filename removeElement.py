"""

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

RETURN K
"""

def removeElement(nums, val):
    k = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = "null"
            k -= 1
    nums.sort()
    return k




removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)



