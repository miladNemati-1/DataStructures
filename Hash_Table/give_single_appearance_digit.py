class Solution:
    def singleNumber(self, nums):
        number_set = set()
        for number in nums:
            if number_set.__contains__(number):
                number_set.remove(number)
            else:
                number_set.add(number)
        return list(number_set)[0]


sol = Solution()

answer = sol.singleNumber([4, 1, 2, 1, 2])
print(answer)
