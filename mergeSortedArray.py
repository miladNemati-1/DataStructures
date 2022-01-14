"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

"""


def mergeSortedArray(m, n, nums1, nums2):
    if m + n == n:
        for i in range(n):
            nums1[i] = nums2[i]
    elif m + n == m:
        return
    elif m == n:
        index = 0
        for i in range(n, len(nums1)):
            nums1[i] = nums2[index]
            if index < n:
                index += 1
    else:
        index = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[index]
            if index < n:
                index += 1

    nums1.sort()






mergeSortedArray(1, 5, [4, 0, 0, 0, 0, 0], [1, 2, 3, 5, 6])
