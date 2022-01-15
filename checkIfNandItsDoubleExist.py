"""
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.



----Best solution on leetcode----

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a = {}
        for i in range(len(arr)):
            if arr[i]*2 in a or arr[i]/2 in a:
                return True
            if arr[i] not in a:
                a[arr[i]] = None
        return False
"""

def checkifexists(array):

    exists = False
    for i in range(len(array)):
        for x in range(len(array)):
            if array[i] == array[x] * 2 and i != x:
                exists = True
                return exists
    return exists

print(checkifexists([-2,0,10,-19,4,6,-8]))













print(checkifexists([-2,0,10,-19,4,6,-8]))



