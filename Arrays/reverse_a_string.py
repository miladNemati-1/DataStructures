class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        self.reverseStringHelper(s)


    def reverseStringHelper(self,s,a= None):


        if len(s) < 1:
            return
        a = s.pop()


        self.reverseStringHelper(s,a)
        return s.insert(0,a)

solution = Solution()

solution.reverseString(['a','p','d'])