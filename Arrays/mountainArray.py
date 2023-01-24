"""

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""
arr = [0, 3, 2, 1]



def isItaMountainArray(arr):
    peak = arr.index(max(arr))
    if peak == 0 or peak == len(arr) - 1:
        return False
    if len(arr) < 3:
        return False
    for i in range(0, peak):
        if arr[i] >= arr[i + 1]:
            return False
    for x in range(peak, len(arr) - 1):
        if arr[x] <= arr[x + 1]:
            return False
    return True



result = isItaMountainArray([0,1,2,4,2,1])

print(result)